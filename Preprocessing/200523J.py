# Data Pre-processing Lab Assignment

# **----- Import all libraries here -----**

import pandas as pd
import numpy as np
from scipy.stats import zscore

# Import the dataset into a data frame -----------------------------------
dataset = pd.read_csv('diabetes.csv')

# Code to pre-process the dataset goes here --------------------------------
# this is to get datarame's columns to a list

column= dataset.columns

# this is to checking duplicates

print(dataset.duplicated().sum())

# this is to clear duplicates

dataset=dataset.drop_duplicates()

# this is to check missing values

print(dataset.isna().sum())
dum=len(column)
for i in range(dum):
    meanValue=dataset[column[i]].mean()
    medianValue=dataset[column[i]].median()
    # this is to fill missing values with median value or mean value
    if (abs(meanValue-medianValue)/meanValue)< 0.1:
        dataset[column[i]].fillna(meanValue, inplace=True)
    else:
        dataset[column[i]].fillna(medianValue, inplace=True)
print(dataset.isna().sum())

# this is to calculate correlation matrix

correlation_matrix = dataset.corr().abs()

# this is to get upper triangle of the correlation matrix
upper = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))

# this is to find that index of feature having corelation greter than 0.85
dropp = [column for column in upper.columns if any(upper[column] > 0.85)]

# drop high corelated featues

dataset = dataset.drop(dropp, axis=1)
# this is to get columns which having outliers
outlier_columns = []
for i in column:
    j = abs(zscore(dataset[i]))
    filt_ent = j > 3
    if any(filt_ent):
        outlier_columns.append(i)

print(outlier_columns)

# This is to remove outlier entities  
for i in outlier_columns:
    k = abs(zscore(dataset[i]))
    filt_ent = k < 3
    dataset = dataset[filt_ent]

print(dataset.head())

# Write the pre-processed dataset into a csv file --------------------------------
pre_processed_dataset = dataset

student_id = "200523J.csv"

pre_processed_dataset.to_csv(student_id, index=False)
