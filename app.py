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
@app.route("/get_index")
def home():
    """
    This is function for main page
    """
    return render_template("index.html")

@app.route("/get_categories")
def get_categories():
    """
    This is function for to get all categories from MongoDB
    """
    categories = mongo.db.categories.find()
    recipes = mongo.db.recipes.find()
    return render_template(
                            "categories.html", 
                            categories=categories, 
                            recipes=recipes)


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
            "password_reconfirm": check_password_hash(pwhash, request.form.get("password_reconfirm"))
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
                    flash("Welcome, {}".format(
                        request.form.get("usernme")))
                    return redirect(url_for(
                        "my_recipes", username=session["user"]))
            else:
                #invaild password match
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
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("my_recipes.html", username=username)
    
    return redirect(url_for("login"))



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
            "recipe_name" : request.form.get("recipe_name"),
            "category_name" : request.form.get("category_name"),
            "cuisine_name" : request.form.get("cuisine_name"),
            "image_url" : request.form.get("image_url") 
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe succesfully created!")
        return redirect(url_for("get_categories"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories = categories)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)