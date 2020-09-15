###----------  Import Packages ------------
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# packages for wordclouds
# note - must install wordcloud
# conda install -c conda-forge wordcloud
import string
import collections
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

###---------- Read in Data ------------
# read a csv into a panda dataframe
# Rulings file
rulingsFile = "/Users/joycewoznica/Syracuse/IST652/Project/data/horse-racing-rulings-beginning-1985.csv"
# remove everything prior to 2009 to match other datasets
# License File
licenseFile = "/Users/joycewoznica/Syracuse/IST652/Project/data/horse-racing-licensing.csv"
# Death and Breakdown File
incidentFile = "/Users/joycewoznica/Syracuse/IST652/Project/data/Equine_Death_and_Breakdown.csv"

rulingsDF = pd.read_csv(rulingsFile)
licenseDF = pd.read_csv(licenseFile)
incidentDF = pd.read_csv(incidentFile)

###---------- Review Structures and Data Clean-up ------------
# review structures
str(rulingsDF)
rulingsDF.shape
# reveals 36790 rows with 14 columns (data needs to only include 2009-2019)
str(licenseDF)
licenseDF.shape
# 25068 rows and 7 columns
str(incidentDF)
incidentDF.shape
# 4148 rows and 13 columns (need to remove 2020 from the data)
# Remove unwanted years from dataframes
# get listing of all rows with a Fine Year <= 2008 (only interested in the last decade)
# also remove any 2020 infractions if they exist, since not a full year
indexNames = rulingsDF[rulingsDF['Fine Year'] <= 2008].index
rulingsDF.drop(indexNames, inplace=True)
rulingsDF.shape
# drops down to only 11,516 rows and 14 columns (removed 25284 rows)
# remove 2020 (since not yet over) from incidentDF
indexNames = incidentDF[incidentDF['Year'] >= 2020].index
incidentDF.drop(indexNames, inplace=True)
incidentDF.shape
# now down to 4152 rows and 13 columns

# Do we need to drop NaN or blanks
rulingsDF.isna().sum()
# need to remove row with blank 'Notice Date'
# need to remove rows with blank rules


# - still needs to be done, but mostly around Suspension Dates which may not be required
# - missing Rules or Notice Date is fine, so no NA removal required

#------------ Merge on Dates -------------
# merging on Dates and Track
# first make dates match
# same column name for Notice Date
# Notice Date is in format: 2019-02-09T00:00:00.000
# Incident Date is format: 02/17/2020
# Track is in rulingsDF
# Race Track is in incidentDF

# Must work on putting dates in same format

# Change columns to "Date" and "Track" in both frames



# merge the dataframes
merged_df = DF2.merge(DF1, how = 'inner', on = ['date', 'hours'])