from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

@app.route("/")
def home():
    mars_mission = mongo.db.collection.find_one()
    return render_template("index.html", mission=mars_mission)
@app.route("/scrape")
def scrape():
    mars_news= mongo.db.collection
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)
if __name__ =="__main__":
    app.run(debug=True)