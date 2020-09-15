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
rulingsDF = pd.read_csv(rulingsFile)

###---------- Review Structures and Data Clean-up ------------
# review structures
str(rulingsDF)
rulingsDF.shape
# reveals 36790 rows with 14 columns (data needs to only include 2009-2019)

# Remove unwanted years from dataframe
# get listing of all rows with a Fine Year <= 2008 (only interested in the last decade)
# also remove any 2020 infractions if they exist, since not a full year
indexNames = rulingsDF[rulingsDF['Fine Year'] <= 2008].index
rulingsDF.drop(indexNames, inplace=True)
rulingsDF.shape

# Do we need to drop NaN or blanks
rulingsDF.isna().sum()
# FIX THIS!!!
rulingsDF.replace(to_replace='0MAR MEHIDI', value='OMAR MEHIDI')
rulingsDF.isin(['0MAR MEHIDI']).any()
# - missing Rules or Notice Date is fine, so no NA removal required
# blank rules are okay - they imply that a license was denied, so no specific rule was broken

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
fg = sns.catplot(x = "TrackName", y = "Infractions", hue = "TrackName", dodge=False,
                    height = 5, aspect = 2, palette="Spectral", kind="bar", data=rulingsDFbyTrack)
fg.set_xticklabels(rotation=45, horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'medium')
fg.set(xlabel = "Race Track", ylabel = "Number of Infractions", title = "Infractions by Race Track from 2009 - 2019")
            
###---------- Analysis: Question 2 ------------
# Question 2: Are there more infractions in Harness or TB Racing?
# count infractions by Race Type
rulingsDFbyType = rulingsDF['Race Type'].value_counts()
rulingsDFbyType = rulingsDFbyType.to_frame()
rulingsDFbyType.columns = ['Infractions']
# Need to remove blanks
rulingsDFbyType.isna()
rulingsDFbyType = rulingsDFbyType.drop(['?'])
# add column of race types for plotting
RaceTypes = rulingsDFbyType.index.values
rulingsDFbyType['RaceType'] = RaceTypes

# plot with seaborn
fg = sns.catplot(x = "RaceType", y = "Infractions", hue = "RaceType", dodge=False,
                    height = 3, aspect = 2, palette="Set1", kind="bar", data=rulingsDFbyType)
#fg.set_title("Infractions by Race Track")
fg.set_xticklabels(horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'medium')
fg.set(xlabel = "Race Type", ylabel = "Number of Infractions", title = "Infractions by Race Type from 2009 - 2019")

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
# add column of race types for plotting
FullNames = rulingsDFbyName.index.values
rulingsDFbyName['FullName'] = FullNames
shortrulingsDFbyName = rulingsDFbyName.head(25)

# plot with seaborn
fg = sns.catplot(x = "FullName", y = "Infractions", hue = "FullName", dodge=False,
                    height = 6, aspect = 2, palette="Spectral", kind="bar", data=shortrulingsDFbyName)
fg.set_xticklabels(rotation = 45, horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'medium')
fg.set(xlabel = "Full Name", ylabel = "Number of Infractions", title = "Infractions by Individual from 2009 - 2019")

###---------- Analysis: Question 4 ------------
# Question 4: What occupation has the most infractions?
# cannot count this - come up with a better way to do this!
rulingsDFbyOccupation = rulingsDF['Occupation'].value_counts() 
rulingsDFbyOccupation = rulingsDFbyOccupation.to_frame()
Occupations = rulingsDFbyOccupation.index.values
rulingsDFbyOccupation.columns = ['Infractions']
# Need to remove blanks
rulingsDFbyOccupation.isna().sum()
Occupations = rulingsDFbyOccupation.index.values
rulingsDFbyOccupation['Occupation'] = Occupations
shortrulingsDFbyOccupation = rulingsDFbyOccupation.head(25)

# plot with seaborn
fg = sns.catplot(x = "Occupation", y = "Infractions", hue = "Occupation", dodge=False,
                    height = 6, aspect = 2, palette="RdBu", kind="bar", data=shortrulingsDFbyOccupation)
fg.set_xticklabels(rotation = 45, horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'medium')
fg.set(xlabel = "Occupation", ylabel = "Number of Infractions", title = "Infractions by Occupation from 2009 - 2019")

###---------- Analysis: Question 5 ------------
# Question 5: Track infractions over the years
# gather data by track and by year and then do something to calculate the values of both
str(rulingsDFbyTrack)
print(rulingsDFbyTrack.columns)
byTrackbyYear = pd.crosstab(rulingsDF['Race Track'], rulingsDF['Fine Year'])
# rows are tracks, but columns are years - need to create column renames
# Need to drop Main Office
# Maybe just drop none?
byTrackbyYear = byTrackbyYear.drop(['Main Office', 'none', 'New York Racing Association'])

# column names
print(byTrackbyYear.columns)
print(list(byTrackbyYear.columns))
# row names
print(byTrackbyYear.index.values)
# Change the index to the year
byTrackbyYear = byTrackbyYear.transpose()
byTrackbyYear['FineYear'] = byTrackbyYear.index.values
melted_byTrackbyYear = pd.melt(byTrackbyYear, id_vars = "FineYear", var_name = "TrackName", value_name = "Infractions")

# need to do this a line plot by column (track) and then different color for each track
plt.rcParams['figure.figsize']=8,6
ax = plt.gca()
g = sns.lineplot(x = 'FineYear', y = 'Infractions', hue="TrackName", style = "TrackName", dashes = False, 
             legend = "full", marker = 'o', palette = "Dark2", data = melted_byTrackbyYear)
