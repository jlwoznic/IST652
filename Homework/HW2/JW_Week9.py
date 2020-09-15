#----------------------- Question 2 Continued: Read tweets --------------------------
# Import packages for tweets (be sure to start Mongo DB)
import tweepy as tw
import json
import sys
import os
import pymongo
import pandas as pd
import nltk
import nltk
nltk.download('punkt')
nltk.download('stopwords')

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
dbname = "week9db"
collname = "week9coll"
# Final Attempt
import time
import datetime
date_since = "2019-01-01"
date_until = time.strftime("%Y-%m-%d")

tweets_to_return = 750
search_wordsList = ["@racingwrongs"]

for search_words in search_wordsList:
    print(search_words)
    run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)

# Get Tweet_List for building pandas dataframe - build one for each tweet_list
# for racedb
client = pymongo.MongoClient('localhost', 27017)
db = client.week9db
coll = db.week9coll
# Get docs (tweets)
docs = coll.find()
tweets = coll.find()
# Create list of tweets - tweet_list
doclist = list(docs)
# Create list of tweets - tweet_list
tweet_list = [tweet for tweet in tweets]

tweetlist = [doc['text'] for doc in doclist if 'text' in doc.keys()]
len(tweetlist)
all_tokens = [tok for text in tweetlist for tok in nltk.word_tokenize(text)]
len(all_tokens)

# now get how many of each occurs
textFD = nltk.FreqDist(all_tokens)
textFD.most_common(30)
# lower case
all_tokens = [tok.lower() for tweet in tweetlist for tok in nltk.word_tokenize(tweet)]
# set stopwords
nltk_stopwords = nltk.corpus.stopwords.words('english')
len(nltk_stopwords)

import re
def alpha_filter(w):
    pattern = re.compile('^[^a-z]+$')
    if (pattern.match(w)):
        return True
    else: 
        return False
    
token_list = [tok for tok in all_tokens if not alpha_filter(tok)]
textFD = nltk.FreqDist(all_tokens)
top_words = textFD.most_common(30)

for word, freq in top_words:
    print(word, freq)
    
# do differently for tweets
tweet = "RT @OccupySandy: Good Morning NYC. http://t.co/yRLgrB53 #NotAnotherKatrina#sandy" 
tokens = nltk.word_tokenize(tweet) 
tokens
ttokenizer = nltk.tokenize.TweetTokenizer() 
tokens = ttokenizer.tokenize(tweet) 
tokens
 
    
    
    
    
    