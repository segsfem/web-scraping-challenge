from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    executable_path = {"executable_path": "/web-scraping-challenge/Missions_to_Mars/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)