plt.title("Infractions by Fine Year by Race Track from 2009 - 2019", fontsize = 12)
plt.xlabel("Fine Year", fontsize = 10)
plt.ylabel("Infractions", fontsize = 10)
g.legend(loc="right", bbox_to_anchor = (1.6, 0.5), ncol = 1 )
l = np.arange(2009, 2020, 1)
ax.set(xticks=l, xticklabels = l)

###---------- Analysis: Question 6 -----------
# Question 6: What is the Total Fine by Individual/Occupation
# Maybe redo this with fines between certain values
# 0 - 1000, 1001 - 2000, 2001 - 3000, 3001 - 4000, 4001 - 5000, etc.
rulingsDFbyFNO = rulingsDF.groupby(['Full Name', 'Occupation'])
tFinesbyFNO = rulingsDFbyFNO.sum()

# reset index
tFinesbyFNO = tFinesbyFNO.reset_index()
# drop the Fine Year column
tFinesbyFNODF = tFinesbyFNO.drop(['Fine Year'], axis=1)
# rename the columns
tFinesbyFNODF.columns = ['FullName', 'Occupation', 'TotalFines']

# need to sort by descending Fine
tFinesbyFNODF = tFinesbyFNODF.sort_values(["FullName", "Occupation", "TotalFines"], ascending =(True, True, False))
# remove all Fines smaller fines to get a more manageable grouping
min(tFinesbyFNODF.TotalFines)
max(tFinesbyFNODF.TotalFines)
tFinesbyFNODF = tFinesbyFNODF[tFinesbyFNODF.TotalFines >= 4000]
# sort by total fine?
tFinedbyFNODF = tFinesbyFNODF.sort_values(["TotalFines"], ascending=(False))
# Do bar graph by person and a different color bar for each occupation w/i person
# plot with seaborn
fg = sns.catplot(x = "FullName", y = "TotalFines", hue = "Occupation", dodge=False,
                    height = 6, aspect = 2, palette="Dark2", kind="bar", data=tFinesbyFNODF)
fg.set_xticklabels(rotation = 45, horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'small')
fg.set(xlabel = "Occupation", ylabel = "Total Fines", title = "Total Fines by Individual/Occupation from 2009 - 2019")

# drop out Luis Pena
tFinesbyFNODF = tFinesbyFNODF[tFinesbyFNODF.FullName != "LUIS PENA"]
# replot without Outlier
# plot with seaborn
fg = sns.catplot(x = "FullName", y = "TotalFines", hue = "Occupation", dodge=False,
                    height = 6, aspect = 2, palette="Dark2", kind="bar", data=tFinesbyFNODF)
fg.set_xticklabels(rotation = 45, horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'small')
fg.set(xlabel = "Occupation", ylabel = "Total Fines", title = "Total Fines by Individual/Occupation from 2009 - 2019")

###---------- Analysis: Question 7 ------------
# Question 6: Average Fine by Occupation
# Struggling with this one
rulingsDFbyOcc = rulingsDF.groupby(['Occupation', 'Full Name'])
aFinebyFNOcc = rulingsDFbyOcc.mean()

# reset index
aFinebyFNOcc = aFinebyFNOcc.reset_index()
# drop the Fine Year column
aFinebyFNOccDF = aFinebyFNOcc.drop(['Fine Year'], axis=1)
# rename the columns
#aFinebyFNOccDF.columns = ['FullName', 'Occupation', 'AvgFine']
avgFinebyOcc = aFinebyFNOccDF.groupby(["Occupation"])
avgFinebyOccDF = avgFinebyOcc.mean()
# set a column for occupation
avgFinebyOccDF['Occupation'] = avgFinebyOccDF.index.values

# round to 2 decimal places
avgFinebyOccDF = avgFinebyOccDF.round({"Fine Amount":2})
avgFinebyOccDF.columns = ['AvgFine', 'Occupation']
# need to sort by descending Fine
avgFinebyOccDF = avgFinebyOccDF.sort_values(["AvgFine"], ascending=(False))
min(avgFinebyOccDF.AvgFine)
max(avgFinebyOccDF.AvgFine)
# remove all fines under $50
avgFinebyOccDF = avgFinebyOccDF[avgFinebyOccDF.AvgFine > 50]

# Do bar graph by person and a different color bar for each occupation w/i person
# plot with seaborn
fg = sns.catplot(x = "Occupation", y = "AvgFine", hue = "Occupation", dodge=False,
                    height = 6, aspect = 3, palette="Spectral", kind="bar", data=avgFinebyOccDF)
fg.set_xticklabels(rotation = 80, horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'small')
fg.set(xlabel = "Occupation", ylabel = "Average Fine in USD", title = "Average Fine by Occupation from 2009-2019")

# drop out Luis Pena
avgFinebyOccDF = avgFinebyOccDF[avgFinebyOccDF.Occupation != "JOCKEY AGENT"]

# plot with seaborn
fg = sns.catplot(x = "Occupation", y = "AvgFine", hue = "Occupation", dodge=False,
                    height = 6, aspect = 3, palette="Spectral", kind="bar", data=avgFinebyOccDF)
fg.set_xticklabels(rotation = 80, horizontalalignment = 'right', 
                         fontweight = 'light', fontsize = 'small')
fg.set(xlabel = "Occupation", ylabel = "Average Fine in USD", title = "Average Fine by Occupation from 2009-2019")

# Submit your code and the output of your program. Submit assignment as a .txt, .py, .pdf, or jupyter notebook file.
# Due 24 hours before the live session in Week 4.

