#  Flask Receipe App
import os
#import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime


app = Flask(__name__)

app.config["MONGO_DNAME"] = 'cuisineAppDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-j5cta.mongodb.net/cuisineAppDB?retryWrites=true'

mongo = PyMongo(app)


 
@app.route('/')
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
    last_modified = datetime.now()
    recipe = mongo.db.userRecipes
    recipe.insert_one({'last_modified': last_modified})
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisine'))
    
insert_recipe()
    
    
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        
 