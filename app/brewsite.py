from flask import Flask
from flask import render_template as rt
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user="Luke Romero")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", user="Luke Romero")


@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html", user="Luke Romero")


@app.route("/about")
def about():
    return rt("about.html", user="Luke Romero")


if __name__ == "__main__":
    app.run(
        debug=True,
        use_debugger=False,
        use_reloader=False
    )