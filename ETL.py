# Importing necessary libraries for the project
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

for dirname, _, filenames in os.walk('./'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# import the projects_data.csv file using the pandas library
df_projects = pd.read_csv('./projects_data.csv')

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
#df_population = pd.read_csv('./population_data.csv')

f = open("./population_data.csv")
for i in range(10):
    line = f.readline()
    print('line: ', i, line)
f.close()