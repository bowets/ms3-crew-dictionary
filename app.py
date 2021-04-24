import os
from flask import Flask

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")



@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/user")
def user():
    return "<p>USER</p>"


if __name__ == "__main__":
    app.run(
        debug=True
    )