 [Food explorers](https://tools.hubteam.com/getting-started-tasks/)
===

This website is mainly targeted at foodies who would like to explore food options from around the world. On this website users can view recipes shared by other people and can also signup and upload recipes they want to share. Users can like, dislike or save a recipe to favorites. Users have to sign up for an account to gain access to some features within the website, for example saving a recipe, sharing a recipe and voting for a recipe. The website uses both front-end and backend technologies, it is driven by MongoDB database structures and presentation is handled by Bootstrap, Semantic UI, and JavaScript. 


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
14. wireframes > mockup images
```

UX and Features
===
#### base.html
This is the main template used throughout the website. It renders the head links, navigation bar, search box, recipe filter dropdown, side bars and also the script tags used throughout the website. All website content is rendered in the middle of this base template.The recipe filter side bar is different on mobileview from desktop meaning the app will dictate a user's device and render the appropriate filter.
#### index.html
 On this page a user can login to their account or register a new one.
#### register.html
From this page a user can sign up for a new account. There is no form validation or password encryption.
#### cuisine.html
this is the landing page of the website, which list all recipes stored in the database. As a user you can:

* click an image and be redirected to a page with more detailed information about a recipe.
* see author of the recipe
* see the number of upvotes and downvotes
* see number of views for each recipe.
* see date a recipe was uploaded.
* see a favourites section on the sidebar if logged in.
 If a recipe is in the favourites list, the recipe image will have a heart icon on the top left corner. If the icon is clicked, the recipe would be removed from user's favourites list. 
#### recipedetail.html
this is where a user can see a recipe in detail. From this page if a user is logged in and the owner of the recipe, then the edit, delete and addrecipe buttons are rendered at the bottom of the page, otherwise they are hidden. A recipe summary is also shown to give an overview of a dish.
#### editrecipe 
this page is only seen by a logged-in user where they can edit only a recipe they uploaded. The form fields are pre-populated with data from the backend and can be deleted by clicking on the 'x' icon or can add new recipe information by clicking the plus icon. When editing is done, data can be sent back to the database with the new updates by clicking the 'Done' button. The user also has the option to delete a recipe they uploaded by clicking the 'x' button.
#### addrecipe.html
on this page a user logged in will create and share a new recipe. New fields can be rendered or removed to fit the user's demands. By clicking the 'plus' button they can add a new field and the 'x' to delete the field. 'Add Recipe' button sends data for storage on the database.
#### app.py  
this file handles all the backend functionality of the website which includes user login information, handles CRUD queries, sets up the database structure which the website is dependent on.
#### Procfile
Instruction file for heroku on how to run the app.
####  requirements 
this file lists the dependencies required by python for the app to run.
#### js folder
stores index.js file which handles some of the front-end functionality of the site like creating or deleting form fields, bootstrap and semantic ui functions.
#### images folder 
stores placeholder images used by each recipe.
#### css folder 
stores the style.css file which handles some of the styling of the website.

### Other features
* Most Recent sidebar: This renders 5  clickable and most recent recipes uploaded on the website.

#### Wireframes 
Download the wireframe.xml file from the wireframes folder and then:

*  use [draw.io](https://draw.io) to view the wireframe file. 

### Hand draw mockups
___
![](/wireframes/imageone.png)
![](/wireframes/imagetwo.png)
![](/wireframes/imagethree.png)
![](/wireframes/imagefour.png)


MongoDB database collections structures used: 
===

###### Recipes collection

```
_id:5d001f65bb6aae000b028d4c
uploaded_by:"Soup Loving Morah"
record:Object
    title:"Mushroom, Broccoli, and Cheese Stuffed Chicken"
    category:"Lunch"
    country:"England"
    ingredients:Array
       0:"2 cups finely chopped broccoli florets"
       1:"2 tablespoons water"
       2:"½ cup shredded pepper jack cheese"
       3:"¼ cup mayonnaise"
       4:"4 smalls button mushrooms, sliced"
       5:"1 teaspoon garlic powder"
       6:"4 largest chicken breasts"
       7:"1 teaspoon paprika"
       8:"salt and ground black pepper to taste"
    directions:Array
       0:"Preheat the oven to 400 degrees F (200 degrees C). Line a baking sheet..."
       1:"Combine broccoli and water in a microwave-safe bowl. Cook in the micro..."
       2:"Combine cooked broccoli, pepper jack cheese, mayonnaise, mushrooms, and..."
       3:"Season both sides of each chicken breast with paprika, salt, and pepper..."
       4:"Bake in the preheated oven until chicken is no longer pink in the cent..."
    allergens:Array
       0:"paprika"
       1:"garlic"
       2:"mushrooms"
up_votes:0
down_votes:0
views:4
date_updated:"2019-06-11"

```
###### Categories collection
```
id:5c7dc3511c9d440000d43848
category_name:"Lunch"
````
###### Users collection
```
id:5cf3015b1c9d4400004b9a6d
email:"mtk@gmail.com"
is_active:true
passcode:"123"
username:"Mtk"
userFavourites:Array
     0:Object
     id:"5cea64caaede91707ac113f1"
     name:"Easy Shrimp Fra Diavolo"
     1:Object
     name:"Easy Shrimp Fra Diavolo"
     id:"5cea64caaede91707ac113f1"
     2:Object
     id:"5ce8f1e11c9d4400007f2154"
     name:"Korean Burger"
userLikes:Array
     0:"5cea64caaede91707ac113f1"
     1:"5cea64caaede91707ac113f1"

```



Technologies Used
===

 1. MongoDB: the storing and retrieving all the recipes and user data.
 2. Javascript: for frontend functionality of the website.
 3. Bootstrap: for handling the some parts of grid layout on the website as the resposive nature of the navigation bar.
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
13. Google chrome development tools.
14. Draw.io: for wireframes
15. Heroku: Hosting the App


### Testing
 Tested the website mainly using Google dev tools. This made it easy to edit the site structure on the website on the fly and then transferring the css code over to the style.css file. 
. For mobile responsive testing I used the toggle device tool option, which is part of google dev tools. From here I tested the website view in all device option available, which range from small screen like Galaxy S5 to large screens like Ipad Pro and even desktop view.

While trying to handle the responsive design of the website, I forgot to add this file: 

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

It gives the browser instructions on how to handle page dimensions and scale accordingly.

Had issues with some semantic ui components like accordions and dropdowns, as they do not work in mobile view. which resulted in having a different views of the recipe filter in mobile and desktopview.

##### Other browsers used for testing

* Firefox
* Microsoft Edge


Bugs and other issues
===

1. The website uses the same image for all recipes which can be improved to having the ability to upload a unique image for each recipe.
2. One image is also used as a user avatar. Can be improved by adding a unique image as the user signs up.
3. As a user logs in, a localstorage file if created to track user likes and and change the like button when clicked, however there is an issue with keeping the color state of the button when page reloads.
4. User can upvote or downvote a recipe more than once.
5. No form validation
6. Search functionality can be improved.
7. No Unit Test.
8. No pagination
9. Had to update Procfile with 
```
web: gunicorn app:app
```
With the help of my mentor 

Setup Process
* [Food explorers](https://tools.hubteam.com/getting-started-tasks/)
* Set up a blank Cloud9 workspace
* Already had a Free MongoDB account, I just setup the collections.
* Did not have to install Python as its part of the Cloud9 IDE.(Only had to change support version to Python Version 3)
* Created folders structure
* Installed Flask framework from the CLI
```
sudo pip3 install flask
```
* Created app.py file


Deployment
===

This website is deployed and hosted on Heroku. I created a free account and push my Cloud9 repo to Heroku so the website can be accessible by any one with an internet connection. The app code is also on Github pages, which where you are currently reading this file from.  

* Setup a free Heroku hosting account, then created an app with the app name 'food-explorers'
* Logged into heroku account from Cloud9 CLI using: 
```
heroku login
```
* Back in heroku under settings I setup 'Config Vars' 
```
IP = 0.0.0.0
PORT = 5000
```
* on Cloud9 I then linked my local repo to heroku app I created 
```
git remote add heroku https://git.heroku.com/food-explorers.git

```

* Created requirements.txt file by running
```
sudo pip3 freeze --local>requirements.txt
```
* added Procfile
```
echo web: python app.py > Procfile

``` 

* commited all staged files then pushed files from Cloud9 repo to heroku remote repository.
```
git push heroku master

```






Acknowledgments
===

* [CodeInstitute](https://codeinstitute.net/)
* [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)
* [W3Schools](https://www.w3schools.com/) -  simplified python examples.
* [Bootstrap](https://getbootstrap.com/)
* [Semantic UI](https://semantic-ui.com/)
* [Draw.io](draw.io)
* [Pexels](https://www.pexels.com/) - Royalty free images.
* [W3C CSS](https://jigsaw.w3.org/css-validator/validator) css code validator
* [Heroku](heroku.com)
