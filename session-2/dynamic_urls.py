from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/welcome/amit")
def welcome_amit():
    return "<h1>Hey Amit, Welcome Our WebPage!</h1>"


@app.route("/welcome/jahir")
#def welcome_amit():   #two different endpoints can not have the same function name.
def welcome_jahir():
    return "<h1>Hey Jahir, Welcome Our WebPage!</h1>"

# if we have 100000 more people?!
# We will use path parameters concept here.

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hey {name.title()}, Welcome Our WebPage!</h1>"  #f string is a cool, capable for 3.6+
# based on our input (perameters), the url/endpoint is created dynamically.


if __name__ == "__main__":
    app.run(debug = True)