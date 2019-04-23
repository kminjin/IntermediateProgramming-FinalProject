import requests, json, csv
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd #helps convert data into tabular structure
from urllib.request import urlopen #new module meets 1/6 requirements
import re #secondmodule
# tools that will make it easier to build on things
from advanced_expiry_caching import Cache


START_URL = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
FILENAME = "countries.json"

# So I can use 1 (one) instance of the Cache tool -- just one for my whole program, even though I'll get data from multiple places
PROGRAM_CACHE = Cache(FILENAME)

# assuming constants exist as such
# use a tool to build functionality here
def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data) # default here with the Cache.set tool is that it will expire in 7 days, which is probs fine, but something to explore
    return data

#######

main_page = access_page_data(START_URL)


# website_url = requests.get(‘https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area’).text
def infoFromHTML(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# function 1
# def infoFromHTML(link):
#     html = requests.get(link)
#     soup = BeautifulSoup(html.content, 'html.parser')
#     return soup

info = infoFromHTML('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
# tables = info.find_all('table') #countries are in table format
# for table in tables:
#     print(table.prettify()) #print what is in tables but make output more readable

table = info.find('table', {'class': 'wikitable sortable'}) #after inspecting tables, we see wikitable sortable has data we need.
rows = table.find_all('tr') #find all the countries
#print(rows) #gives you all info on 538 countries


# List of all links of countries
for row in rows:
    cells = row.find_all('td') #each value in each row(country item)
    if len(cells) > 1:
        country_links = cells[1].find('a') #cells[1] has url info
        # print(country_link.get('href'))


# function 2
#get information from each country!
def getAdditionalDetails(url):
    try:
        each_country = infoFromHTML('https://en.wikipedia.org' + url)
        table = each_country.find('table', {'class': 'infobox geography vcard'})
        eachCountryDetails = []
        read_info = False
        for tr in table.find_all('tr'):
            if (tr.get('class') == ['mergedtoprow'] and not read_info):
                link = tr.find('a')
                if (link and (link.get_text().strip() == 'Area' or
                   (link.get_text().strip() == 'GDP' and tr.find('span').get_text().strip() == '(nominal)'))):
                    read_info = True
                if (link and (link.get_text().strip() == 'Population')):
                    read_info = False
            elif ((tr.get('class') == ['mergedrow'] or tr.get('class') == ['mergedbottomrow']) and read_info):
                eachCountryDetails.append(tr.find('td').get_text().strip('\n'))
                if (tr.find('div').get_text().strip() != '•\xa0Total area' and
                   tr.find('div').get_text().strip() != '•\xa0Total'):
                    read_info = False

        return eachCountryDetails
    except Exception as error:
        print('Error occured: {}'.format(error))
        return []

#I want to cache data here
data_info = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1:
        print(cells[1].get_text())
        country_link = cells[1].find('a')
        country_info = [cell.text.strip('\n') for cell in cells]
        additional_details = getAdditionalDetails(country_link.get('href'))
        if (len(additional_details) == 4):
            country_info += additional_details
            data_info.append(country_info)


all_pages=[]
for l in country_links:
    page_data=access_page_data('https://en.wikipedia.org' + country_link.get('href'))
    soup_of_page = BeautifulSoup(page_data, features="html.parser")
    all_pages.append(soup_of_page)



dataset = pd.DataFrame(data_info)

# Define column headings
headers = rows[0].find_all('th')
headers = [header.get_text().strip('\n') for header in headers]
headers += ['Total Area', 'Percentage Water', 'Total Nominal GDP', 'Per Capita GDP']
dataset.columns = headers

drop_columns = ['Rank', 'Date', 'Source']
dataset.drop(drop_columns, axis = 1, inplace = True)

dataset.to_csv("Dataset.csv", index = False)

dataset = pd.read_csv("Dataset.csv")
dataset.rename(columns={'Country(or dependent territory)': 'Country'}, inplace = True)
dataset.rename(columns={'% of worldpopulation': 'Percentage of World Population'}, inplace = True)
dataset.rename(columns={'Total Area': 'Total Area (km2)'}, inplace = True)

for column in dataset.columns:
    dataset[column] = dataset[column].str.replace(r"\(.*\)", "")
    dataset[column] = dataset[column].str.replace(r"\[.*\]", "")
#remove all parenthesis, square brackets, contents inside them

dataset['Percentage of World Population'] = dataset['Percentage of World Population'].str.strip('%')
dataset['Percentage Water'] = dataset['Percentage Water'].str.strip('%')
dataset['Percentage Water'] = dataset['Percentage Water'].str.strip()

dataset['Population'] = dataset['Population'].str.replace(',', '')

dataset['Total Area (km2)'] = dataset['Total Area (km2)'].str.replace(',', '')

for x in range(len(dataset['Total Area (km2)'])):
    area = dataset.iloc[x]['Total Area (km2)']
    if ('sq\xa0mi' in area):
        area = area.split('-')[0]
        area = re.sub(r'[^0-9.]+', '', area)
        area = int(float(area) * 2.58999)
    else:
        area = area.split('-')[0]
        area = re.sub(r'[^0-9.]+', '', area)
        area = int(float(area))
    dataset.iloc[x]['Total Area (km2)'] = area

dataset['Percentage Water'] = dataset['Percentage Water'].replace('negligible', '0.0')
dataset['Percentage Water'] = dataset['Percentage Water'].replace('Negligible', '0.0')
dataset['Percentage Water'] = dataset['Percentage Water'].str.replace(r'[^0-9.]+', '')

dataset.to_csv("Final_dataset.csv", index = False)
