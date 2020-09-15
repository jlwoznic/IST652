# Homework 2
# Author: Joyce Woznica
# Class: IST 652
###------------------- Import Packages ---------------------
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

###------------------- Read in Data ------------------------
# read a csv into a panda dataframe
# Rulings file
rulingsFile = "/Users/joycewoznica/Syracuse/IST652/Project/data/horse-racing-rulings-beginning-1985.csv"
rulingsDF = pd.read_csv(rulingsFile)

###---------- Review Data Structure, Data Clean-up ------------
# review structures
str(rulingsDF)
rulingsDF.shape
# 25068 rows and 7 columns

# get listing of all rows with a Fine Year <= 2008 (only interested in the last decade)
# also remove any 2020 infractions if they exist, since not a full year
indexNames = rulingsDF[rulingsDF['Fine Year'] <= 2008].index
rulingsDF.drop(indexNames, inplace=True)
rulingsDF.shape
# drops down to only 11,516 rows and 14 columns (removed 25284 rows)

# remove 2020 (since not yet over) from incidentDF
# Do we need to drop NaN or blanks
rulingsDF.isna().sum()
# drop the NaN notice date
rulingsDF = rulingsDF[rulingsDF['Notice Date'].notna()]

#----------------------- Question 1: Common Words ----------------------
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
# see what is in the final text
final_text_ruling[:500]

# must remove "nbsp" which is non-breaking space from wordcloud_text
# Attempt 1
stopwords = set(STOPWORDS)
stopwords.update(["is", "of", "nbsp", "for", "the", "a", "he", "you", "to", 
                  "in", "with", "are", "new", "york", "state", "will", "hereby",
                  "quot", "may"])
# need to remove all numbers
wordcloud_text = WordCloud(stopwords=stopwords, collocations=False, background_color="white", 
                           colormap = 'nipy_spectral',
                           prefer_horizontal = 0.85,
                           max_font_size= 30, max_words=175).generate(final_text_ruling)
# show the plot
plt.figure(figsize = (15,15))
plt.axis("off")
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title("Top 175 Most Common Words in Infraction Descriptions", fontsize = 16)
plt.show()
    
# Attempt 2
# add additional information to try to rule out certain words to find more details
stopwords.update(["is", "of", "nbsp", "for", "the", "a", "he", "you", "to", 
                  "in", "with", "are", "new", "york", "state", "will", "hereby",
                  "quot", "may", "race", "racing", "pari-mutuel",
                  "driving", "license", "participate", "fined", "hereby", "suspension",
                  "licensing", "failed", "horse", "requirements", "notified", "commission",
                  "racetrack", "receipt", "board", "comply", "day", "consideration",
                  "gaming", "wagering", "purse", "quot", "1st", "2nd", "3rd", "4th", "5th",
                  "6th", "7th", "8th", "invoice", "january", "february", "march", "april",
                  "may", "june", "july", "august", "september", "october", "november", "december",
                  "suspended", "days", "violation", "pari", "mutuel"])
# need to remove all numbers
wordcloud_text = WordCloud(stopwords=stopwords, collocations=False, background_color="white", 
                           colormap = 'nipy_spectral',
                           prefer_horizontal = 0.85,
                           max_font_size= 30, max_words=175).generate(final_text_ruling)
# show the plot
plt.figure(figsize = (15,15))
plt.axis("off")
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title("Top 175 Most Common Words in Infraction Descriptions", fontsize = 16)
plt.show()

# Attempt 3
# add additional information to try to rule out certain words to find more details
stopwords.update(["is", "of", "nbsp", "for", "the", "a", "he", "you", "to", 
                  "in", "with", "are", "new", "york", "state", "will", "hereby",
                  "quot", "may", "race", "racing", "pari-mutuel",
                  "driving", "license", "participate", "fined", "hereby", "suspension",
                  "licensing", "failed", "horse", "requirements", "notified", "commission",
                  "racetrack", "receipt", "board", "comply", "day", "consideration",
                  "gaming", "wagering", "purse", "quot", "1st", "2nd", "3rd", "4th", "5th",
                  "6th", "7th", "8th", "9th", "invoice", "january", "february", "march", "april",
                  "may", "june", "july", "august", "september", "october", "november", "december",
                  "suspended", "days", "violation", "pari", "mutuel", "reason", "respondent", 
                  "nycrr", "hearing", "appeal", "rule", "employee", "fine", "rules", "general", 
                  "right", "employ", "sunday", "monday", "tuesday", "wednesday", "thursday",
                  "friday", "saturday", "sunday", "generally", "mr", "person", 
                  "downs", "statement", "calendar"])
