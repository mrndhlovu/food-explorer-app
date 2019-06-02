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
    week_ago = today - DT.timedelta(days=14)
    most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5)
    return render_template("cuisine.html", recipes=mongo.db.userRecipes.find().sort('date_updated'), categories = category_found, most_recent=most_recent.sort('date_updated'), favourites=favourites)


@app.route('/add_recipe')
def add_recipe():
    if 'username' in session:
        favourites = mongo.db.usersDB.find_one({'username': session['username']})
    else:
        favourites = ''
    today = today = DT.date.today()
    week_ago = today - DT.timedelta(days=14)
    most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5)
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    if 'username' in session:
        return render_template("addrecipe.html", categories = category_found, most_recent= most_recent, favourites=favourites)
    return redirect(url_for('index'))

@app.route('/remove_favourites/<_id>')
def remove_favourites(_id):
    print(type(_id), _id)
    favourites = mongo.db.usersDB.find({'username': session['username']})
    for index,fav in enumerate(favourites):
        liked_recipes =  fav['userFavourites']
        for fav in liked_recipes:
            if _id  ==  fav['id']:
                print(fav)
                favourites.updateMany({}, {'$unset':{"passwrod":1}})
                db.getCollection('Devices').update(
    {"FieldsCollection.Fields.FieldName":"ABC"},
    {$unset: {"FieldsCollection.$[].Fields.$[f].Fields":1}, 
     $set:{"FieldsCollection.$[].Fields.$[f].item1":"value1",
           "FieldsCollection.$[].Fields.$[f].item2":"value2"}
    },  
    {arrayFilters: [{ "f.FieldName":"ABC"} ],multi:true }
)
    # remove_like.remove({'_id': ObjectId(_id)})
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
            "directions":  request.form['directions'],
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
            "record.directions":  request.form.get('directions'),
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
    print('click', _id, name)
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
    return render_template("categorylist.html", recipe=recipe, category=category_id, categories=category_found)
     
    
@app.route('/browse_filter/<query>/<sort>')
def browse_filter(query,sort):
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    
    query_field = 'record.' + query
    query_found = mongo.db.userRecipes.find({query_field: sort})
   
    
    today = today = DT.date.today()
    week_ago = today - DT.timedelta(days=14)
    most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lte': today.strftime('%Y-%m-%d') }}).limit(5)
    
    render_results = render_template("cuisine.html", recipes=query_found, categories=category_found, most_recent=most_recent) 
    
    if sort == 'descending':
        most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lt': today.strftime('%Y-%m-%d') }}).limit(5)
        query_found = mongo.db.userRecipes.find({query: {"$gt": 0}}).sort([(query, -1)])
        return  render_template("cuisine.html", recipes=query_found, categories=category_found, most_recent=most_recent) 
    elif sort == 'ascending':
        most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lt': today.strftime('%Y-%m-%d') }}).limit(5)
        query_found = mongo.db.userRecipes.find({query: {"$gt": 0}}).sort([(query, 1)])
        return  render_template("cuisine.html", recipes=query_found, categories=category_found, most_recent=most_recent) 
    elif query == 'allergen':
        most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lt': today.strftime('%Y-%m-%d')}}).limit(5)
        query_found =  mongo.db.userRecipes.find( { 'record.allergens' : sort } )
        return  render_template("cuisine.html", recipes=query_found, categories=category_found, most_recent=most_recent) 
    elif query == 'author':
        most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lt': today.strftime('%Y-%m-%d')}}).limit(5)
        query_found =  mongo.db.userRecipes.find( { 'uploaded_by' : sort } )
        return  render_template("cuisine.html", recipes=query_found, categories=category_found, most_recent=most_recent) 
    elif query == 'recent':
        most_recent = mongo.db.userRecipes.find({ 'date_updated': {'$lt': today.strftime('%Y-%m-%d')}}).limit(5)
        query_found =  mongo.db.userRecipes.find().sort('date_updated')
        return  render_template("cuisine.html", recipes=query_found, categories=category_found, most_recent=most_recent) 
    # elif query == 'search':
    #     most_recent = mongo.db.userRecipes.find()
    #     query_found =  mongo.db.userRecipes.find( { 'uploaded_by' : sort } ) 
    #     return  render_template("cuisine.html", recipes=most_recent, categories=category_found, most_recent=most_recent) 
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
        


