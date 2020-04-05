from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    articles = {}
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    articles["news_title"] = soup.find("a", class_="bottom_gradient").get_text()
    articles["news_article"] = soup.find("a", class_="rollover_description_inner").get_text()
    
    mars_news = {
        "news_title": news_title,
        "news_article": news_article
    }

    browser.quit()
    return mars_news
def scrape_pic():
    browser_pic= init_browser()
    mars = {}
    featured_image_url = "https://mars.nasa.gov/news/"
    browser_pic.visit(featured_image_url)

    html = browser_pic.html
    soup = bs(html, "html.parser")

    mars = soup.find("img style").get_jpg()
    
   

    browser.quit()
    return mars

    