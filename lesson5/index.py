from flask import Flask

print('Hello Flask!')

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    # return "<h1>Hello, World!</h1><h2>This is my first web page</h2>"
    return render_template("index.html.jinja2")

@app.route("/classes")
def classes():
    return render_template("classes.html.jinja2")


@app.route("/news")
def news():
    return render_template("news.html.jinja2")

@app.route("/traffic")
def traffic():
    return render_template("traffic.html.jinja2")

@app.route("/contact")
def contact():
    return render_template("contact.html.jinja2")

