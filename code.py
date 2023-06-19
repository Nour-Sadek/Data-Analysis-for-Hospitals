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

"""Stage 2: Merge them!

Description

The datasets are uploaded but are somewhat difficult to work with. They are 
divided into three parts, and the column names are different: HOSPITAL and Sex 
in the prenatal, Hospital and Male/female in the sports facility. We cannot 
study our data in full and perform statistical calculations. It also stands in 
the way of good visualization.

Objectives

In this stage, we will change the column names and merge our datasets into one.
All column names in the sports and prenatal tables must match the column names 
in the general table. The three datasets will be merged in the following order:
general, prenatal, sports. After merging, a side Unnamed: 0 column will appear. 
This column contains the indexes of the tables. This column is not needed for 
the practical purposes of this project, so we will delete it in this stage.

"""