#  Flask Receipe App
import os
#import pymongo
from flask import Flask, render_template, redirect, request,session,url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime


app = Flask(__name__)

app.config["MONGO_DNAME"] = 'cuisineAppDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-j5cta.mongodb.net/cuisineAppDB?retryWrites=true'

mongo = PyMongo(app)

app.secret_key = 'the random string'
app.config['SECRET_KEY'] = 'the random string' 
SECRET_KEY = 'the random string'

# os.urandom(24)

# SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'


@app.route('/index')
def index():
    if 'username' in session:
        return "You are logged in as " + session ['username']
    return render_template("register.html")
    
    
@app.route('/get_cuisine')
def get_cuisine():
    return render_template("cuisine.html", recipes=mongo.db.userRecipes.find())

@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.categories.find()
    category_found = [category for category in categories]
    return render_template("addrecipe.html", categories = category_found)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.userRecipes

    last_modified = {'last_modified': datetime.today().strftime('%d, %b %Y')}
    recipe.insert(last_modified)
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisine'))

    

# check if user is has a username already if true point to add recipe pag
@app.route('/login', methods=['GET', 'POST'])
def login():
    users = mongo.db.usersDB
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        
        return redirect(url_for('index'))

    return 'You need to register!'
    
@app.route('/')    
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.usersDB
        existing_user = users.find_one({'name' : request.form['username']})
       
        if existing_user is None:
            
            users.insert({'name' : request.form['username'], 'passcode' : request.form['password']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

if __name__  == '__main__':
    app.secret_key = '123'
    app.run(debug=True)
    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        
 