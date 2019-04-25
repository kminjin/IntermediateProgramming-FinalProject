import requests, json, csv
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd #helps convert data into tabular structure
from urllib.request import urlopen #new module meets 1/6 requirements
import re #secondmodule
# tools that will make it easier to build on things
from advanced_expiry_caching import Cache



continents=pd.read_csv("continents.csv")

countries=pd.read_csv("cleaned_countries.csv")
continents=pd.read_csv("continents.csv")

df_new=countries.merge(continents[['Country', 'Continent_Name']])

df_new.to_csv("final_countriesDB.csv", index = False)


# list_Asia=[]
# list_NA=[]
# list_SA=[]
# list_Europe=[]
# list_Africa=[]
# list_Oceania=[]

#     if row[7]== "Asia":
#         list_Asia.append(row[0])
#     if row[7]== "North America":
#         list_NA.append(row[0])
#     if row[7]== "South America":
#         list_SA.append(row[0])
#     if row[7]== "Africa":
#         list_Africa.append(row[0])
#     if row[7]== "Europe":
#         list_Europe.append(row[0])
#     if row[7]== "Oceania":
#         list_Oceania.append(row[0])
