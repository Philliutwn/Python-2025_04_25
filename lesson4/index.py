from flask import Flask,render_template

print('Hello Flask!')

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # return "<h1>Hello, World!</h1><h2>This is my first web page</h2>"
    return render_template("index.html.jinja2")

@app.route("/user")
def user():
    return "<h1>User!</h1><h2>This is my 2nd web page</h2>"

@app.route("/Product")
def product():
    return "<h1>Product</h1><h2>This is my 3rd web page</h2>"