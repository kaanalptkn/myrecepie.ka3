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
            {"username": request.form.get("usernme").lower()}
        )

        if existing_user:
            flash("Username already exist, please try something else")
            return render_template(url_for("signup"))

        register = {
            register ["username"]: request.form.get("username").lower(),
            register ["email"] : request.form.get("email").lower(),
            register ["password"] : generate_password_hash(request.form.get("password")),
            register ["password_reconfirm"]: check_password_hash(request.form.get("password_reconfirm"), register ["password"])
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower(),
        flash("You have successfully signed up")
        return redirect(url_for("get_categories"))

    return render_template("signup.html")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)