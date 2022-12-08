# import libraries 
from bs4 import BeautifulSoup
from datetime import date
import requests 
import pandas as pd


def scrape_country(CountryInput,WebsiteInput):
    # make the CountryInput lower case 
    CountryInput = CountryInput.lower()
    # Create an URL object
    url = WebsiteInput
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
    for j in table1.find_all('tr')[2:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row

    # Drop and clearing unnecessary rows
    mydata.drop(mydata.index[0:7], inplace=True)
    mydata.drop(mydata.index[222:229], inplace=True)
    mydata.reset_index(inplace=True, drop=True)
    # Drop data that isnt needed from each column
    mydata.drop('#', inplace=True, axis=1)
    mydata.drop('TotalCases',inplace = True,axis=1)
    mydata.drop('NewCases',inplace = True,axis=1)
    mydata.drop('TotalRecovered',inplace = True,axis=1)
    mydata.drop('NewRecovered',inplace = True,axis=1)
    mydata.drop('ActiveCases',inplace = True,axis=1)
    mydata.drop('Serious,Critical',inplace = True,axis=1)
    mydata.drop('Tot\xa0Cases/1M pop',inplace = True,axis=1)
    mydata.drop('TotalTests',inplace = True,axis=1)
    mydata.drop('Tests/1M pop',inplace = True,axis=1)
    mydata.drop('Population',inplace = True,axis=1)
    mydata.drop('Continent',inplace = True,axis=1)
    mydata.drop('1 Caseevery X ppl',inplace = True,axis=1)
    mydata.drop('1 Deathevery X ppl',inplace = True,axis=1)
    mydata.drop('1 Testevery X ppl',inplace = True,axis=1)
    mydata.drop('New Cases/1M pop',inplace = True,axis=1)
    mydata.drop('Active Cases/1M pop',inplace = True,axis=1)
    
    # Make the country names lower case 
    mydata['Country,Other'] = mydata['Country,Other'].str.lower()
        
    # Access the country input by user
    output = mydata.loc[(mydata["Country,Other"]) == CountryInput]

    # Export to json file with current date
    today_date = str(date.today())
    file_name = "json_files/Covid_data_for_" + CountryInput + "_" + today_date + ".json"
    output.to_json(file_name)
