#  Flask Receipe App
import os
from flask import Flask, render_template, redirect, request,session,url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from datetime import datetime
from operator import attrgetter
from bson import ObjectId
import statistics
import datetime
import datetime as DT

app = Flask(__name__)

app.config["MONGO_DNAME"] = 'cuisineAppDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-j5cta.mongodb.net/cuisineAppDB?retryWrites=true'

mongo = PyMongo(app)

app.secret_key = 'some random password'
app.config['SECRET_KEY'] = 'some random password' 
SECRET_KEY = 'some random password'


@app.route('/index')
def index():
    if 'username' in session:
        return  redirect(url_for('get_cuisine'))
    return render_template("index.html")

def e_sort(recipe):
    return recipe.date_updated

@app.route('/')    
@app.route('/get_cuisine')
def get_cuisine():
    if 'username' in session:
        favourites = mongo.db.usersDB.find_one({'username': session['username']})
        favourites_found = favourites['userFavourites']
    else:
        favourites = ''
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    today = today = DT.date.today()
    week_ago = today - DT.timedelta(days=30)
    most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5)
    srted = most_recent.sort('date_updated',  pymongo.DESCENDING)
    direction = lambda  most_recent: most_recent[1]
    print('most_recent: ', most_recent)
    return render_template("cuisine.html", recipes=mongo.db.userRecipes.find().sort('date_updated', pymongo.DESCENDING), categories = category_found, most_recent=srted, favourites=favourites)


@app.route('/add_recipe')
def add_recipe():
    if 'username' in session:
        favourites = mongo.db.usersDB.find_one({'username': session['username']})
    else:
        favourites = ''
    today = today = DT.date.today()
    most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5)
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    if 'username' in session:
        return render_template("addrecipe.html", categories = category_found, most_recent= most_recent, favourites=favourites)
    return redirect(url_for('index'))


#  Remove favourite record from favourites list
@app.route('/remove_favourites/<_id>')
def remove_favourites(_id):
    users = mongo.db.usersDB
    user_record = mongo.db.usersDB.find({'username': session['username']})
    for favourites in user_record: 
        for favourite in favourites['userFavourites']:
            if _id == favourite['id']:
                remove_id = favourite['id']
                users.update({'username': session['username']},{"$pull": {"userFavourites":{ "id": remove_id }}})
    return redirect(url_for('get_cuisine'))
    

# create new recipe record
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.userRecipes
    userRecipe = { 'uploaded_by': session['username'],
        'record': {
            "title":   request.form['title'],
            "category":  request.form['category'],
            "country":  request.form['country'],
            "ingredients":  request.form.getlist('ingredient'),
            "directions":  request.form.getlist('directions'),
            "allergens":  request.form.getlist('allergens')
        },
            
        'up_votes': 0,
         'down_votes': 0,
        'views': 0,
        'date_updated': datetime.datetime.now().strftime('%Y-%m-%d')
    }
    recipe.insert_one(userRecipe)
    return redirect(url_for('get_cuisine'))
    
 
# edit recipe
@app.route('/edit_recipe/<_id>')
def edit_recipe(_id): 
    if 'username' in session:
        favourites = mongo.db.usersDB.find_one({'username': session['username']})
    else:
        favourites = ''
    today = DT.date.today()
    week_ago = today - DT.timedelta(days=30)
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lt': current_date, '$gt': week_ago.strftime('%Y-%m-%d') }}).limit(5)
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    if 'username' in session:
        return render_template("editrecipe.html", recipe=id, categories=category_found, recipes=mongo.db.userRecipes.find_one({'_id': ObjectId(_id)}) ,most_recent=most_recent, favourites=favourites)
    return render_template('register.html')
    
    
# Render recipe detail and track number of views
@app.route('/show_detail/<recipe_id>')
def show_detail(recipe_id):
    if 'username' in session:
        favourites = mongo.db.usersDB.find_one({'username': session['username']})
    else:
        favourites = ''
    count = mongo.db.userRecipes
    count.update({'_id': ObjectId(recipe_id)},
    { "$inc": { "views": 1 },})
    
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    today = today = DT.date.today()
    week_ago = today - DT.timedelta(days=14)
    most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d'), '$gte': week_ago.strftime('%Y-%m-%d') }}).limit(5)
    return render_template("recipedetail.html", recipe=mongo.db.userRecipes.find({'_id': ObjectId(recipe_id)}), categories=category_found,most_recent=most_recent, favourites=favourites )   

 
# update edited recipe 
@app.route('/update_recipe/<_id>', methods=['POST'])
def update_recipe(_id): 
    recipe = mongo.db.userRecipes
    recipe.update({'_id': ObjectId(_id)},
    { "$set": 
        { 
            "record.title":  request.form.get('title'),
            "record.category":  request.form.get('category'),
            "record.country":  request.form.get('country'),
            "record.ingredients":  request.form.getlist('ingredient'),
            "record.directions":  request.form.getlist('directions'),
            "record.allergens":  request.form.getlist('allergens'),
            "date_updated": datetime.datetime.now().strftime('%Y-%m-%d'),
        },
    })
    return redirect(url_for('show_detail', recipe_id=_id))
    

