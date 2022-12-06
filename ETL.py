# Importing necessary libraries for the project
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import sqlite3
import requests

'''E-xtract'''
'''T-ransform'''
for dirname, _, filenames in os.walk('./'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# import the projects_data.csv file using the pandas library, when executing this line below we'll got an error dtype because there's values missed in some columns
#df_projects = pd.read_csv('./projects_data.csv')

#Read in the projects_data.csv file using the read_csv method and dtype = str option
df_projects = pd.read_csv('./projects_data.csv', dtype='str')

# See what the data looks like
df_projects.head()

# count the number of null values in the data set
df_projects.isnull().sum()

#  output the shape of the data frame
df_projects.shape

# read in the population_data.csv file using the read_csv() method
# Put the results in a variable called df_population
# df_population = pd.read_csv('./population_data.csv')


# We can see that The first four lines in the file are not properly formatted and don't contain data.
def inspect_rows(file_path : str, n_row = 10) :
    f = open(file_path)
    for i in range(n_row):
        line = f.readline()
        print('line: ', i, line)
    f.close()

inspect_rows('./population_data.csv', 10)

# Read in population data skipping first four rows
df_population = pd.read_csv('./population_data.csv', skiprows=4)

df_population.head()

# Count the number of null values in each column
print(df_population.isnull().sum(axis=1))

#After finding that each row contains at least a null value, we suspect the 'unamed : 62', so we drop it
df_population = df_population.drop('Unnamed: 62', axis=1)
# This code outputs any row that contains a null value
# The purpose is to see what rows contain null values now that
#   'Unnamed: 62' was dropped from the data.
df_population[df_population.isnull().any(axis=1)]

'''Extract from JSON and XML'''
# Read in the population_data.json file using pandas's
# read_json method. Don't forget to specific the orient option
# store the results in df_json

df_json = pd.read_json('./population_data.json', orient='records')
print(df_json.head())

# open the population_data.xml file and load into Beautiful Soup
with open("./population_data.xml") as fp:
    soup = BeautifulSoup(fp, features="html5lib") #lxml is the parser type

# output the first 5 records in the xml file
# this is an example of how to navigate the XML document with BeautifulSoup
i = 0
# use the find_all method to get all record tags in the document
for record in soup.find_all('record'):
    # use the find_all method to get all fields in each record
    i += 1
    for record in record.find_all('field'):
        print(record['name'], ': ' , record.text)
    print()
    if i == 5:
        break
'''Extract from database'''
# DEFINE THE DATABASE CREDENTIALS

conn = sqlite3.connect('./population_data.db')

print(pd.read_sql('SELECT "Country_Name", "Country_Code", "1960" FROM population_data', conn))

# We can perform the same extraction from DB using sqlalchemy if using Mysql or Postgres

'''Extract with api'''
# Run the code example below to request data from the World Bank Indicators API. According to the documntation,
# you format your request url like so:
# http://api.worldbank.org/v2/countries/ + list of country abbreviations separated by ; + /indicators/ + indicator name + ? + options

url = 'http://api.worldbank.org/v2/countries/br;cn;us;de/indicators/SP.POP.TOTL/?format=json&per_page=1000'
r = requests.get(url)

pd.DataFrame(r.json()[1])

# TODO: get the url ready
url = 'http://api.worldbank.org/v2/country/CH/indicator/SP.POP.TOTL/?format=json&date=1995:2001'

# TODO: send the request
r = requests.get(url)
r.json()
