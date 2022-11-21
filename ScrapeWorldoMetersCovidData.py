# import libraries 
from bs4 import BeautifulSoup
import requests 
import pandas as pd


# Create an URL object
url = 'https://www.worldometers.info/coronavirus/'
# Create object page
page = requests.get(url)
# Change html to Python friendly format 
soup = BeautifulSoup(page.text,'html5lib')

# Obtain infromation from tag <table>
table1 = soup.find('table',id='main_table_countries_today')

# Obtain every title of columns with tag <th>
headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)
headers[13] = 'Tests/1M pop'

# Create a dataframe
mydata = pd.DataFrame(columns = headers)

# Create a for loop to fill mydata
for j in table1.find_all('tr')[4:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# Drop and clearing unnecessary rows
mydata.drop(mydata.index[0:7], inplace=True)
mydata.drop(mydata.index[222:229], inplace=True)
mydata.reset_index(inplace=True, drop=True)
# Drop “#” column
mydata.drop('#', inplace=True, axis=1)

# Export to json file
mydata.to_json(r'covid_data.json', orient = 'columns')