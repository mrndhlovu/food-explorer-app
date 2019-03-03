#  Flask Receipe App
import os
#import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DNAME"] = 'cuisineAppDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-j5cta.mongodb.net/cuisineAppDB?retryWrites=true'

mongo = PyMongo(app)


 
@app.route('/')
@app.route('/get_cuisine')
def get_cuisine():
    return render_template("cuisine.html", recipes=mongo.db.userRecipes.find())

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
    
    
    
    
    

    
   
    