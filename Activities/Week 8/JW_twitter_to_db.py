''' 
This main topic search function for Twitter using the python tweepy package
      Tries to get up to 1000 results from the Twitter REST/Search API search function
        using the tweepy Cursor to repeat the twitter search api requests
      The query string may be a keyword or hashtag, or a set of them connected by or
        example:  query = "#CuseLAX OR CNYlacrosse"
        some queries require quotes on the command line
    Returns a list of json formatted tweets
'''

# Try elimating other code and running this alone with the databases - make sure
# that database will keep filling as new searches are run

import tweepy as tw
import json
import sys
import os
import pymongo
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
    save_to_DB(DBname, DBcollection, result_tweets)

    # Done!

# run tweets
# could use this to loop through dates (+/- 5 days), track and db and collection
tweets_to_return = 100
search_words = "@TheNYRA"
date_since = "2020-01-01"
date_until = "2020-12-31"
dbname = "belmontdb"
collname = "belmontcoll"

run_simple_tweet_search(search_words, tweets_to_return, date_since, date_until, dbname, collname)
                        
                        
                        
                        
                        
                        
