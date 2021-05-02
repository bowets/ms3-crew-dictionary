import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from datetime import datetime
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
    words = mongo.db.words.find().sort("word")
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
        return redirect(url_for("dashboard", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_user = mongo.db.users.find_one(
            {"user_name": request.form.get("username").lower()})

        if login_user:
            if check_password_hash(
                login_user["user_password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome {}".format(request.form.get("username")))
                    return redirect(url_for("dashboard", username=session["user"]))
            else:
                # if the password does not match
                flash("Username and/or password are not correct")
                return redirect(url_for("login"))

        else:
            flash("Username and/or password are not correct")
            return redirect(url_for("login"))
        
    return render_template("login.html")


@app.route("/dashboard/<username>", methods=["GET", "POST"])
def dashboard(username):
    #grab the session user and find user in database
    username = mongo.db.users.find_one(
        {"user_name": session["user"]})["user_name"]
    user_type = mongo.db.users.find_one({"user_name": session["user"]})["user_type"]
    words = mongo.db.words.find()

    return render_template("user_dashboard.html", username=username, words=list(words), user_type=user_type)


@app.route("/submit_word", methods=["GET", "POST"])
def submit_word():
    if request.method == "POST":
        existing_word = mongo.db.words.find_one({"word": request.form.get("word")})

        if not existing_word:
            word = {
                "word": request.form.get("word"),
                "word_category": request.form.get("word_category"),
                "word_definition": request.form.get("word_definition"),
                "word_sentence": request.form.get("word_sentence"),
                "word_submitted_by": session["user"],
                "word_approved_by": "",
                "word_status": "pending_approval",
                "word_submitted_datetime": datetime.now()
            }
            mongo.db.words.insert_one(word)
            flash("Word added successfully. Once reviewed by the editors, it will display in the dictionary")
            return redirect(url_for("dictionary"))
        else:
            flash("This word already exists, please submit a new word")
            return redirect(url_for("submit_word"))

    categories = mongo.db.category.find()
    return render_template("submit_word.html", categories = categories)


@app.route("/change_pwd", methods=["GET", "POST"])
def change_pwd():
    if request.method == "POST":
        old_pwd = mongo.db.users.find_one({"user_name": session["user"]})["user_password"]
        
        if check_password_hash(old_pwd, request.form.get("old_pwd")):
            mongo.db.users.update({"user_password": generate_password_hash(request.form.get("regpassword"))})
            flash("new password is {}".format(mongo.db.users.find_one({"user_name" : session["user"]}["user_password"])))

    return render_template("change_pwd.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("dictionary"))


# Error code taken from askPython https://www.askpython.com/python-modules/flask/flask-error-handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        debug=True,
        port = int(os.environ.get("PORT"))
    )