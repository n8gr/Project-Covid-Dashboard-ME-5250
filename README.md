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

Step 4: Create a folder named: json_files and place in the same project folder where you placed the scrape website module 

Step 5: In your python file import the scrape website module using the following command "import ScrapeWebsite"

Step 6: Now you can use the scrape country function to get the following statistics for a specific country 

        - Total Deaths
        
        - Daily Deaths
        
        - Total Deaths/1 Million Population
        
        - Daily Deaths/1 Million Population
        
        The function will save these statistics as a json file to your project folder with the following name "Covid_data_for_CountryInput_CurrentDate.json"
        
        The function scrapes date from 'https://www.worldometers.info/coronavirus/' 
        
        The function has two inputs the country name whos statistics you want to observe and the website 'https://www.worldometers.info/coronavirus/'
        
        To use the function simply type ScrapeWebsite.scrape_country('Country Name','https://www.worldometers.info/coronavirus/')
        
        
Step 7: When you run the function a json file will be saved in the json_files folder in the project folder with the statistics of the country you put into the function

Note: There is a "TestScrapeWebsite.py" file above that has the function calls for four countries the USA,China,India, and Mexico you can use this file to test and makes sure the ScrapeWebsite module is working properly and you downloaded all the necessary libraries. 

# Libraries to include for data display
PyYAML

python-dateutil

Jinja2

numpy

pillow

packaging

tornado

typing_extensions 

bokeh

glob


# Steps to run the data_display module
Step 1: Install all of the libraries listed above.

Step 2: Download DataDisplay.py file and place it in your desired project folder.

Step 3: Create or place a folder named json_files in the same project  folder as your DataDisplay.py file.

Step 4: To call the module in your project use the DataDisplay.data_display(). The module will than display the following:

        - Graphs of the Total and New covid deaths each day(days that are in json files), Graphs the Total deaths and new deaths per 1M.
        
        - You can toggle between the different plots by selecting the tabs above the graph.
        
        - Each country will be repressented by a new color.
        
        - The module will plot as many countries as you have a json file

Note: In the "TestScrapeWebsite.py" file above there is also a call to DataDisplay module to test the files written in.
