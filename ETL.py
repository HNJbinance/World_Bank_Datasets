# Importing necessary libraries for the project
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

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
