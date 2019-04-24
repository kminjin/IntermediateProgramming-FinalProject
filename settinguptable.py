import requests, json, csv
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd #helps convert data into tabular structure
from urllib.request import urlopen #new module meets 1/6 requirements
import re #secondmodule
# tools that will make it easier to build on things
from advanced_expiry_caching import Cache



countries=pd.read_csv("final_dataset.csv")
continents=pd.read_csv("continents.csv")


df_new=countries.merge(continents[['Country', 'Continent_Name']])

df_new.to_csv("new_countriestable.csv", index = False)
