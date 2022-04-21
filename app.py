import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_categories")
def get_categories():
    """
    This is function for to get all categories from MongoDB
    """
    categories = list(mongo.db.categories.find())
    recipes = list(mongo.db.recipes.find())
    cuisines = list(mongo.db.cuisine.find())

    return render_template(
        "categories.html", 
        categories=categories, 
        recipes=recipes,
        cuisines=cuisines)
        

@app.route("/search", methods=["GET", "POST"])
def search():
    """
    This function for search recipes"
    """
    query = request.form.get("query")
    categories = list(mongo.db.categories.find())
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    cuisines = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    return render_template(
        "categories.html",
        categories=categories,
        recipes=recipes,
        cuisines=cuisines)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    This function for user to register on
    website and they could use more options
    such as add recipie, delete, edit
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exist, please try something else")
            return redirect(url_for("signup"))

        pwhash = generate_password_hash(request.form.get("password"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": pwhash,
            "password_reconfirm": check_password_hash(pwhash, request.form.get(
                "password_reconfirm"))
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower(),
        flash("You have successfully signed up")
        return redirect(url_for("get_categories"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome " + session["user"].format(request.form.get("username")))
                return redirect(
                    url_for("my_recipes", username=session["user"]))
            else:
                # invaild password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect("login")
    return render_template("login.html")


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    """
    This function for user's username from db
    """
    username = session["user"]
    if username == session["user"]:
        recipes = list(mongo.db.recipes.find(
            {"created_by": session["user"]}))
    else:
        flash("You were not supposed to be here!")
        return redirect(url_for("get_categories"))
    return render_template(
            "my_recipes.html",       
            username=username,   
            recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    It displays full recipe
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = recipe['category_name']
    cuisines = recipe['cuisine_name']
    allergens = recipe['allergens']

    return render_template(
        "recipe.html",
        recipe=recipe, 
        categories=categories, 
        cuisine=cuisines, 
        allergens=allergens)
    

@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect("login")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Adding new recipe function
    """
    if not session.get("user"):
        flash("You must be logged in to create new recipe")
        return redirect("login")

    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "created_by": session["user"],
            "cuisine_name": request.form.get("cuisine_name"),
            "image_url": request.form.get("image_url"),
            "allergens": request.form.getlist("allergen"),
            "ingredients": request.form.getlist("ingredients"),
            "instructions": request.form.getlist("instructions")
        }
        
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe succesfully created!")
        return redirect(url_for("get_categories"))
    recipes = mongo.db.recipes.find().sort("recipe_name")
    categories = mongo.db.categories.find().sort("category_name")
    cuisines = mongo.db.cuisine.find().sort("cuisine_name", 1)
    allergens = mongo.db.allergen.find().sort("allergen_name", 1)

    return render_template(
        "add_recipes.html", 
        recipes=recipes,
        categories=categories,
        cuisines=cuisines, 
        allergens=allergens)


@app.route("/edit_recipes/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    This function for user editing own recipes
    """
    if "user" in session:
        user = session["user"]
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        if recipe["created_by"] == user:
            if request.method == "POST":
                update = {'$set': { 
                    "recipe_name": request.form.get("recipe_name"),
                    "category_name": request.form.get("category_name"),
                    "created_by": session["user"],
                    "cuisine_name": request.form.get("cuisine_name"),
                    "image_url": request.form.get("image_url"),
                    "allergens": request.form.getlist("allergens"),
                    "ingredients": request.form.getlist("ingredients"),
                    "instructions": request.form.getlist("instructions")
                }}
                mongo.db.recipes.update_one(
                    {"_id": ObjectId(recipe_id)}, update)
                flash("Recipe Updated Succesfully")
                return redirect(url_for("get_categories"))

        else:
            flash("You need to login first for editing")
            return redirect(url_for("login.html"))

        categories = mongo.db.categories.find().sort("category_name")
        cuisines = mongo.db.cuisine.find().sort("cuisine_name", 1)
        allergens = list(mongo.db.allergen.find().sort("allergen_name", 1))
        ingredients = list(mongo.db.recipe.find().sort("ingredients"))
        instructions = list(mongo.db.recipe.find().sort("instructions"))

        return render_template(
            "edit_recipe.html",
            recipe=recipe,
            categories=categories,
            cuisines=cuisines, 
            allergens=allergens,
            ingredients=ingredients,
            instructions=instructions)
        

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    This function for remove recipe from database
    """
    if "user" in session:
        user = session["user"]
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        if recipe["created_by"] == user:
            mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
            flash("Recipe Succesfully Removed")
            return redirect(url_for("get_categories"))
        else:
            flash("This not the recipe you created")
            return redirect(url_for("categories.html"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)