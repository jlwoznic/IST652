# Week 8
# Joyce Woznica
# Working with Twitter

import pymongo
client = pymongo.MongoClient('localhost',27017)
#list the databases defined
client.database_names()
db = client.bball
db.collection_names()
coll=db.bbcoll
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
#4. Then see if you can find the Screen names referenced in these tweets.
# Yes - changed the function to display them
#5. Can you display them?

# 8.3 - maybe see if Kentucky is mentioned in the message

def find_team(tweets, team):
    for tweet in tweets:
        msg = tweet['text']
        if msg.find(team) != -1:
            print('Team Mentioned: ', msg)

find_team(doclist[:10], "Kentucky")
# could count these
def count_tweets(tweets, team):
    i = 0
    for tweet in tweets:
        msg = tweet['text']
        if msg.find(team) != -1:
            i = i + 1
    print("Team ", team, " mentioned ", i, " times.")

count_tweets(doclist[:30], "Kentucky")

## Twitter reads
import pymongo
# connect to the database
client = pymongo.MongoClient('localhost', 27017)

##
client.database_names()
db = client.grad
db.collection_names()
coll=db.class2020
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

