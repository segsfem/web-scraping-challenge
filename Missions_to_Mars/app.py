from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "/static/image/Valles Marineris Hemisphere"},
    {"title": "Cerberus Hemisphere", "img_url": "/static/image/Cerberus Hemisphere"},
    {"title": "Schiaparelli Hemisphere", "img_url": "/static/image/Schiaparelli Hemisphere"},
    {"title": "Syrtis Major Hemisphere", "img_url": "/static/image/Syrtis Major Hemisphere"}
]