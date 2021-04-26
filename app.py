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
@app.route("/dictionary")
def dictionary():
    words = mongo.db.words.find().sort("word", 1)
    return render_template("dictionary.html", words=words)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists. Please select a different username.")
            return redirect(url_for("register"))

        register = {
            "user_name": request.form.get("username").lower(),
            "user_password": generate_password_hash(request.form.get("regpassword")),
            "user_type": "user"
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie

        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull")
        return redirect(url_for("dictionary", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_user = mongo.db.users.find_one(
            {"user_name": request.form.get("username").lower()})

        if login_user:
            if check_password_hash(login_user["user_password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get("username")))
                return redirect("dictionary")
            else:
                # if the password does not match
                flash("Username and/or password are not correct")
                return redirect(url_for("login"))

        else:
            flash("Username and/or password are not correct")
            return redirect(url_for("login"))
        
    return render_template("login.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        debug=True,
        port = int(os.environ.get("PORT"))
    )