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
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


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
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Logs in user after registration and puts user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successfull")
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


# Route for user's account page
@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("account.html", username=username)

    return render_template("account.html", username=username)


# Route for user Log Out
@app.route("/logout")
def logout():
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Runs flask app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)