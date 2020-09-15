# Homework 3
# Author: Joyce Woznica
# Class: IST 652
###----------  Import Packages ------------
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import datetime as dt

# packages for wordclouds
# note - must install wordcloud
# conda install -c conda-forge wordcloud
import string
import collections
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from colour import Color

###---------- Read in Data ------------
# read a csv into a panda dataframe
# Rulings file
rulingsFile = "/Users/joycewoznica/Syracuse/IST652/Project/data/horse-racing-rulings-beginning-1985.csv"
# Death and Breakdown File
incidentFile = "/Users/joycewoznica/Syracuse/IST652/Project/data/Equine_Death_and_Breakdown.csv"

rulingsDF = pd.read_csv(rulingsFile)
incidentDF = pd.read_csv(incidentFile)

###---------- Review Structures and Data Clean-up ------------
# review structures
str(rulingsDF)
rulingsDF.shape
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
# drop the NaN notice date
rulingsDF = rulingsDF[rulingsDF['Notice Date'].notna()]

#----------------------- Question 1: Common Words ----------------------
# can we do something to root words???
#Checking for null values in `description`
rulingsDF['Ruling Text'].isnull().sum()
# none, so we can continue

# subset out just the text about the ruling
textDF = rulingsDF['Ruling Text']
textDF = textDF.to_frame()

# convert all to lower case
textDF['Ruling Text'] = textDF['Ruling Text'].str.lower()

# grab all text together
all_text = textDF['Ruling Text'].str.split(' ')
all_text.head()

# create blank dataframe for individual words
all_text_nopunc = []

for text in all_text:
    text = [x.strip(string.punctuation) for x in text]
    all_text_nopunc.append(text)

all_text_nopunc[0]
text_ruling = [" ".join(text) for text in all_text_nopunc]

final_text_ruling = " ".join(text_ruling)
final_text_ruling[:500]

# must remove "nbsp" which is non-breaking space from wordcloud_text
stopwords = set(STOPWORDS)
# doesn't seem to be updating
stopwords.update(["is", "of", "nbsp", "for", "the", "a", "he", "you", "to", 
                  "in", "with", "are", "new", "york", "state", "will", "hereby",
                  "quot", "may"])
    
stopwords.update(["is", "of", "nbsp", "for", "the", "a", "he", "you", "to", 
                  "in", "with", "are", "new", "york", "state", "race", "racing",
                  "driving", "license", "participate", "fined", "hereby", "suspension",
                  "licensing", "failed", "horse", "requirements", "notified", "commission",
                  "racetrack", "receipt", "board", "comply", "day", "consideration",
                  "gaming", "wagering", "purse", "quot", "1st", "2nd", "3rd", "4th", "5th",
                  "6th", "7th", "8th", "invoice", "january", "february", "march", "april",
                  "may", "june", "july", "august", "september", "october", "november", "december",
                  "suspended", "days", "violation", "pari", "mutuel"])
# need to remove all numbers
wordcloud_text = WordCloud(stopwords=stopwords, collocations=False, background_color="white", 
                           colormap = 'Dark2',
                           prefer_horizontal = 0.85,
                           max_font_size= 30, max_words=175).generate(final_text_ruling)
# show the plot
plt.figure(figsize = (15,15))
plt.axis("off")
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title("Top 175 Most Common Words in Infractions Descriptions", fontsize = 16)
plt.show()

# Different representation of top words in pie graph (remove numbers)
filtered_text_ruling = [word for word in final_text_ruling.split() if word not in stopwords]
counted_word_ruling = collections.Counter(filtered_text_ruling)

word_count_ruling = {}

for letter, count in counted_word_ruling.most_common(20):
    if not (letter.isnumeric()):
        word_count_ruling[letter] = count
    
topwordDF = pd.DataFrame.from_dict(word_count_ruling, orient='index', columns = ['wordcount'])
len(topwordDF)
explode_slices = (0, 0.1, 0, 0.1, 0, 0.1, 0, 0, 0, 0, 0, 0,)
len(explode_slices)
red = Color("red")
colors = np.array(list(red.range_to(Color("green"),17)))
#fig1, ax1 = plt.subplots()
#ax1.pie(wordcount, explode=explode_slices, labels = )
#wdcnt = topwordDF['wordcount']
#word = topwordDF['index']

