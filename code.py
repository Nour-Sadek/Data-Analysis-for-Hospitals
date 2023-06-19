# Imported packages
import pandas as pd

"""Stage 1: Upload the data

Description

Imagine you are a data scientist and you're currently working with the data for 
local hospitals. You have several files with information about patients from 
different districts. Sometimes, the data is split into many datasets or may 
contain empty or invalid values. The first step is to preprocess the data before 
the analysis: merge the files into one, delete empty or incorrect rows, fill the 
missing values, and so on.

Objectives

In this stage, you will deal with datasets that contain information about 
patients from three hospitals: a general, a prenatal, and a sports one. You need 
to upload the data from the hidden test directory of the project for further 
processing.

"""

# Reading the data sets from the three hospitals: general, prenatal, and sports
# stored as .csv files in the Data directory

general_df = pd.read_csv('Data/general.csv')
prenatal_df = pd.read_csv('Data/prenatal.csv')
sports_df = pd.read_csv('Data/sports.csv')

# Printing the first 20 rows of each hospital DataFrame

print('The first 20 rows of the dataset from the general hospital:')
print(general_df.head(20), end='\n\n')
print('The first 20 rows of the dataset from the prenatal hospital:')
print(prenatal_df.head(20), end='\n\n')
print('The first 20 rows of the dataset from the sports hospital:')
print(sports_df.head(20), end='\n\n')

