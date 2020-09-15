# Homework 1
# Author: Joyce Woznica
# Class: IST 652
###----------  Import Packages ------------
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

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

###---------- Analysis: Question 1 ------------
# Question 1: Which tracks have the most infractions?
# count infractions by Race Track
rulingsDFbyTrack = rulingsDF['Race Track'].value_counts()
rulingsDFbyTrack = rulingsDFbyTrack.to_frame()
trackNames = rulingsDFbyTrack.index.values
rulingsDFbyTrack.columns = ['Infractions']


# Need to drop Main Office
rulingsDFbyTrack = rulingsDFbyTrack.drop(['Main Office', 'none', 'New York Racing Association'])
trackNames = rulingsDFbyTrack.index.values
# add column of track names
rulingsDFbyTrack['TrackName'] = trackNames

# plot with seaborn
fg = sns.factorplot(x = "TrackName", y = "Infractions", hue = "TrackName", dodge=False,
                    size = 5, aspect = 2, palette="Spectral", kind="bar", data=rulingsDFbyTrack)
#fg.set_title("Infractions by Race Track")
fg.set_xticklabels(rotation=45, horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'medium')
fg.set(xlabel = "Race Track", ylabel = "Number of Infractions", title = "Infractions by Race Track")
            
###---------- Analysis: Question 2 ------------
# Question 2: Are there more infractions in Harness or TB Racing?
# count infractions by Race Type
rulingsDFbyType = rulingsDF['Race Type'].value_counts()
rulingsDFbyType = rulingsDFbyType.to_frame()
RaceTypes = rulingsDFbyType.index.values
rulingsDFbyType.columns = ['Infractions']
# Need to remove blanks
rulingsDFbyType.isna()
rulingsDFbyType = rulingsDFbyType.drop(['?'])

my_colors='gc'
rulingsDFbyType.plot(kind='bar', label='Index', color=my_colors)

###---------- Analysis: Question 3 ------------
# Question 3: Are certain individuals receiving higher numbers of infractions that others?
# grab top 20 or 15 of the individuals (Full Name) and number of infractions sorted by highest to lowest
# count infractions by Full Name
rulingsDFbyName = rulingsDF['Full Name'].value_counts()
rulingsDFbyName = rulingsDFbyName.to_frame()
FullNames = rulingsDFbyName.index.values
rulingsDFbyName.columns = ['Infractions']
# Need to remove blanks
rulingsDFbyName.isna()
shortrulingsDFbyName = rulingsDFbyName.head(20)

my_colors='rmygbck'
shortrulingsDFbyName.plot(kind='bar', label='Index', color=my_colors)

###---------- Analysis: Question 4 (BROKEN) ------------
# Question 4: What occupation has the most infractions?
# cannot count this - come up with a better way to do this!
rulingsDFbyOccupation = rulingsDF['Occupation'].value.counts() 
rulingsDFbyOccupation = rulingsDFbyOccupation.to_frame()
Occupations = rulingsDFbyOccupation.index.values
rulingsDFbyOccupation.columns = ['Infractions']
# Need to remove blanks
rulingsDFbyOccupation.isna()

my_colors='rmygbck'
rulingsDFbyOccupation.plot(kind='bar', label='Index', color=my_colors)

###---------- Analysis: Question 5 (NEED PLOT) ------------
# Question 5: Track infractions over the years
str(rulingsDFbyTrack)
print(rulingsDFbyTrack.columns)
byTrackbyYear = pd.crosstab(rulingsDF['Race Track'], rulingsDF['Fine Year'])
# rows are tracks, but columns are years - need to create column renames
# Need to drop Main Office
byTrackbyYear = byTrackbyYear.drop(['Main Office', 'none', 'New York Racing Association'])

# column names
print(byTrackbyYear.columns)
print(byTrackbyYear.keys())
print(list(byTrackbyYear.columns))
# row names
print(byTrackbyYear.index.values)

# need to do this a line plot by column (year) and then different color for each track
sns.relplot(x="Fine Year", y="Race Track", col="align",
            hue="choice", size="coherence", style="choice",
            facet_kws=dict(sharex=False),
            kind="line", legend="full", data=byTrackbyYear);

###---------- Analysis: Question 6 (TO DO) ------------
# Question 6: Average Fine by Occupation
rulingsDFbyBoth = rulingsDF.groupby(['Full Name', 'Occupation'])
totalsbyBoth = rulingsDFbyBoth.sum()

###---------- Analysis: Question 7 (TO DO) ------------
# Question 7: Average Fine by Year


###---------- Analysis: Question 8 (TO DO) ------------
# Question 8: Total Fines by Year by Occupation


###---------- Analysis: Question 9 (TO DO) ------------
# Question 9: Total Fines by Track by Year


###---------- Analysis: Question 10 (TO DO) ------------
# Question 10: Are their common threads or words in the descriptions of the infraction?







# Submit your code and the output of your program. Submit assignment as a .txt, .py, .pdf, or jupyter notebook file.
# Due 24 hours before the live session in Week 4.

