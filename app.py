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


# Route for home
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Route for get_recipes
@app.route("/get_recipes")
def get_recipes():
    # Gets queries
    filter_category = request.args.get('category_name')

    # Queries database and retrieves recipes that match query
    if filter_category:
        recipes = mongo.db.recipes.find({"category_name": filter_category})
    else:
        # retrieve all recipes if no filter specified
        recipes = mongo.db.recipes.find()

    # Fetch categories
    categories = mongo.db.categories.find()

    return render_template(
        "recipes.html",
        recipes=recipes,
        categories=categories)


# Route for recipe_details
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
            "fav_cuisine": request.form.get("fav_cuisine"),
            "password": generate_password_hash(request.form.get("password")),
            "date_joined": datetime.now(),
            "is_admin": False
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
            {"email": request.form.get("email")}
        )

        if existing_user:
            # Check if password match
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = existing_user["username"]
                flash("Welcome, {}".format(existing_user["username"]))
                return redirect(url_for(
                    "account", username=session["user"]
                ))
            else:
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Route for Delete user
@app.route("/delete_user/<user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    if request.method == "POST":
        mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        flash("We are sorry you're leaving us. "
              "Please feel free to rejoin at any time!")
        session.pop("user")
        return redirect(url_for("home"))

    return redirect(url_for("home"))


# Route for user's account page
@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # Check if user is logged in
    if "user" not in session:
        flash("Please log in to see this page")
        return redirect(url_for("login"))

    # Check if user has permission to view page
    if session["user"] != username:
        flash("You do not have permission to view this page.")
        return redirect(url_for("home"))

    user = mongo.db.users.find_one({"username": username})
    # Checks if user has account
    if user is None:
        flash("Sorry your account could not be found!")
        return redirect(url_for("home"))

    return render_template("account.html", user=user)


# Route for edit account
@app.route("/edit_account/<user_id>", methods=["GET", "POST"])
def edit_account(user_id):
    if request.method == "POST":
        # Retrieves submitted form data
        new_email = request.form.get("email")
        new_username = request.form.get("username").lower()

        # Checks if new email is already in use by another user
        existing_email = mongo.db.users.find_one(
            {"email": new_email.lower(), "_id": {"$ne": ObjectId(user_id)}})
        if existing_email:
            flash("Email already in use")
            return redirect(url_for("edit_account", user_id=user_id))

        # Checks if new username is already in use by another user
        existing_username = mongo.db.users.find_one(
            {"username": new_username.lower(),
             "_id": {"$ne": ObjectId(user_id)}})
        if existing_username:
            flash("Username already in use")
            return redirect(url_for("edit_account", user_id=user_id))
        # Updates account if email and username are not in use
        update_account = {
            "email": request.form.get("email"),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "username": request.form.get("username").lower(),
            "fav_cuisine": request.form.get("fav_cuisine"),
        }
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)}, {"$set": update_account})
        flash("Your details have been updated successfully")
        return redirect(url_for("account", username=session["user"]))

    # Gets the user by id and renders edit_account page
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_account.html", user=user, user_id=user_id)


# Route for user Log Out
@app.route("/logout")
def logout():
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Route for add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Checks if the user is in session
    if "user" not in session:
        flash("Please log in or register to see this page")
        return redirect(url_for("login"))

    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "cuisine": request.form.get("cuisine"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "photo_url": request.form.get("photo_url"),
            "author_id": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe successfully added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find()
    return render_template("add_recipe.html", categories=categories)


# Route for edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # Checks if the user is in session
    if "user" not in session:
        flash("Please log in or register to see this page")
        return redirect(url_for("login"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # Checks if recipe exist and if author match or admin
    if recipe is None or recipe.get(
        'author_id') != session["user"] and session["user"] != "admin":
        flash("You are not authorized to access this recipe")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find()

    # Checks if form is submitted and updates the recipe with new data
    if request.method == "POST":
        update_recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "cuisine": request.form.get("cuisine"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "photo_url": request.form.get("photo_url"),
            "author_id": session["user"]
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {"$set": update_recipe})
        flash("Your recipe has been updated")
        return redirect(url_for("get_recipes"))

    return render_template("edit_recipe.html",
     recipe=recipe, categories=categories)


# Route for delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Checks if user is in session
    if "user" not in session:
        flash("Please log in or register to see this page")
        return redirect(url_for("login"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # Checks if recipe exist and if author match or admin
    if recipe is None or recipe.get(
        'author_id') != session["user"] and session["user"] != "admin":
        flash("You are not authorized to access this recipe")
        return redirect(url_for("get_recipes"))

    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Your recipe has been deleted")
    return redirect(url_for("get_recipes"))


# Route for admin page to add remove categories
@app.route("/get_categories")
def get_categories():
    # Checks if user in session
    if "user" not in session:
        flash("Please log in to access this page")
        return redirect(url_for("login"))
    # Checks if user  is admin
    if session.get("user") != "admin":
        flash("You do not have permission to view this page.")
        return redirect(url_for("home"))

    categories = list(mongo.db.categories.find())
    return render_template("categories.html", categories=categories)


# Route for Add Category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # Checks if user in session
    if "user" not in session:
        flash("Please log in to access this page")
        return redirect(url_for("login"))
    # Checks if user is admin
    if session.get("user") != "admin":
        flash("You do not have permission to view this page.")
        return redirect(url_for("home"))

    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("Category successfully Added!")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Route for Edit Category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # Check if user is in session
    if "user" not in session:
        flash("Please log in to access this page")
        return redirect(url_for("login"))
    # Check if user is admin
    if session.get("user") != "admin":
        flash("You do not have permission to view this page.")
        return redirect(url_for("home"))

    if request.method == "POST":
        update_category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one(
            {"_id": ObjectId(category_id)}, {"$set": update_category})
        flash("Category Successfully Updated!")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Route for Delete Category
@app.route("/delete_category/<category_id>", methods=["POST"])
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted!")
    return redirect(url_for("get_categories"))


# User error handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


# Runs flask app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
