# The Green Recipes

## Backend Development Milestone Project 

ADD PICTURE

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

[UX](#ux)

## Website owner business goals

This page presents all the recipe details to its owner. The owner can update, edit, delte  any recipe details and resubmit the recipe. The data is passed from the form to python. The page and its functionality were created using the Materilaze, Framework, JQuery, Python and The Flasks, Heroku, MongoDB.

## User stories/User goals

### Professional

Whoever has a passion for the art of fine cuisine will be a user who is interested in cooking and baking as a serious hobby or as a profession. They will expect specific content for example, lists of ingredients, cooking instructions, and allergens. They will expect to be able to browse recipes or search for specific content. They will want content presented in a logical order, that will be easy to follow. They will register to be able to add/edit their recipes .


### Hobbiest

A hobbyist will visit the site to investigate a possible new recipe source. They will register to be able to add, edit their own recipes, and look at others recipes. They will be interested in interacting with the application. 


### Casuals

A casual user will visit the site out of interest. They may browse a few recipes, search for some recipes based on a specific ingredient they might be using at the time. They may not register on the site to be able to add/edit recipes. The may visit the recipes page and casually browse the content.


## Structure of the website

The Green Recipe  is designed to be simple and user-friendly on all types of devices. On desktop, tablet, or mobile device there should be no difference for a user to have a great experience. All parts are designed to concentrate maximum user satisfaction. Users will get some interaction from the interface as links and buttons will have a hover effect. User will be able to add, remove, edit recipes.

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

* In this section user can see all recipes with indvidual profiles; there's information about recipe category, created by, recipe name and cuisine information. On the bottom view section, when user click to view section they will see full recipe. If user logged in and they have a own recipes on this section they will see edit/delete button side of view button.


## Log in

* If user already signed in before, they can login with username and password. Username is more than five character, and pasword as well. If the user first time coming to our website, there's a link on the bottom "New here? Sign Up! 

## Sign up

* This section provides to user sign up information. If user first time in our webpage and they woudl like to add their own recipes and edit/remove they need sign up. 

## My Recipes

* When user loged in the page direct them to the my recipe page. My recipe page collecting users own recipes. They will see edit/delete button side of view button, with view button they can see all recipe and also they can edit or remove their own recipes.


## Add recipe

* After user logged in, they will see add recipe option on nav bar. From add recipe page user will be able add new recipe. Ther's a recipe name all recipes need name, image all recipes need image adress if you dont have just leave blank, allergens section keeping in diffrent allergens, such as nuts, fish, milk, ingredinets section user can add ingredinets and quantity, instructions section is methods for cooking.

## Log out

* In this section user can log out anytime, when you log out the page will you direct to all recipes page automatically.

[Back to Table of contents](#table-of-contents)