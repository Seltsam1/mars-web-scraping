### Scraping Steps for Mars App ###

# Dependencies

from bs4 import BeautifulSoup as bs
import pandas as pd

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

##################################
### Functions ###
##################################

# Function to execute scraping code and return data as a dictionary

def scrape_all():

    # Executable path
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # call mars_news function and save in variables
    news_title, news_paragraph = mars_news(browser)

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser)
    }

    # Close browser
    browser.quit()

    # Print to console
    print("All scraping complete")

    # return data as dictionary
    return data


### NASA website ###
def mars_news(browser):

    # Url to be scraped (NASA Mars News Site)
    url = "https://mars.nasa.gov/news/"

    # Direct browser to nasa page
    browser.visit(url)

    # Save html from browser to variable
    html = browser.html

    # Create Beautiful soup object and parse
    soup = bs(html, "html.parser")

    # Retrieve results for most recent title and paragraph description (top most article)
    try:
        results = soup.select_one("ul.item_list li.slide")
    
        # Save first title as title variable
        title = results.find("div", class_="content_title").text

        # Save first paragraph of article as paragraph variable
        paragraph = results.find("div", class_="article_teaser_body").text

        # Print to console
        print("Scraping of NASA website complete")

    except:
        print("No data found")
        return None, None

    return title, paragraph


### JPL website ###
def featured(browser):

    # Url to be scraped for image (Jet Propulsion Laboratory, California Institute of Technology)
    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"

    # Direct browser to JPL page
    browser.visit(url)

    # Save html from browser to variable
    html = browser.html

    # Create Beautiful soup object and parse
    soup_image = bs(html, "html.parser")

    # Click on "full image" to get larger pic
    try:
        full_image = soup_image.find("a", class_="showimg fancybox-thumbs")
    except:
        print("No data found")
        return None, None

    # Save relative url of image with base url into variable
    featured = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + full_image["href"]

    # Print to console
    print("Scraping of JPL website complete")

    return featured


### Space Facts website ###
def mars_facts():

    # Convert html with pandas
    df = pd.read_html("https://space-facts.com/mars/")

    # Select first dataframe in list
    mars_df = df[0]

    # Name columns
    mars_df.columns=["Description", "Mars"]

    # Set first column as index
    mars_df.set_index("Description", inplace=True)

    # Print to console
    print("Scraping of Space Facts website complete")

    return mars_df.to_html(classes="table table-striped")


### USGS Astrogeology website ###
def hemispheres(browser):

    # Url to be scraped for images (USBS Astrogeology)
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Direct browser to USGS page
    browser.visit(url)

    # List of hemispheres
    hemisphere_urls = browser.find_by_css("a.product-item h3")

    # Empty list to save final pic urls
    hemisphere_images = []

    # Loop through list of hemispheres
    for i in range(len(hemisphere_urls)):
        
        # Empty dictionary for images
        hemisphere = {}
        
        # Click to get link to larger image
        browser.find_by_css("a.product-item h3")[i].click()
        
        # Get image url and titles for images
        try:
            hemisphere_links = browser.links.find_by_text("Sample").first["href"]
            hemisphere_title = browser.find_by_css("h2.title").text
            
            # Save results in dictionary
            hemisphere["title"] = hemisphere_title
            hemisphere["link"] = hemisphere_links
            
            # Append dictionary values to list
            hemisphere_images.append(hemisphere)
            
            # Go back to prior page
            browser.back()

        except:
            print("No data found")
            return None
    
    # Print to console
    print("Scraping of USGS Astrogeology complete")
    
    return hemisphere_images