# need to remove all numbers
wordcloud_text = WordCloud(stopwords=stopwords, collocations=False, background_color="white", 
                           colormap = 'Dark2',
                           prefer_horizontal = 0.85,
                           max_font_size= 30, max_words=175).generate(final_text_ruling)
# show the plot
plt.figure(figsize = (15,15))
plt.axis("off")
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title("Top 175 Most Common Words in Infraction Descriptions", fontsize = 16)
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
explode_slices = (0.1, 0, 0, 0, 0.1, 0, 0, 0.1, 0, 0, 0, 0.1)
len(explode_slices)
# for colors
import random
import matplotlib.colors as mcolors
colors = random.choices(list(mcolors.CSS4_COLORS.values()),k = len(topwordDF))
plot = topwordDF.plot.pie(y='wordcount', figsize=(12, 12),
                          explode=explode_slices, 
                          shadow = True, colors = colors,
                          labels = topwordDF.index)
# Fix for this plot
plt.title("Top 12 Most Used Words in Infraction Descriptions", fontsize = 16)
plot.legend(loc="right", bbox_to_anchor = (1.2, 0.5), ncol = 1 )

#----------------------- Question: Check Tweets around the same Month --------
# duplicate the origin dataframe
wDaterulingsDF = rulingsDF.copy()

# remove rulings related to main office, etc. as traditionally just licensing issues
wDaterulingsDF = wDaterulingsDF[wDaterulingsDF['Race Track'] != "Main Office"]
wDaterulingsDF = wDaterulingsDF[wDaterulingsDF['Race Track'] != "New York Racing Association"]
wDaterulingsDF = wDaterulingsDF[wDaterulingsDF['Race Track'] != "none"]
wDaterulingsDF.shape

notice_date = wDaterulingsDF['Notice Date']
# now convert to a data frame - hoping for matching indices
ndateDF = pd.DataFrame(notice_date)

mdyDF = []
mdyDF = pd.DataFrame(columns=['Infraction Date', 'Year', 'Month', 'Day'])

# warning - this takes a while 
# convert date to different format and create Year, Month and Day columns
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
# get max and minimum infractions - determine where to cut off data frame for tweet lookup
min(arulingsbyMYT_DF.Infractions)
max(arulingsbyMYT_DF.Infractions)
# remove all but the highest number of infractions by track by year/month
arulingsbyMYT_DF = arulingsbyMYT_DF[arulingsbyMYT_DF.Infractions > 28]
top_list = len(arulingsbyMYT_DF.Infractions)
# reindex the top by track
arulingsbyMYT_DF = arulingsbyMYT_DF.set_index('Race Track')

#----------------------- Question 2 Continued: Read tweets --------------------------
# Import packages for tweets (be sure to start Mongo DB)
import tweepy as tw
import json
import sys
import os
import pymongo
import pandas as pd

# Twitter Keys for API
CONSUMER_KEY = 'NeMSryEx2Uc6YFi8t74fHsFNe'
CONSUMER_SECRET = 'XlzCSmkKQM2OhrfO9r10p9fWNRNB1W2Qd8fLOHo0VcCET0ELqM'
OAUTH_TOKEN = '1259973954166456320-b5xXXSu7WUfTVLEjhXagRvYF6wzmiL'
OAUTH_SECRET = 'G3AbUXGLUEcobVTeJYlAzz29uiTQIKchSUfb1rVUFgoHI'

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

# db_fns - courtesy of Dr. D. Landowski
# This function either starts or adds to an existing database and collection in Mongo
# Parameters:  
#   data - this should be a list of json objects, where each will be a collection element
#      in the DB stored under a unique ID key created by Mongo
#   DBname - the name of the database, either new or existing
#   DBcollection - the name of the collection, either new or existing
def save_to_DB (DBname, DBcollection, data):
    # connect to database server and just let connection errors fail the program
    client = pymongo.MongoClient('localhost', 27017)
    # save the results in a database collection
    #   change names to lowercase because they are not case sensitive
    #   and remove special characters like hashtags and spaces (other special characters may also be forbidden)
    DBname = DBname.lower()
    DBname = DBname.replace('#', '')
    DBname = DBname.replace(' ', '')
    DBcollection = DBcollection.lower()
    DBcollection = DBcollection.replace('#', '')
    DBcollection = DBcollection.replace(' ', '')

    # use the DBname and collection, which will create if not existing
    db = client[DBname]
    collection = db[DBcollection]   
        
    # add the data to the database
    collection.insert_many(data)
    print("Saved", len(data), "documents to DB collection", DBname, DBcollection)

