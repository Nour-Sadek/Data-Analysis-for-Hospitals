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

# Changing the names of some of the columns so they match those in the general
# hospital DataFrame

prenatal_df.rename(columns={'HOSPITAL': 'hospital',
                            'Sex': 'gender',}, inplace=True)
sports_df.rename(columns={'Hospital': 'hospital',
                          'Male/female': 'gender'}, inplace=True)

# Merging the datasets into one

all_hospitals_df = pd.concat([general_df, prenatal_df, sports_df],
                             ignore_index=True)

# Deleting the 'Unnamed: 0' column

all_hospitals_df.drop(columns='Unnamed: 0',
                      inplace=True)

# Printing out the merged DataFrame <all_hospitals_df>

print('A sample of 20 rows from the merged DataFrame that contains data from all\
 three hospitals:')
print(all_hospitals_df.sample(n=20), end='\n\n')

"""Stage 3: Improve your dataset

Description

Some cells in our table have NaN as values: the patient gender is not defined in 
the prenatal hospital, and columns with the results of medical tests have empty 
values in all three tables. We still cannot commit to the analysis as the 
statistics are not going to be objective. We have to correct the table for 
further study.

Objectives

Let's take a closer look at the gender column. It's a big mess: there we have 
female, male, man, woman. You need to correct the data in this column. The 
values should be either f or m. Replace the empty gender column values for 
prenatal patients with f (we can assume that the prenatal treats only women).

The bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months 
columns also need to be corrected. Replace the NaN values of the columns above 
with zeros.

Additionally, delete all the empty rows.

"""

# Delete all empty rows

all_hospitals_df.dropna(axis=0, how='all', inplace=True)

# Correct all the gender column values to 'f' and 'm' from {'female', 'woman'}
# and {'male', 'man'} respectively

all_hospitals_df['gender'] = all_hospitals_df['gender'].replace({'female': 'f',
                                                                 'woman': 'f',
                                                                 'male': 'm',
                                                                 'man': 'm'})

# Change all NaN's values in the <all_hospitals_df> 'gender' column
# corresponding to the prenatal hospital to 'f'

all_hospitals_df.loc[all_hospitals_df.hospital == 'prenatal',
                                                  'gender'] = \
    all_hospitals_df.loc[all_hospitals_df.hospital == 'prenatal',
                                                      'gender'].fillna('f')

# Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound,
# mri, xray, children, months columns with zeros

all_hospitals_df[['bmi', 'diagnosis',
                  'blood_test', 'ecg', 'ultrasound',
                  'mri', 'xray', 'children',
                  'months']] = all_hospitals_df[['bmi', 'diagnosis',
                                                 'blood_test', 'ecg',
                                                 'ultrasound',
                                                 'mri', 'xray', 'children',
                                                 'months']].fillna(0)

# Print the shape of the DataFrame and a random set of 20 rows
print('A sample of 20 rows from the improved DataFrame where missing values\
 have been handled: ')
print(all_hospitals_df.sample(n=20, random_state=30), end='\n\n')
