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

    ''' Dictionary home page '''

    words = mongo.db.words.find().sort("word")

    # If there is a session, find the user which is in the session
    # and return the home page with the user variable
    if is_authenticated():

        user_type = mongo.db.users.find_one(
            {"user_name": session["user"]})["user_type"]
        
        return render_template("dictionary.html", words=words, user_type=user_type)
    else:
        return render_template("dictionary.html", words=words)    


@app.route("/search", methods=["GET", "POST"])
def search():

    ''' Dictionary search function '''

    search_word = request.form.get("query").lower()
    words = mongo.db.words.find({"$text": {"$search": search_word}})
    if session.get("user") is not None:
        user = mongo.db.users.find_one(
            {"user_name": session["user"]})["user_type"]
        return render_template("dictionary.html", words=words, user_type=user)
    else:
        return render_template("dictionary.html", words=words) 


@app.route("/about")
def about():
    '''About dictionary'''

    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    '''Register new user'''

    # Reference for this code is above function definition below
    if is_authenticated():
        flash("Please log out first before registering a new user")
        return redirect(url_for("dashboard"))

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
    '''Log in existing user'''

    #check if another user is already logged in
    if is_authenticated():
        flash("You must log out first before logging back in")
        return redirect(url_for("login"))

    #if no users logged in, log in user
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

        #if username does not match
        else:
            flash("Username and/or password are not correct")
            return redirect(url_for("login"))
        
    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    #grab the session user and find user in database
    #import pdb; pdb.set_trace()

    #check if user is in session, if not redirect to login page
    if not is_authenticated():
        flash("You are not logged in, you must log in first")
        return redirect(url_for("login"))
        
    username = mongo.db.users.find_one(
        {"user_name": session["user"]})["user_name"]
    words = mongo.db.words.find()
    user_type = mongo.db.users.find_one({"user_name": session["user"]})["user_type"]
    words_active = mongo.db.words.count_documents({"word_submitted_by": session["user"], "word_status": "approved"})
    words_pending = mongo.db.words.count_documents({"word_submitted_by": session["user"], "word_status": "pending_approval"})
    words_to_approve = mongo.db.words.count_documents({"word_status": "pending_approval"})
    

    return render_template("user_dashboard.html", username=username, words=list(words), user_type=user_type, words_active=words_active, words_pending=words_pending, words_to_approve=words_to_approve)


@app.route("/submit_word", methods=["GET", "POST"])
def submit_word():
    if request.method == "POST":
        existing_word = mongo.db.words.find_one({"word": request.form.get("word")})

        if not existing_word:
            word = {
                "word": request.form.get("word").lower(),
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
            return redirect(url_for("dashboard", username=session["user"]))
        else:
            flash("This word already exists, please submit a new word")
            return redirect(url_for("submit_word"))

    categories = mongo.db.category.find()
    return render_template("submit_word.html", categories = categories)


@app.route("/edit_word/<word_id>", methods=["GET", "POST"])
def edit_word(word_id):
    if request.method == "POST":
        edit_word = {
                "word": request.form.get("word").lower(),
                "word_category": request.form.get("word_category"),
                "word_definition": request.form.get("word_definition"),
                "word_sentence": request.form.get("word_sentence"),
                "word_submitted_by": session["user"],
                "word_approved_by": "",
                "word_status": "pending_approval",
                "word_submitted_datetime": datetime.now()
            }
        mongo.db.words.update({"_id": ObjectId(word_id)}, edit_word)
        flash("Word successfully updated. The word is in the pending queue and will be reviewed by one of the editors.")
        return redirect(url_for("dashboard", username=session["user"]))

    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})

    categories = mongo.db.category.find()
    return render_template("edit_word.html", word=word, categories = categories)


@app.route("/approve/<word_id>")
def approve(word_id):
    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    mongo.db.words.update({"_id": ObjectId(word_id)}, { "$set" : {"word_approved_by": session["user"], "word_status":"approved"}})
    flash("Approved")
    return redirect(url_for("dashboard", username=session["user"]))


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    mongo.db.words.remove({"_id": ObjectId(word_id)})
    flash("Word successfully deleted")
    return redirect(url_for("dictionary"))


@app.route("/change_pwd", methods=["GET", "POST"])
def change_pwd():
    if request.method == "POST":
        old_pwd = mongo.db.users.find_one({"user_name": session["user"]})["user_password"]
        
        if check_password_hash(old_pwd, request.form.get("old_pwd")):
            mongo.db.users.update_one({"user_name": session["user"]}, { "$set": {"user_password": generate_password_hash(request.form.get("regpassword"))} })
            flash("Password Successfully updated")
            return redirect(url_for("dashboard", username=session["user"]))

    return render_template("change_pwd.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user", None)
    return redirect(url_for("dictionary"))


# Error code taken from askPython https://www.askpython.com/python-modules/flask/flask-error-handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")


# Code taken from previous student project "ai-chat-annotator" by "NgiapPuoyKoh" from https://github.com/NgiapPuoyKoh/ai-chat-annotator/blob/7b37842579f8d1783de8d11be544f9790b248f05/app.py

def is_authenticated():
    ''' Is there a user in the session '''

    return 'user' in session




if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        debug=True,
        port = int(os.environ.get("PORT"))
    )