plot = topwordDF.plot.pie(y='wordcount', figsize=(12, 12),
                          explode=explode_slices, 
                          shadow = False,
                          labels = topwordDF.index)
# Fix for this plot
plt.title("Top 20 Most Used Words in Infraction Descriptions", fontsize = 16)
plot.legend(loc="right", bbox_to_anchor = (1.2, 0.5), ncol = 1 )

#----------------------- Question: Change date to month/year and use Fine Year as Year --------
# duplicate the origin dataframe
wDaterulingsDF = rulingsDF.copy()

# try another way
wDaterulingsDF = wDaterulingsDF[wDaterulingsDF['Race Track'] != "Main Office"]
wDaterulingsDF = wDaterulingsDF[wDaterulingsDF['Race Track'] != "New York Racing Association"]
wDaterulingsDF = wDaterulingsDF[wDaterulingsDF['Race Track'] != "none"]
wDaterulingsDF.shape

notice_date = wDaterulingsDF['Notice Date']
# now convert to a data frame - hoping for matching indices
ndateDF = pd.DataFrame(notice_date)

mdyDF = []
mdyDF = pd.DataFrame(columns=['Infraction Date', 'Year', 'Month', 'Day'])

for value in ndateDF['Notice Date']:
    # split out date
    yy = int(value[0:4])
    mm = int(value[5:7])
    dd = int(value[8:10])
    # convert date for new Infraction Date
    infdate = dt.datetime(yy, mm, dd).strftime('%m/%d/%Y')
    # convert month
    month = dt.date(yy, mm, dd).strftime('%B')
    mdyDF = mdyDF.append(pd.DataFrame({'Infraction Date': [infdate],
                           'Year': [yy],
                           'Month': [month],
                           'Day': [dd]}))

# reset the index properly
mdyDF = mdyDF.reset_index()
# remove bad index
mdyDF = mdyDF.drop(['index'], axis=1)

# need to add the columns from the other 
wDaterulingsDF['Month'] = mdyDF['Month']
wDaterulingsDF['Day'] = mdyDF['Day']
# not really necessary as we have Fine Year, but just in case there wasn't a fine
wDaterulingsDF['Infraction Date'] = mdyDF['Infraction Date']

# Now see which month in each year has the most infractions by racetrack
# after that - we check twitter to see if there is any tweets that month (+/- 5 days)
rulingsbyMYT_DF = wDaterulingsDF.groupby(['Fine Year', 'Month', 'Race Track'])
rulingsbyMYT_DF.groups
# now need to sum each by count racetrack for each year/month
# need something around value_counts()
arulingsbyMYT_DF = rulingsbyMYT_DF.size()
# This is what we need to graph by track, but need to do that stacking and reindexing
# reset index
arulingsbyMYT_DF = arulingsbyMYT_DF.reset_index()
# drop the Fine Year column
# rename the columns
arulingsbyMYT_DF.columns = ['Year', 'Month', 'Race Track', 'Infractions']
arulingsbyMYT_DF['Race Track'].unique()

# sort by descending infractions
arulingsbyMYT_DF = arulingsbyMYT_DF.sort_values(['Infractions', 'Race Track', 'Year', 'Month'],
                                                ascending=(False, True, True, True))
len(arulingsbyMYT_DF.Infractions)
# get max and minimum infractions
min(arulingsbyMYT_DF.Infractions)
max(arulingsbyMYT_DF.Infractions)
# remove all but the highest number of infractions by track by year/month
arulingsbyMYT_DF = arulingsbyMYT_DF[arulingsbyMYT_DF.Infractions > 30]
top_list = len(arulingsbyMYT_DF.Infractions)
# reindex the top by track?
arulingsbyMYT_DF = arulingsbyMYT_DF.set_index('Race Track')
# grab the top line and check tweets
# Just do by hand

#----------------------- Question 3: Read tweets from a few accounts --------------------------
# Do a word cloud or a bar graph of most used words 



#----------------------- Question 3: Check Type ------------------------
# maybe do something around the Type: Fine, Suspension, Fine & Suspension, etc
rulingsDF['Type'].unique()

# maybe look for correlation bewteen text and type of ruling

#----------------------- Question 4: Merge the files by -----------------
#------------------------            Notice Date = Incident Date --------
#------------------------            Race Track = Track -----------------

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

ry 

# merge the dataframes
merged_df = DF2.merge(DF1, how = 'inner', on = ['date', 'hours'])