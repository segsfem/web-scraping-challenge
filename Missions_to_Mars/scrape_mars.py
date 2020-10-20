from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    executable_path = {"executable_path": "/web-scraping-challenge/Missions_to_Mars/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_news():
    browser = init_browser()

    # Visit https://mars.nasa.gov/news
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #store data in variables
    news_title = soup.find("h1", class_="article_title").get_text()
    news_p = soup.find("p", class_="main_image_caption").get_text()

    mars_data = {
        "title": news_title,
        "paragraph": news_p
    }

    browser.quit()

    return mars_data

def scrape_images():
    browser = init_browser()

    #Visit https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #store data in variables
    relative_image_path = soup.find_all('img')[0]["src"]
    featured_image = url + relative_image_path

    mars_image = {
        "image": = featured_image
    }

    browser.quit()

    return mars_image

def scrape_table():
    browser = init_browser

    #Visit https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    
    tables = pd.read_html(url)

    mars_tables = {
        "tables": tables
    }

    browser.quit()

    return mars_tables

hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "/static/image/Valles Marineris Hemisphere"},
    {"title": "Cerberus Hemisphere", "img_url": "/static/image/Cerberus Hemisphere"},
    {"title": "Schiaparelli Hemisphere", "img_url": "/static/image/Schiaparelli Hemisphere"},
    {"title": "Syrtis Major Hemisphere", "img_url": "/static/image/Syrtis Major Hemisphere"}
]

scrape_mars = [
    {
        "news": mars_data,
        "featured_image": = mars_image,
        "tables": mars_image
        "hemisphere_image": hemisphere_image_urls
    }
]








