# Project-Covid-Dashboard-ME-5250
# Libraries to include for data scraping
BeautifulSoup4

Requests

pandas

html5lib

datetime
# How to run the scrape website module
Step 1: Ensure the libraries listed above have been installed 

Step 2: Download the scrape website module and place it in your desired project folder

Step 3: Open a new python file and save it in the same project folder where you placed the scrape website module 

Step 4: In your python file import the scrape website module using the following command "import ScrapeWebsite"

Step 5: Now you can use the scrape country function to get the following statistics for a specific country 

        - Total Deaths
        
        - Daily Deaths
        
        - Total Deaths/1 Million Population
        
        - Daily Deaths/1 Million Population
        
        The function will save these statistics as a json file to your project folder with the following name "Covid_data_for_CountryInput_CurrentDate.json"
        
        The function scrapes date from 'https://www.worldometers.info/coronavirus/' 
        
        The function has two inputs the country name whos statistics you want to observe and the website 'https://www.worldometers.info/coronavirus/'
        
        To use the function simply type ScrapeWebsite.scrape_country('Country Name','https://www.worldometers.info/coronavirus/')
        
        
Step 6: When you run the function a json file will be saved in your project folder with the statistics of the country you put into the function

Note: There is a "TestScrapeWebsite.py" file above that has the function calls for four countries the USA,China,India, and Mexico you can use this file to test and makes sure the ScrapeWebsite module is working properly and you downloaded all the necessary libraries. 

# Libraries to include for data display
PyYAML>=3.10

python-dateutil>=2.1

Jinja2>=2.7

numpy>=1.11.3

pillow>=4.0

packaging>=16.8

tornado>=5

typing_extensions >=3.7.4

bokeh


# Example on how to web scrape
https://medium.com/analytics-vidhya/how-to-scrape-a-table-from-website-using-python-ce90d0cfb607

# Examples of how to use the bokeh module
https://www.geeksforgeeks.org/python-bokeh-tutorial-interactive-data-visualization-with-bokeh/?tab=article
