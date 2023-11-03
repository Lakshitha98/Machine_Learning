# Data Pre-processing Lab Assignment

# **----- Import all libraries here -----**

import pandas as pd
import numpy as np

# Import the dataset into a data frame -----------------------------------
dataset = pd.read_csv('diabetes_.csv')

# Code to pre-process the dataset goes here --------------------------------


# Write the pre-processed dataset into a csv file --------------------------------
pre_processed_dataset = dataset

student_id = "123456.csv"

pre_processed_dataset.to_csv(student_id, index=False)
