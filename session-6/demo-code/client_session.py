from flask import (
  Flask, render_template, redirect, url_for, flash
)

from forms import LoginForm

app = Flask (__name__)
app.config ["SECRET_KEY"] = "secret_key"

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html", title = "Home")


@app.route("/login")
def login():
  return render_template("login.html", title = "Login")

@app.route("/about")
def about():
  return render_template("about.html", title = "About")

@app.route("/contact")
def contact():
  return render_template("contact.html", title = "Contact")

if "__name__" == "__main__":
  app.run(debug=True)