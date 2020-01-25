from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title= soup.find("div", id="news")
    news_article= soup.find("div", id="news")

    mars_news = {
        "news_title": news_title,
        "news_article": news_article
    }

    browser.quit()
    return mars_news