# check if user is has a username already if true point to add recipe page
@app.route('/login', methods=['GET', 'POST'])
def login():
    users = mongo.db.usersDB
    login_user = users.find_one({'username' : request.form['username']})
    login_pass = users.find_one({'passcode' : request.form['password']})
    if login_user:
        if login_pass:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return ('Invalid password or username')    
    return ('Invalid password or username') 
    
 
    
# delete recipe
@app.route('/delete_recipe/<_id>', methods=["GET"])
def delete_recipe(_id):
    recipe = mongo.db.userRecipes
    if 'username' in session:
        recipe.remove({'_id': ObjectId(_id)})
        return redirect(url_for('get_cuisine'))
    return ('Invalid password or username') 

    
# Track Recipe up_votes
@app.route('/up_votes/<_id>', methods=['GET', 'POST'])
def up_votes(_id):
    # add to userLikes
    if 'username' in session:
        username = mongo.db.usersDB.find_one({'username' :session['username']})
        user = mongo.db.usersDB
        user.update({'_id': ObjectId(username['_id'])},
        { "$push": { "userLikes": _id }})
    
        #  update record likes total
        recipe = mongo.db.userRecipes
        recipe.update({'_id': ObjectId(_id)},
        { "$inc": { "up_votes": 1 },})
        
        return redirect(url_for('get_cuisine'))
    return render_template('index.html')   
    
    
# Track Recipe down_votes
@app.route('/down_votes/<_id>', methods=['GET', 'POST'])
def down_votes(_id):
    if 'username' in session:
        #  update record down votes total
        recipe = mongo.db.userRecipes
        recipe.update({'_id': ObjectId(_id)},
        { "$inc": { "down_votes": 1 },})
        return redirect(url_for('get_cuisine'))
    return render_template('index.html') 
    
    
# Track user favourites
@app.route('/favourites/<_id>/<name>', methods=['GET', 'POST'])
def favourites(_id,name):
    # Track user favourites
    if 'username' in session:
        username = mongo.db.usersDB.find_one({'username' :session['username']})
        user = mongo.db.usersDB
        user.update({'_id': ObjectId(username['_id'])},
        { "$push": 
            { 
            "userFavourites":{'id': _id, 'name': name},
            }
        })
    return redirect(url_for('show_detail', recipe_id=_id))


   
# user logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('get_cuisine'))


@app.route('/get_category/<category_id>')
def get_category(category_id):
    recipe = mongo.db.userRecipes.find()
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    return render_template("categorylist.html", recipe=recipe, category=category_id, categories=category_found )
     
    
@app.route('/browse_filter/<query>/<sort_order>')
def browse_filter(query,sort_order):
    if 'username' in session:
        favourites = mongo.db.usersDB.find_one({'username': session['username']})
    else:
        favourites = ''
    recipe = mongo.db.userRecipes.find()
    countries = [country for country in recipe ]
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    query_field = 'record.' + query
    query_found = mongo.db.userRecipes.find({query_field: sort_order}).sort('date_updated', pymongo.DESCENDING)
    today = today = DT.date.today()
    week_ago = today - DT.timedelta(days=14)
    
    most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5).sort('date_updated',  pymongo.DESCENDING )
    
    render_results = render_template("cuisine.html", recipes=query_found, categories=category_found, most_recent=most_recent, favourites=favourites, country=countries ) 
    
    if sort_order == 'descending':
        found = mongo.db.userRecipes.find({query: {"$gt": 0}}).sort([(query, -1)])
        most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5).sort('date_updated',  pymongo.DESCENDING)
        return  render_template("cuisine.html", recipes=found, categories=category_found, most_recent=most_recent, favourites=favourites ,country=countries) 
    elif sort_order == 'ascending':
        found = mongo.db.userRecipes.find({query: {"$gt": 0}}).sort([(query, 1)])
        most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5).sort('date_updated',  pymongo.DESCENDING)
        return  render_template("cuisine.html", recipes=found, categories=category_found, most_recent=most_recent, favourites=favourites, country=countries) 
    elif query == 'search':
        sort_order = request.form.get('search')
        most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5).sort('date_updated',  pymongo.DESCENDING)
        found =  mongo.db.userRecipes.find( { 'record.directions' : sort_order } ) 
        return  render_template("cuisine.html", recipes=found, categories=category_found, most_recent=most_recent, favourites=favourites, country=countries) 
    else:
        return  render_results   
    

# def insert_image(request):
#   with open(request.GET["image_name"], "rb") as image_file:
#       encoded_string = base64.b64encode(image_file.read())
#   print encoded_string
#   abc=db.database_name.insert({"image":encoded_string})
#   return HttpResponse("inserted")

# def retrieve_image(request):
#   data = db.database_name.find()
#   data1 = json.loads(dumps(data))
#   img = data1[0]
#   img1 = img['image']
#   decode=img1.decode()
#   img_tag = '<img alt="sample" src="data:image/png;base64,{0}">'.format(decode)
#   return HttpResponse(img_tag)


# register user  
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.usersDB
        user_found = users.find_one({'username' : request.form['username']})
        if user_found is None:
            users.insert({
            'userFavourites': [], 
            'is_active' : True,
            'username' : request.form['username'],
            'email' : request.form['email'], 
            'passcode' : request.form['password']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'That username has been taken, try again with a different username'
    return render_template('register.html')
    

if __name__  == '__main__':
    app.secret_key = '123'
    app.run(debug=True)
    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        


