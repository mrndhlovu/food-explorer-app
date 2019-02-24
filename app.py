#  Flask Receipe App
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymomgo import PyMongo
from bson.objectid import ObjectId
import pymongo

# Test for connection to DB

MONGODB_URI = os.getenv('MONGO_URI')
DBS_NAME = "cuisineAppDB"
COLLECTION_NAME = "userRecipes"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)  

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)
    
# Connecto heroku app

app = Flask(__name__)

app.config["MONGO_DNAME"] = 'milestone3-recipe-app'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-ghrjb.mongodb.net/cuisineAppDB?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.fidn())
    

@app.route('/')
def index():
    return "HelloWorld Again!"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    
   
    