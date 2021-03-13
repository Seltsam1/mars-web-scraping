#################################################
# Mars App
#################################################

# Dependencies

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


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
    return "TBD"




# To run applicaton

if __name__ == "__main__":
    app.run(debug=True)
