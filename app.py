#  Flask Receipe App
import os
from flask import Flask, render_template, redirect, request,session,url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from bson import ObjectId
import datetime

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
    return render_template("cuisine.html", recipes=mongo.db.userRecipes.find())



@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    if 'username' in session:
        return render_template("addrecipe.html", categories = category_found)
    return redirect(url_for('index'))



# create new recipe record
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.userRecipes
    userRecipe = { 'uploaded_by': session['username'],
        'record': request.form.to_dict(),
        'up_votes': 0,
        'views': 0,
        'date_updated': datetime.datetime.now().strftime('%Y-%m-%d')
    }
    recipe.insert_one(userRecipe)
    return redirect(url_for('get_cuisine'))
 

   
# edit recipe
@app.route('/edit_recipe/<_id>')
def edit_recipe(_id): 
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    print('categories found',category_found)
    if 'username' in session:
        return render_template("editrecipe.html", recipe=id, categories=category_found, recipes=mongo.db.userRecipes.find_one({'_id': ObjectId(_id)}))
    return render_template('register.html')
    
   
@app.route('/show_detail/<recipe_id>')
def show_detail(recipe_id):
    return render_template("recipedetail.html", recipe=mongo.db.userRecipes.find({'_id': ObjectId(recipe_id)}))   

 
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
            "record.ingredients":  request.form.get('ingredients'),
            "record.directions":  request.form.get('directions'),
            "record.allergens":  request.form.get('allergens'),
            "date_updated": datetime.datetime.now().strftime('%Y-%m-%d'),
        },
    })
    return redirect(url_for('get_cuisine'))
    


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
        uploader = recipe.uploaded_by
        if uploader == 'username':
            recipe.remove({'_id': ObjectId(_id)})
            return redirect(url_for('get_cuisine'))
    return ('Invalid password or username') 
    

@app.route('/add_like')
def add_like():
   print("I was clicked")
 
    
# user logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('get_cuisine'))



# register user  
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.usersDB
        user_found = users.find_one({'username' : request.form['username']})
        if user_found is None:
            users.insert({'userFavourites': [], 
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
        