# This function gets data from an existing DB and collection
# Parameters:  
#   DBname and DBcollection- the name of the database and collection, either new or existing
# Result:
#   data - returns all the data in the collection as a list of JSON objects
def load_from_DB (DBname, DBcollection):
    # connect to database server and just let connection errors fail the program
    client = pymongo.MongoClient('localhost', 27017)
    # use the DBname and collection, which will create if not existing
    db = client[DBname]
    collection = db[DBcollection]    
        
    # get all the data from the collection as a cursor
    docs = collection.find()
    #  convert the cursor to a list
    docs_bson = list(docs)
    docs_json_str = [dumps(doc) for doc in docs_bson]
    docs_json = [json.loads(doc) for doc in docs_json_str]
    return docs_json

# Simple search using tweepy
# result_tweets = simple_search(api, query, max_results=num_tweets)
def simple_search(api, query, since, until, max_results=500):
  # the first search initializes a cursor, stored in the metadata results,
  #   that allows next searches to return additional tweets
  #search_results = [status for status in tw.Cursor(api.search, q=query).items(max_results)]
  search_results = tw.Cursor(api.search,
                             q=search_words,
                             lang="en",
                             since=date_since,
                             until=date_until).items(max_results)
  
  # for each tweet, get the json representation
  tweets = [tweet._json for tweet in search_results]
  return tweets

# tie all these together for a single call to all functions
def run_simple_tweet_search(query, num_tweets, since, until, DBname, DBcollection):
    # api = oauth_login()
    ''' if needed switch to using the appauth login to avoid rate limiting '''
    #api = appauth_login()
    api = tw.API(auth, wait_on_rate_limit=True)

    print ("Twitter Authorization: ", api)
    
    # access Twitter search
    result_tweets = simple_search(api, query, since, until, max_results=num_tweets)
    tot_results = len(result_tweets)
    print ('Number of result tweets: ', len(result_tweets))

    # save the results in a database collection
    #   change names to lowercase because they are not case sensitive
    #   and remove special characters like hashtags and spaces (other special characters may also be forbidden)
    DBname = DBname.lower()
    DBname = DBname.replace('#', '')
    DBname = DBname.replace(' ', '')
    DBcollection = DBcollection.lower()
    DBcollection = DBcollection.replace('#', '')
    DBcollection = DBcollection.replace(' ', '')
    
    # use the save and load functions in this program
    # in this, we do not want any retweeted tweets - only originals
    if tot_results > 0:
        save_to_DB(DBname, DBcollection, result_tweets)
    # Done!

#-------------------------- Run Tweets -----------------------------
# Set common variables for runs
tweets_to_return = 200
dbname = "racedb"
collname = "racecoll"

# 1st pass - Finger Lakes August 2012
# need to make the search_words a list and process through them 
search_wordsList = ["@FLGaming", "#FingerLakesRaceTrack", "@racingwrongs", "@HR_Nation", 
                    "@TheNYRA", "@NYSGamingComm", "@NYRBets", "@SireStakesNY", "@Equibase"]
date_since = "2012-08-01"
date_until = "2012-08-30"

# Using for loop 
for search_words in search_wordsList: 
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)
# no tweets for any of the list for the FingerLakes 8/2012

# 2nd pass - Yonkers Raceway August 2015
search_wordsList = ["@YonkersRaceway", "#YonkersRaceway", "@racingwrongs", "@HR_Nation", 
                    "@TheNYRA", "@NYSGamingComm", "@NYRBets", "@trotinsider", "#harnessracing"]
date_since = "2015-08-01"
date_until = "2015-08-30"

for search_words in search_wordsList:
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)
# no tweets for this timeperiod either

# 3rd pass - Yonkers Raceway May 2016
search_wordsList = ["@YonkersRaceway", "#YonkersRaceway", "@racingwrongs", "@HR_Nation", 
                    "@TheNYRA", "@NYSGamingComm", "@NYRBets", "@trotinsider", "#harnessracing"]
date_since = "2016-05-01"
date_until = "2016-05-31"

for search_words in search_wordsList:
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)
# again no tweets

# 4th pass - Saratoga Raceway November 2012
search_wordsList = ["@SaratogaNYRA", "#saratogaraceway", "@racingwrongs", "@HR_Nation", 
                    "@TheNYRA", "@NYSGamingComm", "@NYRBets", "@trotinsider", "#harnessracing"]
date_since = "2012-11-01"
date_until = "2012-11-31"

for search_words in search_wordsList:
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)
# again no tweets
    
