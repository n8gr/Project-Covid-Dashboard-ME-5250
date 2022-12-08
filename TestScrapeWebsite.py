import ScrapeWebsite
import DataDisplay

# scrape the covid data for the USA
ScrapeWebsite.scrape_country('USA','https://www.worldometers.info/coronavirus/')

# scrape the covid data for China
ScrapeWebsite.scrape_country('China','https://www.worldometers.info/coronavirus/')

# scrape the covid data for India
ScrapeWebsite.scrape_country('India','https://www.worldometers.info/coronavirus/')

# scrape the covid data for Mexico
ScrapeWebsite.scrape_country('Mexico','https://www.worldometers.info/coronavirus/')

# Display the data from all files collected
DataDisplay.data_display()
