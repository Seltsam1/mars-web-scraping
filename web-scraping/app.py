#################################################
# Mars App
#################################################

# Dependencies

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# From mars-scraping.py file
import mars_scraping

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Database Setup
#################################################

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Route for scraping websites
@app.route("/scrape")
def scrape():

    # Create collection in mongo database
    mars = mongo.db.mars
    
    # Call scrape_all function from python file
    mars_data = mars_scraping.scrape_all()

    # Insert data into mongo database
    mars.update({}, mars_data, upsert=True)

    # Redirect to index.html
    return redirect("/", code=302)


# To run applicaton

if __name__ == "__main__":
    app.run(debug=True)
