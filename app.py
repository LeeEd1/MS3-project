import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe_details(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_details.html", recipe=recipe)


# Route for Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        # Check if passwords match
        if password != confirm:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        # Checks if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Checks if email exists
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if existing_email:
            flash("Email already in use")
            return redirect(url_for("register"))

        # Register user
        register = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "date_joined": datetime.now()
        }
        mongo.db.users.insert_one(register)

        # Logs in user after registration and puts user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for("account", username=session["user"]))
    return render_template("register.html")


# Route for user Log In
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check if password match
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for("account", username=session["user"]))
            else:
                flash("Incorrect Email/Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Email/Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Route for Delete user
@app.route("/delete_user/<user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    if request.method == "POST":
        mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        flash("We are sorry you're leaving us. Please feel free to rejoin at any time!")
        session.pop("user")
        return redirect(url_for("home"))

    return redirect(url_for("home"))


# Route for user's account page
@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    user = mongo.db.users.find_one({"username": username})

    if user:
        first_name = user.get("first_name")
        last_name = user.get("last_name")
        date_joined = user.get("date_joined").strftime("%Y-%m-%d")

        return render_template("account.html", first_name=first_name, last_name=last_name,
         username=username, date_joined=date_joined, user=user)

    return render_template("account.html", username=username)


# Route for user Log Out
@app.route("/logout")
def logout():
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Route for add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "tags": request.form.get("tags"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "photo_url": request.form.get("photo_url"),
            "author_id": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe successfully added")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html")


# Route for edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        update_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "tags": request.form.get("tags"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "photo_url": request.form.get("photo_url"),
            "author_id": session["user"]
        }
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": update_recipe})
        flash("Your recipe has been updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    return render_template("edit_recipe.html", recipe=recipe)


# Route for delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Your recipe has been deleted")
    return redirect(url_for("get_recipes"))


# Runs flask app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)