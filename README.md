# The Green Recipes

## Backend Development Milestone Project 

![iamresponsive](../myrecepie.ka3/static/md_images/mockup.png)

### Website presents Green Recipes as a online cookbook. Users will be able to find, add, delete, edit recipes content in easy and simple way.

This project is for educational purposes and can not be used as a template for a business use. 

This application uses Python on the back-end with the Flask web framework, and uses MongoDB for the database. It also uses the Materialize framework on the front-end such as HTML, CSS, JavaScript.


To open live project click [here](https://flask-myrecipes-ka.herokuapp.com/)<br>


# Table of Contents

- [UX](#ux)
   - [Website owner business goals](#Website-owner-business-goals)
   - [User stories/User goals](#User-goals)
       - [Professionals](#Pofessional-user-stories-goals)
       - [Hobbiest](#Returning-user-sotries-goals)
       - [Casuals](#Casual-user-stories-goals)
  
   - [Structure of the website](#Structure-of-the-website)
   - [Wireframes](#Wireframes)
   - [Surface](#Surface)
       - [Colors](#Colors)
       - [Fonts](#Fonts)
       - [Images](#Images)
-  [Fetures](#Fetures)
-  [Technologies](#Technologies)
-  [Testing](#Testing)
   - [Functional testing](#Functional-testing)
   - [Compatibility testing](#compatibility-testing)
   - [Code Validation](#code-validation)
   - [User stories testing](#user-stories-testing)
   - [Issues found during site development](#issues-found-during-site-development)
   - [Performance testing](#performance-testing)
-  [Deployment](#deployment)
- [Credits](#Credits)
- [Screenhots](#Screenhots)

# UX

## Website owner business goals

This page presents all the recipe details to its owner. The owner can update, edit, delte  any recipe details and resubmit the recipe. 
The data is passed from the form to python. The page and its functionality were created using the Materilaze, Framework, JQuery, 
Python and The Flasks, Heroku, MongoDB.

## User stories/User goals

### Professional

Whoever has a passion for the art of fine cuisine will be a user who is interested in cooking and baking as a serious hobby or as a 
profession. They will expect specific content for example, lists of ingredients, cooking instructions, and allergens. They will expect 
to be able to browse recipes or search for specific content. They will want content presented in a logical order, that will be easy to 
follow. They will register to be able to add/edit their recipes .


### Hobbiest

A hobbyist will visit the site to investigate a possible new recipe source. They will register to be able to add, edit their own recipes, 
and look at others recipes. They will be interested in interacting with the application. 


### Casuals

A casual user will visit the site out of interest. They may browse a few recipes, search for some recipes based on a specific ingredient 
they might be using at the time. They may not register on the site to be able to add/edit recipes. The may visit the recipes page and casually 
browse the content.


## Structure of the website

The Green Recipe  is designed to be simple and user-friendly on all types of devices. On desktop, tablet, or mobile device there should be no 
difference for a user to have a great experience. All parts are designed to concentrate maximum user satisfaction. Users will get some interaction 
from the interface as links and buttons will have a hover effect. User will be able to add, remove, edit recipes.

## Wireframes

I used this website Balsamiq to create  wireframes.

![Wireframes](/static/md_images/wireframes/wireframes.png)

# Surface

### Colors

Main colours used in a project:
* background color: #81c784, #a5d6a7, #c8e6c9
* font color: rgb(59, 58, 58);rgb(0, 0, 0);
* other colors: whitesmoke, rgb(217, 211, 211, 0.5)

### Fonts
* I used below fontts for my project:
    - Roboto,Oxygen-Sans
    - Ubuntu,Cantarell
    - Helvetica,sans-serif;
* The reason why I chose these fonts is that my page is more tidy and does not tire the eyes while looking at my page. 

### Images
* I used images from [Pixel.com](https://www.pexels.com/)) and there are credited in [credits](#credits) section.

[Back to Table of contents](#table-of-contents)

# Fetures

The website consists of 6 pages. Six are accessible from a navigation menu.

The website has below features:

## Navigation bar

* #### Navigation bar is visible on the top of each website. It is responsive and will adapt to mobile devices by a change into a burger menu.

* Navigation scheme:

 * On left side there is a logo. It can be used as navigation link to the main page.
 * On right side there are four links or nav menu. It contains:
   * All Recipes
   * My recipes
   * Add Recipe
   * Log in
   * Log out
   * Sign in

## Add Recipes

* Users can add own recipes here. Also they can edit, remove their own recipes. 

## Footer

* Footer is consistent on all pages. It has contact details, copyright,  and social links, and my github page. Each link will open in a separate tab in a browser.

## All Recipes

* In this section user can see all recipes with indvidual profiles; there's information about recipe category, created by, recipe name and cuisine information. 
On the bottom view section, when user click to view section they will see full recipe. If user logged in and they have a own recipes on this section they will 
see edit/delete button side of view button.


## Log in

* If user already signed in before, they can login with username and password. Username is more than five character, and pasword as well. If the user first time 
coming to our website, there's a link on the bottom "New here? Sign Up! 

## Sign up

* This section provides to user sign up information. If user first time in our webpage and they woudl like to add their own recipes and edit/remove they need sign 
up. 

## My Recipes

* When user loged in the page direct them to the my recipe page. My recipe page collecting users own recipes. They will see edit/delete button side of view button, 
with view button they can see all recipe and also they can edit or remove their own recipes.


## Add recipe

* After user logged in, they will see add recipe option on nav bar. From add recipe page user will be able add new recipe. Ther's a recipe name all recipes need 
name, image all recipes need image adress if you dont have just leave blank, allergens section keeping in diffrent allergens, such as nuts, fish, milk, ingredinets 
section user can add ingredinets and quantity, instructions section is methods for cooking.

## Log out

* In this section user can log out anytime, when you log out the page will you direct to all recipes page automatically.

[Back to Table of contents](#table-of-contents)

# Technologies

## Languages:

* HTML
* CSS
* javaScript
* JQuery
* Python

## Libraries:

* JQuery: for easier and faster javascript and DOM manipulation.
* Matrialize: used for creating a responsive design.
* Flask: used as Python web framwork.
* PyMongo: used as Python distribution containing tools for working with MongoDb.
* Flask-PyMongo: used as a bridge between Flask and PyMongo.
* Werkzeug: used for password hasing and authentication.
* Jinja: for displaying backend data on the screen.

## Other programs used:

* Balsamiq: for wireframing.
* Google Fonts: for the fonts used.
* Github
* Visual Studio Code: as a IDE (Integrated Development Environment) for developing the project
* Git: for version control
* Google Chrome Dev Tools: for testing purposes. Console logging checking for breakpoints.
* Prettier: to beautify code.
* FontAwesome: used for icons throughout the website FontAwesome
* Heroku to deploy the project

[Back to Table of contents](#table-of-contents)

# Testing 

## Functional testing

* I used the Google Chrome developer tools and Mozilla web developer tools to test and fix issues with responsiveness
and styling issues. In the style.css file, both tools made it extremely easy for me to use margin, padding, font, width, 
height and other elements correctly use on my web page.

## Compatibility testing

My website has been tested with multiple mobile devices and browsers. I've tested extention  devices in both Mozilla web 
developer tolls and Chrome developer tools. 
 
Also, I tested on hardware devices such as iPhone5 iPhone 7S, iPhone 11, iPhone 12, and Samsung Galaxy S10 and 
Galaxy S21.

## Issues found during site development

- Bugs 1

![bug1](../myrecepie.ka3/static/testing/bug-1-allergen%20isn't%20appear.png)


When we clicked on the edit page, the allergen part was not saved. 

* I had to change the name of the checkboxes to allergen, then I can get the list from that. Then I was working on the rendering. I added below section on my app.py file:
  -   recipe = mongo.db.recipes.find_one({"_id":     ObjectId(recipe_id)})
    categories = recipe['category_name']
    cuisines = recipe['cuisine_name']
    allergens = recipe['allergens']
* I render it, but I needed to loop over the allergens as it is just was printing it as a list or cursor object.
And updated Allergens: {% for allergen in recipe.allergens %} {{ allergen }} {% endfor %} jinja on the recipe page, and issue was solved.

Bugs 2

![Bug2](../myrecepie.ka3/static/testing/Bug2-ingredinets-isnt-save-when-edit.png)

* The instruction and ingredients sections on the edit page were not saved. When you click on the Edit button, these parts were reset automatically.
I make sure I am looping over the correct variables in my template to display them. I wasn't sure if the variables I am using in my template are correct. I tested  it by displaying the variable in a large heading to see if it contains any data. 
  - I was trying to loop over 'ingredinets', so I add
"h1 style="color:red;"> {{ ingredinets }}"
to see if that variable exists, which is it was. 
So it was displaying the instructions, I just added to put '{{ instruction }}' in value of the input in your loop, and issue sorted.

### Performance testing 

#### Desktop view 

![Desktop](../myrecepie.ka3/static/testing/performance-desktop.png)

#### Mobile view

![Mobile](../myrecepie.ka3/static/testing/performance-lighthouse.png)


## Code validation

* [W3C HTML validator](https://validator.w3.org/) to validate HTML code
* [W3C CSS validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
* [JavaScript validator ](https://jshint.com/) to validate JavaScript code
* [JShint](https://jshint.com/) to validate JavaScript code
* [Python Syntax Checker](https://extendsclass.com/python-tester.html) to verify syntax used.


[Back to Table of contents](#table-of-contents)

# Deployment:

The project was developed using Gitpod ass the IDE, committed to Git as a local repository, and pushed/stored in Github.
It was then deployed on Heroku since Github pages cannot deploy a Python app.

Deploying on Heroku:

- Using the Heroku Command Line Interface
- Connect to a github repository. (The easier method)

1. ## Set up a new Heroku App:

Navigate to Heroku.com, create a new account or login if you already have an account.   
* On the dashboard page, click "Create New App" button.   
* Give the app a name, the name must be unique with hypens between words. 
* Set the region closest to you, and click "Create App".  

2. ## Create a requirements.txt file:

Heroku needs to know on what dependencies the project runs on to run succesfully, this way Heroku knows what language we're using.
To create a requirements.txt file:
* In the terminal type: pip3 --local > requirements.txt
* git add requirements.txt
* git commit -m "Add requirements.txt"
* git push

3. ## Create a procfile:

This tells Heroku how to run our project:
* In terminal type: echo web: python run.py > Procfile (mind the capital P)
* git add, commit and push.

4. ## Connect our app to heroku:

* In Heroku app dashboard, navigate to deploy page, click on github.
* Click on connect to Github.
* Fill in the name of your repository and click on search.
* After the correct repository is found click on connect.

5. ## Set up environment Variables:

* The environment variables for this project are hidden in a env.py file and ignored when pushing to github.
* You need to manually tell Heroku what these variables are.
* GO back to the dashboard and navigate to the settings page.
* Click on reveal config vars and add the environment variables in key-value pairs:"
 IP | 0.0.0.0

  PORT | 5000

  SECRET_KEY | `<Your secret_key>`

  MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority`

  MONGO_DBNAME | `<database_name>`

6.  ## Enable automatic deployment:

* On "Automatic Deploys" section, from our master/main branch click on "Enable Automatic Deployment".
* On "Manual deploy" section, from our master/main click on "Deploy Branch".
* Heroku will now receive the code from Github and start building the app using our required packages. Once it's done, you'll see a notification "Your app was successfully deployed."  The deployed version can now be viewed by selecting View App.

## To use this project follow the following steps:

1. Create a database on MongoDb

* Login
* Create a cluster by choosing the Shared Cluster.
 - Select a cloud provider and select the region closest to you.
* Select a cluster tier, choose the M0 Tier (Free forever).
* Click on cluster name and choose whatever name you like.
* Click Create Cluster. This cluster name will be used in your MONGO_URI environment variable.
* Navigate to Database Access under the Security section on the left, in order to create our database user credentials.
* Click on "Add New Database User", create a username and password.
* Set the "Database User Privileges" to Read and Write to any database, and click "Add User".
* Click on "Network Access" within the Security menu in order to whitelist our IP address and make sure that it has access to our database. Click "Add IP Address", select "Allow Access from Anywhere", click "Confirm".

2. Create database:

* From the cluster page click on collections button.
* Click on Create Database, provide the database name and one initial collection name. 
  - This name will be used in your MONGO_URI and MONGO_DBNAME environment variables.
* Create more collections by clicking the Create Collection button.
* To manually create a document, click on the Collection followed by Insert Document.

3. Fork or Clone THe Github Repository:

## Forking:

* Log in to GitHub.  
* Navigate to the main page of the GitHub Repository that you want to fork.  
* At the top right of the Repository just below your profile picture, locate the "Fork" Button.  
* You should now have a copy of the original repository in your GitHub account.  
* Changes made to the forked repository can be merged with the original repository via a pull request. 

## Cloning:

* Go to repository.
* Click on the button "code".
* Select the "HTTPS" option.
* Copy the URL presented.
* Open your Terminal.
* Create a directory for storing this repository.
* Type "git clone" and paste the URL in that you previously copied.
* Press enter to create local clone repository.

4. Set local environment variables and install dependancies:

* Create a .gitignore file and add env.py to it
* Create an env.py file to hold your sensitive information.
* Within the env.py file:
    - import os
    - os.environ.setdefault("IP", "0.0.0.0")
    - os.environ.setdefault("PORT", "5000")
    - os.environ.setdefault("SECRET_KEY", <your_secret_key")
    - os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority")
    - os.environ.setdefault("MONGO_DBNAME", "<database_name")
* Install all dependencies listed from the requirements.txt file.
  - Type in terminal: pip3 install -r requirements.txt  

5. Go to deployment on heroku and fill in your variables, you no longer need to create a requirements.txt file and Procfile.

6.  Deploying your app to heroku

* Login to heroku and enter your details.
    - command: heroku login -i

* 2. Get your app name from heroku.
    - command: heroku apps

* 3. Set the heroku remote. (Replace <app_name> with your actual app name)
    - command: ﻿heroku git:remote -a <app_name>

* 4. Add, commit and push to github
    - command: git add . && git commit -m "Deploy to Heroku via CLI"

5. Push to both github and heroku
    - command: git push origin main
    - command: git push heroku main


# Credits

## Code

1. The code in this project mainly comes from Code Institute's Task Manager project and used as a main reference while creating this project
in setting up a database to writing Python with Flask and the Jinja Template language.

2. General content [BBC Food](https://www.bbc.co.uk/food/diets/vegan)

3. I created my own css file and used some Materialize file.

### Media

#### Image

##### [Pixel.com](https://www.pexels.com/)

* [Background image](https://www.pexels.com/photo/green-and-purple-kale-in-white-surface-5755640/)

# Screenhots

- Home Page

![Home page](../myrecepie.ka3/static/md_images/screenshots/A.png)

- Log in Page

![Log In](../myrecepie.ka3/static/md_images/screenshots/B.png)

- Add Recipe

![Add Recipe](../myrecepie.ka3/static/md_images/screenshots/C.png)

- Sign Up

![Sign up](../myrecepie.ka3/static/md_images/screenshots/D.png)

- Home page (mobile view)

![Mobile home](../myrecepie.ka3/static/md_images/screenshots/E.png)

- Log In (mobile)

![Login-mobile](../myrecepie.ka3/static/md_images/screenshots/F.png)




[Back to Table of contents](#table-of-contents)

