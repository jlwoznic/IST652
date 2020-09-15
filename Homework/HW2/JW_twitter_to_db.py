# Homework 2
# Author: Joyce Woznica
# Class: IST 652
###----------  Import Packages ------------

# Try elimating other code and running this alone with the databases - make sure
# that database will keep filling as new searches are run

import tweepy as tw
import json
import sys
import os
import pymongo
import pandas as pd

#import bson.json_util import dumps

CONSUMER_KEY = 'NeMSryEx2Uc6YFi8t74fHsFNe'
CONSUMER_SECRET = 'XlzCSmkKQM2OhrfO9r10p9fWNRNB1W2Qd8fLOHo0VcCET0ELqM'
OAUTH_TOKEN = '1259973954166456320-b5xXXSu7WUfTVLEjhXagRvYF6wzmiL'
OAUTH_SECRET = 'G3AbUXGLUEcobVTeJYlAzz29uiTQIKchSUfb1rVUFgoHI'

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

# db_fn
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

'''
  Uses the tweepy Cursor to wrap a twitter api search for the query string
    Returns json formatted results
'''

def simple_search(api, query, since, until, max_results=500):
  # the first search initializes a cursor, stored in the metadata results,
  #   that allows next searches to return additional tweets
  #search_results = [status for status in tw.Cursor(api.search, q=query).items(max_results)]
  # q = search_words
  print(query)
  search_results = tw.Cursor(api.search,
                             q=search_words,
                             lang="en",
                             since=date_since,
                             until=date_until).items(max_results)
  
  # for each tweet, get the json representation
  tweets = [tweet._json for tweet in search_results]
  return tweets

# how to run above
# result_tweets = simple_search(api, query, max_results=num_tweets)
# print ('Number of result tweets: ', len(result_tweets))
def run_simple_tweet_search(query, num_tweets, since, until, DBname, DBcollection):
    # api = oauth_login()
    ''' if needed switch to using the appauth login to avoid rate limiting '''
    #api = appauth_login()
    api = tw.API(auth, wait_on_rate_limit=True)

    print ("Twitter Authorization: ", api)
    
    # access Twitter search
    result_tweets = simple_search(api, query, since, until, max_results=num_tweets)
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
    #if len(result_tweets) != 0:
    save_to_DB(DBname, DBcollection, result_tweets)

# run tweets
# could use this to loop through dates (+/- 5 days), track and db and collection
# need to make the search_words a list and process through them 
# 1st pass - Finger Lakes August 2012
tweets_to_return = 200
search_wordsList = ["@FLGaming", "#FingerLakesRaceTrack", "@racingwrongs", "@HR_Nation", 
                    "@TheNYRA", "@NYSGamingComm", "@NYRBets", "@SireStakesNY", "#COVID19"]
search_wordsList = ["#COVID19"]
date_since = "2020-04-01"
date_until = "2020-04-30"
dbname = "racedb"
collname = "racecoll"

# Using for loop 
for value in search_wordsList: 
    print(value) 
    run_simple_tweet_search(value, tweets_to_return, date_since, date_until, dbname, collname)
# no tweets for any of the list for the FingerLakes 8/2012

# 2nd pass - Yonkers Raceway August 2015
tweets_to_return = 200
search_wordsList = ["@YonkersRaceway", "#YonkersRaceway", "@racingwrongs", "@HR_Nation", 
                    "@TheNYRA", "@NYSGamingComm", "@NYRBets", "@trotinsider", "#harnessracing"]
date_since = "2015-08-01"
date_until = "2015-08-30"
dbname = "racedb"
collname = "racecoll"

# Using for loop 
for search_words in search_wordsList: 
    print(search_words) 
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)    
    
# since client called within a function - redefine
client = pymongo.MongoClient('localhost', 27017)
# set db variable to our database
db = client.racedb
coll = db.racecoll
# Get tweets
tweets = coll.find()
# Create list of tweets - maybe not necessary if in dataframe
tweet_list = [tweet for tweet in tweets]

# Convert previously selected fields into a pandas dataframe for analysis
# function courtesy of Matthew Beck 
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
               ,'Language':tweet['metadata']['iso_language_code']
               ,'content type':content_type
               ,'device':re.search("\">(.*)<",tweet['source']).group(1)
               ,'favorites':tweet['favorite_count']
               ,'retweets':tweet['retweet_count']
              }
        
        df = df.append(data,ignore_index=True)
    return df

tweets_pd = tweets_to_pd(tweetlist)

# drop the table for next run
db.coll.drop()
# always search #harnessracing #horseracing #racingwrongs #nyra
# @HR_Nation @racingwrongs @trotinsider @TheNYRA
# can we lump all into a single database
                        
                        