# 5th Pass - Yonkers Raceway August 2012
search_wordsList = ["@YonkersRaceway", "#YonkersRaceway", "@racingwrongs", "@HR_Nation", 
                    "@TheNYRA", "@NYSGamingComm", "@NYRBets", "@trotinsider", "#harnessracing"]
date_since = "2012-08-01"
date_until = "2012-08-30"

for search_words in search_wordsList:
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)
# no tweets for this timeperiod either

# 6th Pass - Yonkers Raceway June 2013
search_wordsList = ["@YonkersRaceway", "#YonkersRaceway", "@racingwrongs", "@HR_Nation", 
                    "@TheNYRA", "@NYSGamingComm", "@NYRBets", "@trotinsider", "#harnessracing"]
date_since = "2013-06-01"
date_until = "2013-06-30"

for search_words in search_wordsList:
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname) 

# Assuming they were "late to twitter" - will just run 1/2019 through present day
# so - just ran tweets on all racetracks and the common hashtags and users
# Final Attempt
import time
import datetime
date_since = "2019-01-01"
date_until = time.strftime("%Y-%m-%d")
search_wordsList = ["#aqueductracetrack", "@BDRacetrack", "#belmontpark", "@BelmontStakes", 
                    "@BufffaloRaceway", "#buffaloraceway", "@FLGaming", "#fingerlakesracetrack", 
                    "#monticelloraceway", "@gotiogadowns", "#tiogadowns", "@governondowns", 
                    "#vernondowns", "@YonkersRaceway", "#yonkersraceway", "@racingwrongs", 
                    "@HR_Nation", "@TheNYRA", "@NYSGamingComm", "@NYRBets", 
                    "@trotinsider", "#harnessracing", "@Equibase"]

for search_words in search_wordsList:
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)

# build a database of just the last 1000 tweets from racingwrongs
tweets_to_return = 750
search_wordsList = ["@racingwrongs"]

# put them in their own database and collection
dbname = "racewrongdb"
collname = "racewrongcoll"

for search_words in search_wordsList:
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)

# Get Tweet_List for building pandas dataframe - build one for each tweet_list
# for racedb
client = pymongo.MongoClient('localhost', 27017)
db = client.racedb
coll = db.racecoll
# Get tweets
tweets = coll.find()
# Create list of tweets - tweet_list
tweet_list = [tweet for tweet in tweets]

# same for racing wrongs
# Get Tweet_List for building pandas dataframe
db = client.racewrongdb
coll = db.racewrongcoll
# Get tweets
tweets = coll.find()
# Create list of tweets - rwtweet_list
rwtweet_list = [tweet for tweet in tweets]

# Convert previously selected fields into a pandas dataframe for analysis
def tweets_to_pd(tweets):
    df = pd.DataFrame()
    for tweet in tweets:
        if not tweet['entities'].get('media') is None:
            for m in tweet['entities'].get('media'):
                content_type =  m.get('type')
        else:
            content_type = "None"
        data = {'id':str(tweet['id'])
               ,'user':tweet['user']['name']
               ,'text':tweet['text']
               ,'Timestamp': tweet['created_at']
               ,'location':tweet['user']['location']
               ,'content type':content_type
               ,'favorites':tweet['favorite_count']
               ,'retweets':tweet['retweet_count']
              }
        # remove retweets
        if not(tweet['text'].startswith('RT')):
            df = df.append(data,ignore_index=True)
    return df

tweets_DF = tweets_to_pd(tweet_list)
# need to remove every row that has rt > 0
#tweets_DF = tweets_DF[tweets_DF['retweets'] == 0]

rwrong_DF = tweets_to_pd(rwtweet_list)
#rwrong_DF = rwrong_DF[rwrong_DF['retweets'] == 0]

# then redo the cloud on the tweets_pd
# should "functionize" this, but ran out of time - def prep_for_wc
#-------------------------- Run Wordcloud: racing accounts and hashtags ----------------
tweets_DF['text'].isnull().sum()
# none, so we can continue

# subset out just the text about the ruling
tweetDF = tweets_DF['text']
tweetDF = tweetDF.to_frame()

# convert all to lower case
tweetDF['text'] = tweetDF['text'].str.lower()

# grab all text together
all_tweets = tweetDF['text'].str.split(' ')
all_tweets.head()

# create blank dataframe for individual words
all_tweets_nopunc = []

for tweet in all_tweets:
    tweet = [x.strip(string.punctuation) for x in tweet]
    all_tweets_nopunc.append(tweet)

