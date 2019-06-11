## Foods Explorers
___



This website main is targeted at foodies and who would like to explore food options from around the world. On this site website users can view recipes shared by other people and can also signup and upload recipes to share recipes. Users can like, dislike or save a recipe to favorites. Users have to sign up for an account to gain access to some features within the website, for example saving a recipe to favourites, sharing a recipe or liking a recipe. The website uses both front-end and back-end technologies like  bootstrap, Semantic UI, flask and MongoDB. 


### Website Files
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

###  UX and Features
* base.html - This is the main template used throughout the website. It renders the head links, navigation bar, search box, recipe filter dropdown, side bar and also the script tags used throughout the website. All website content is rendered or graphed in the middle of this base template. 
* index.html - On this page a user can sign into their account or click signup to register for a new one.
* register.html - From this page a user can sign up for a new account.
* cuisine.html - this is the landing page of the website, which list all recipes stored in the database. From this page users can:
`
.  See a placeholder image as every recipe on the database is rendered.When the image is clicked, they are redirected to a ‘recipedetail.html’ page.
. The author of the recipe
. Number of upvotes and downvotes
. Number of views
. Date the recipe was uploaded.
. Should a user be logged in  they can see favourites section on the sidebar .
. If they have any recipes save to favourites, whenever a recipe is the favourites list is rendered it will have a heart icon on the top left of the recipe image. If icon is clicked, the recipe would be removed from favourites.
* recipedetail.html - this is where a user can see a recipe in detail. From this page if a user is logged and is the owner of the recipe being viewed, then the edit, delete and add recipe buttons are shown below, otherwise they do not render.
* editrecipe -  this page is only seen by a logged-in user where they can edit only a recipe they uploaded. The form fields are pre-populated with data from the backend and can be deleted by clicking on the 'x' icon or can add new recipe information by clicking the plus icon. When editing is done, data can be sent back to the database with the new updates by clicking the 'Done' button. The user also has the option to delete a recipe they uploaded by clicking the 'Delete' button.
* addrecipe.html - on this page a user logged in will create and share a new recipe. New fields can be rendered or removed to fit the user's demands. By clicking the 'plus' button they can add a new field and the 'x' to delete the field. Save button sends data to storage on the database.
* app.py:  this file handles all the backend functionality of the website which includes user login information, handles database queries, sets up the schema on how data show be stored, deleting or creating a recipe.
* Procfile: Instruction file for heroku on how to run the app.
* requirements : this file lists the dependencies required by python for the app to run.
* js folder -  stores index.js file which keeps some of the front-end functionality of the site.
* images folder stores images used by recipes.
* css folder stores the style.css file which handles some of the styling of the website.

Database structure used 

```

Recipes collection

_id:5ce8a22e1c9d4400007f2152
record:Object
ingredients:Array
0:"1 onion, diced"
1:"1 pound cubed beef stew meat"
2:"1 1/2 teaspoons minced garlic"
3:"1/2 lime, juiced"
4:"1 jalapeno pepper, seeded and chopped"
title:"English Breakfast"
directions:"Heat olive oil in a large skillet over medium-high heat. Add the onion..."
allergens:Array
0:"chilli"
1:"nuts"
2:"beef"
category:"Breakfast"
country:"England"
date_updated:"2013-05-25"
views:349
up_votes:335
down_votes:12
uploaded_by:"Bean"


```
### Technologies Used
___
 1. MongoDB: the database keeping all the recipe and user data.
 2. Javascript: for frontend functionality of the website.
 3. Bootstrap: for handling the some parts of grid layout on the website.
 4. Semantic UI: a frontend framework like bootstrap but with more advanced build tools mostly used on the site for handling the majority of the layout and some css styling. 
 5. Python version 3.4.3
 6. Pip: packet manager for Python
 6. Flask: Python framework
 7. CSS: for styling parts of the website.
 8. JQuery.
 9. Cloud9: Integrated Development Environment
10. JavaScript
11. Heroku: App deployment.
12. Git: for version tracking of the app.
13. Google chrome development tools


### Testing
 Tested the website main using Google. This made it easy to edit the site structure on the website on the fly and then transferring the css code over to style.css file. 
. For mobile responsive testing i used the toggle device tool option, which is part of google dev tools. From here I tested the website view in all device option available, which range from small screen like Galaxy S5 to large screens like Ipad Pro and even desktop view.

Issues I had here however where that sometimes the site would not appear appear as expected, until the page is refreshed a couple of times. Could have been a Chrome caching issue but at times the cache was as little as 10MB. 





 








