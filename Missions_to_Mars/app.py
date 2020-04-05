from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.current_mars_info
collection = db.mars_info

@app.route("/")
def index():
    articles = mongo.db.collection.articles.find_one()
    return render_template("index.html", articles=articles)
@app.route("/scrape")
def scrape():
    articles= mongo.db.collection
    articles_data = scrape_mars.scrape()
    articles.update({}, articles_data, upsert=True)
    return redirect("/", code=302)
if __name__ =="__main__":
    app.run(debug=True)