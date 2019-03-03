#  Flask Receipe App
import os
#import pymongo
from flask import Flask, render_template, redirect, request, url_for
#from flask_pymomgo import PyMongo
#from bson.objectid import ObjectId


# Test for connection to DB

# MONGODB_URI = os.getenv('MONGO_URI')
# DBS_NAME = "cuisineAppDB"
# COLLECTION_NAME = "userRecipes"

# def mongo_connect(url):
#     try:
#         conn = pymongo.MongoClient(url)
#         print("Mongo is connected")
#         return conn
#     except pymongo.errors.ConnectionFailure as e:
#         print("Could not connect to MongoDB: %s") % e
# app.config["MONGO_DNAME"] = 'milestone3-recipe-app'
# app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-ghrjb.mongodb.net/cuisineAppDB?retryWrites=true'
# mongo = PyMongo(app)
        
#...........................................................Connect heroku app

app = Flask(__name__)
    

@app.route('/')
def index():
    return "HelloWorld Again!"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        
#.......................start app       
# def show_menu():
#     print("")
#     print("1. Add a record")
#     print("2. Find a record by name")
#     print("3. Edit a record")
#     print("4. Delete a record")
#     print("5. Exit")

#     option = input("Enter option: ")
#     return option


# def main_loop():
#     while True:
#         option = show_menu()
#         if option == "1":
#             print("You have selected option 1")
#         elif option == "2":
#             print("You have selected option 2")
#         elif option == "3":
#             print("You have selected option 3")
#         elif option == "4":
#             print("You have selected option 4")
#         elif option == "5":
#             conn.close()
#             break
#         else:
#             print("Invalid option")
#         print("")
        
        
# conn = mongo_connect(MONGODB_URI)  

# coll = conn[DBS_NAME][COLLECTION_NAME]

# main_loop()
    
    
    
    
    

    
   
    