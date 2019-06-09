## Foods Explorers
___



This website main purpose is targeted at people who are foodies and would like to explore food options in the world. On this site website users can view recipes shared by other people and can also share recipes with other people. Users can like or dislike or add favorite recipes. Users have to register for an account to gain access to some features within the website, for example favourite a recipe, sharina a recipe or voting for a recipe. The website uses both frontend and backend technologies like  bootstrap, Semantic UI, flask and MongoDB. 


### Website Files and Features
---

static folder holds the following files:
```
1. index.html
2. register.html
3. base.html
4. cuisine.html
5. recipedetail.html
6. editrecipe.html
7. addrecipe.html
8. app.pymongo
9. Procfile
10. requirements.txt
11. js folder > index.js
12. images folder > (holds image files)
13. css folder > style.css
```

* base.html - This file is the main template for the website. It keeps head links, navigation bar, search box, recipe filter dropdown, side bar and script tags used through out the website. All pages the website content is rendered or graphed in the middle of this base template. 

* index.html - On this page a user can login into their account or click register for signup for a new one.
* register.html - From this page a user can register for new account.
* cuisine.html - this is the main landing page of the website, which list all recipes stored in the database. The page has features like:
`
. Displaying what shloud be the recipe image
. The author of the recipe
. Number of upvotes and downvotes
. Number of views
. Should a user be logged in and have a list of favourites on the database, that would be shown by a heart icon on the top left of the recipe image.

* recipedetail.html - this is where a user can see more detail about a recipe they click on the cuisine.html page. This page is only seen by a logged in user, other wise they are prompted to login or register first. From this page if a logged in user is the owner of the recipe being viewed, then the edit, delete and add recipe buttons are shown below, otherwise they do not render.
* editrecipe -  this page is only seen by a logged-in user where they can edit only a recipe they uploaded. The form fields are pre-populated with data from the backend and can be delete by the 'x' buttons or can add new infomation by clicking the plus icon on the left of each segment. When editing is done, data can be sent back to the database with the new updates by clicking the 'Done' button. The user has also the option to only delete a recipe they uploaded by clicking the 'Delete' button.
* addrecipe.html - on this page a user logged in user can create and share a new recipe. New feilds can be rendered or removed to fit the user's options. By click the red 'plus' button they can add a new field and the 'x' to delete field.
* app.py:  this file handles all the backend functinality of the website which includes user login,user logout, database queries, database schema setup,deleting or creating a recipe.
* Procfile 
* requirements : 
* js folder -  stores index.js file which keeps all the fronted functionalty of the site.
* images folder stores images used by recipes.
* css folder stores the style.css file which keeps handles some of the styling of the website.

### Technologies Used
___
 1. MongoDB: for handling database storing of all the recipe and users data.
 2. Javascript: for frontend functionality of the website.
 3. Bootstrap: for handling the grid layout on the website.
 4. Semantic UI: a frontend framework like bootstrap but with more advanced build tools mostly used on this website. tools like dropdown menus, 
 5. Python version 3.4.3
 6. Pip: packet manager for Python
 6. Flask: Python framework
 7. CSS
 8. JQuery
 9. Cloud9: Intergrated Development Environment
 10. 
 


 






