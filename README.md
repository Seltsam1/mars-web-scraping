# mars-web-scraping

## Getting Started

This project will scrape 4 websites for data and images about Mars and use the resulting information in an app

- Websites scraped:
  - [Nasa Mars Exploration Program](https://mars.nasa.gov/news/ "Nasa Mars Exploration Program")
  - [Jet Propulsion Laboratory](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html "Jet Propulsion Laboratory")
  - [Space Facts - Mars](https://space-facts.com/mars/ "Space Facts - Mars")
  - [USGS Astrogeology - Mars](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars "USGS Atrogeology - Mars")

- All necessary files are in the "web-scraping" folder
  - The jupyter notebook file contains all prelimary code used in scraping the above websites and shows resulting values of variables
  - The first pyton file (marps_scraping.py) contains functions based on the code in the jupyter notebook to scrape the above websites
  - The second python file (app.py) will create a flask instance, store scraped data into a mongo database, and render the indext.html file
  - The html file (located in templates folder) is the landing page for the Mars app

## Features

- web-scraping.ipynb (Jupyter Notebook)
  - Uses BeautifulSoup, pandas, splinter, and webdriver_manager
  - NASA section
    - Gets the newest article title and descriptive paragraph
  - JPL section
    - Gets the "featured image" link
  - Space Facts section
    - Gets tabular information about Mars
    - Converts to pandas dataframe, then to HTML
  - USGS Astrogeology section
    - Gets 4 links to images for each hemisphere of Mars
  - Closes remote controlled browser at end

- mars_scraping.py
  - Contains a function "scrape_all" based on the code from the Jupyter Notebook
    - Function will call 4 subfunctions, one for each website to scrape
    - Prints messages to console when each step is complete
    - Returns all scraped data as a dictionary

- app.py
  - Uses flask and flask_pymongo
  - Imports the "scrape_all" function from the mars_scraping.py file
  - Has two app routes:
    - /scrape
      - Calls the "scrape_all" function
      - Stores the resulting data in a mongo database
      - Redirects back to index page
    - / (index)
      - Uses data from the mongo database
      - Renders data into the "index.htm" file

- index.html
  - Located in templates folder
  - Contains landing page for Mars app
  - Utilizes bootstrap css
  - Includes a for loop to go through the hemisphere impages

## Licensing by:

The code in this project is licensed under MIT license.
