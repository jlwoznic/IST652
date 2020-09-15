#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:21:50 2020

@author: joycewoznica
"""

# Twitter reads
import pymongo
# connect to the database
client = pymongo.MongoClient('localhost', 27017)

##
client.database_names()
db = client.racing
db.collection_names()
coll=db.racetweet
docs = coll.find()
#convert the document cursor to a list of documents
doclist = [tweet for tweet in docs]
len(doclist)
# show difference from print
print(doclist[:1])
#Look through this to point out field names
#Here is a little print function that will help.
def print_tweet_data(tweets):
    for tweet in tweets:
        print('\nDate:', tweet['created_at'])
        print('From:', tweet['user']['name'])
        print('Screen Name: ',tweet['user']['screen_name'])
        print('Message', tweet['text'])

print_tweet_data(doclist[:5])

def print_tweet_data2(tweets):
  for tweet in tweets:
    print('\nDate:', tweet['created_at'])
    print('From:', tweet['user']['name'])
    print('Message', tweet['text'])
    if not tweet['place'] is None:
      print('Place:', tweet['place']['full_name'])

print_tweet_data2(doclist)

import tweepy as tw
import os

CONSUMER_KEY = 'NeMSryEx2Uc6YFi8t74fHsFNe'
CONSUMER_SECRET = 'XlzCSmkKQM2OhrfO9r10p9fWNRNB1W2Qd8fLOHo0VcCET0ELqM'
OAUTH_TOKEN = '1259973954166456320-b5xXXSu7WUfTVLEjhXagRvYF6wzmiL'
OAUTH_SECRET = 'G3AbUXGLUEcobVTeJYlAzz29uiTQIKchSUfb1rVUFgoHI'

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

# search after a specific time
# Define the search term and the date_since date as variables
search_words = "Belmont"
date_since = "2020-01-01"
date_until = "2020-05-16"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since,
              until=date_until).items(100)

# Iterate and print tweets
for tweet in tweets:
    if not tweet.text.startswith('RT'):
        print('Tweet Text: ', tweet.text)
        
def print_tweet_data2(tweets):
  for tweet in tweets:
    print('\nDate:', tweet['created_at'])
    print('From:', tweet['user']['name'])
    print('Message', tweet['text'])
    if not tweet['place'] is None:
      print('Place:', tweet['place']['full_name'])
      
print_tweet_data2(tweets)
