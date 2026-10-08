from flask import Flask
from flask import Flask, render_template as rt
import requests

response = requests.get("https://api.openbrewerydb.org/v1/breweries/")
response.raise_for_status()
data = response.json()

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user="Luke Romero")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", content = data)

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