all_tweets_nopunc[0]
tweet_ruling = [" ".join(tweet) for tweet in all_tweets_nopunc]

final_tweet_ruling = " ".join(tweet_ruling)
# see what is in the final text
final_tweet_ruling[:500]

# set stopwords
stopwords = set(STOPWORDS)
stopwords.update(["rt"])

# plot wordcloud
wordcloud_text = WordCloud(stopwords=stopwords, collocations=False, background_color="white", 
                           colormap = 'ocean',
                           prefer_horizontal = 0.85,
                           max_font_size= 30, max_words=175).generate(final_tweet_ruling)
# show the plot
plt.figure(figsize = (15,15))
plt.axis("off")
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title("Top 175 Most Common Words in Tweets about Racing since January 2019", fontsize = 16)
plt.show()

# clean up by removing some account names           
# Massage the stopwords
stopwords.update(["rt", "https", "ejxd2", "hf6y7ysgeg", "co"])
# plot wordcloud
wordcloud_text = WordCloud(stopwords=stopwords, collocations=False, background_color="white", 
                           colormap = 'ocean',
                           prefer_horizontal = 0.85,
                           max_font_size= 30, max_words=175).generate(final_tweet_ruling)
# show the plot
plt.figure(figsize = (15,15))
plt.axis("off")
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title("Top 175 Most Common Words in Tweets about Racing since January 2019", fontsize = 16)
plt.show()                 
         
# clean up again by removing all the different tracks            
stopwords.update(["rt", "https", "ejxd2", "hf6y7ysgeg", "co", "thenyra", "nysgamingcomm",
                  "equibase", "hr_nation", "nyrabets", "racingwrongs", "amp", "thenyra"])

# plot wordcloud
wordcloud_text = WordCloud(stopwords=stopwords, collocations=False, background_color="white", 
                           colormap = 'ocean',
                           prefer_horizontal = 0.85,
                           max_font_size= 30, max_words=175).generate(final_tweet_ruling)
# show the plot
plt.figure(figsize = (15,15))
plt.axis("off")
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title("Top 175 Most Common Words in Tweets about Racing since January 2019", fontsize = 16)
        
#---------------------------- Wordcloud for racingwrongs ----------------------   
# repeat (as mentioned - need to make a function) for racingwrongs
# then redo the cloud on the tweets_pd
# should "functionize" this, but ran out of time
rwrong_DF['text'].isnull().sum()
# none, so we can continue

# subset out just the text about the ruling
rwrongDF = rwrong_DF['text']
rwrongDF = rwrongDF.to_frame()

# convert all to lower case
rwrongDF['text'] = rwrongDF['text'].str.lower()

# grab all text together
all_tweets = rwrongDF['text'].str.split(' ')
all_tweets.head()

# create blank dataframe for individual words
all_tweets_nopunc = []

for tweet in all_tweets:
    tweet = [x.strip(string.punctuation) for x in tweet]
    all_tweets_nopunc.append(tweet)

all_tweets_nopunc[0]
tweet_ruling = [" ".join(tweet) for tweet in all_tweets_nopunc]

final_tweet_ruling = " ".join(tweet_ruling)
# see what is in the final text
final_tweet_ruling[:500]

# set stopwords
stopwords = set(STOPWORDS)
stopwords.update(["rt", "https", "co", "oyq9jtw09s", "raypowe94432684", "racingwrongs","via",
                  "hejtkjhpvh", "lisakayemundy", "k7ig8vveut", "britneyeurton", "amp", 
                  "mkn8gn9ank", "f5clpn9jka", "ndbig7ajnb", "mknBgn9ank", "xzayamkox2",
                  "robbiesaunders0", "yvsavh7aje", "lvzz1asvvo", "angelagirl7777",
                  "x00rwydr17", "alameda140", "xdevtgq4s3", "cc88mksaee", "6zsgbfb17w",
                  "fvjhhqpjfp", "uuyzyamb1y", "vi40kbw5zs", "ae8sz18udm", "xdevtfq4s3",
                  "cr2dup8uqt", "kyyxa1nbrk", "eacnoqukukd", "tddifi8ryb", "y1q0hkb1kh"])

# plot wordcloud
wordcloud_text = WordCloud(stopwords=stopwords, collocations=False, background_color="black", 
                           colormap = 'Accent',
                           prefer_horizontal = 0.85,
                           max_font_size= 30, max_words=175).generate(final_tweet_ruling)
# show the plot
plt.figure(figsize = (15,15))
plt.axis("off")
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title("Top 175 Most Common Words from @racingwrongs since January 2019", fontsize = 16)
plt.show()
                 
