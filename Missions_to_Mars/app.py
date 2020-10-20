from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

#Establish mongodb connection
mongo = PyMongo(app, uri="mongodb://localhost:27017//mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    mars_news = mongo.db.mars.find_one()
    return render_template("index.html", listings=listings)

if __name__ == "__main__":
    app.run(debug=True)
