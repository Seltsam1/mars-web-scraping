# mars-web-scraping

## Getting Started

This project will scrape 4 websites for data and images about Mars and use the resulting information in an app

- Websites scraped:
  - [Nasa Mars Exploration Program](https://mars.nasa.gov/news/ "Nasa Mars Exploration Program")
  - [Jet Propulsion Laboratory](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html "Jet Propulsion Laboratory")
  - [Space Facts - Mars](https://space-facts.com/mars/ "Space Facts - Mars")
  - [USGS Astrogeology - Mars](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars "USGS Atrogeology - Mars")

The jupyter notebook file contains all prelimary code used in scraping the above websites and shows resulting values of variables
The python file...

## Features

- web-scraping.ipynb (Jupyter Notebook)
  - Uses BeautifulSoup, pandas, and splinter
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

## Licensing by:

The code in this project is licensed under MIT license.
