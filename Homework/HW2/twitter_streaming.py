# Twitter Accounts
twitterAcctList = ["@TheNYRA", "@HR_Nation", "@NYSGamingComm", "@racingwrongs", "@trotinsier", 
                   "@YonkersRaceway", "@BuffaloRaceway", "@governondowns", "@FIGaming", "@gotiogadowns"]
# list of hashtags

#AqueductRaceTrack
#BataviaDowns
#BelmontPark
#BuffaloRaceway
#FingerLakesRacetrack 
#MonticelloRaceway
#SaratogaRaceCourse
#TiogaDowns
#VernonDown
#YonkersRaceway 

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
    
# Not sure what this is:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = []
username = 'jack'
count = 100
try: 
# Pulling individual tweets from query
for tweet in api.user_timeline(id=username, count=count):
# Adding to list that contains all tweets
  tweets.append((tweet.created_at,tweet.id,tweet.text))
except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)
      
      
tweets_list = []
text_query = '2020 US Election'
count = 100
try:
# Pulling individual tweets from query
    for tweet in api.search(q=text_query, count=count):
# Adding to list that contains all tweets
      tweets.append((tweet.created_at,tweet.id,tweet.text))
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)
    
for tweet in api.search(q=text_query, count=count):
  # Appending chosen tweet data
  tweets.append((tweet.created_at,tweet.id,tweet.text, tweet.user,   tweet.favorite_count))


username = 'jack'
count = 2000
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                        .setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
user_tweets = [[tweet.date, tweet.text] for tweet in tweets]


text_query = 'USA Election 2020'
count = 2000
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)\
                                            .setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
text_tweets = [[tweet.date, tweet.text] for tweet in tweets]



text_query = 'USA Election 2020'
since_date = '2019-01-01'
until_date = '2019-10-31'
count = 2000
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)
.setSince(since_date).setUntil(until_date).setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
text_tweets = [[tweet.date, tweet.text] for tweet in tweets]

# another example
#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []  

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    #write the csv  
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("J_tsar")
    
# Yet another example
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

account_list = []
if (len(sys.argv) > 1):
  account_list = sys.argv[1:]
else:
  print("Please provide a list of usernames at the command line.")
  sys.exit(0)

if len(account_list) > 0:
  for target in account_list:
    print("Getting data for " + target)
    item = auth_api.get_user(target)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))

tweets = item.statuses_count
account_created_date = item.created_at
delta = datetime.utcnow() - account_created_date
account_age_days = delta.days
print("Account age (in days): " + str(account_age_days))
if account_age_days > 0:
   print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))
      
hashtags = []
mentions = []
tweet_count = 0
end_date = datetime.utcnow() - timedelta(days=30)
for status in Cursor(auth_api.user_timeline, id=target).items():
   tweet_count += 1
   if hasattr(status, "entities"):
        entities = status.entities
        if "hashtags" in entities:
          for ent in entities["hashtags"]:
            if ent is not None:
              if "text" in ent:
                hashtag = ent["text"]
                if hashtag is not None:
                  hashtags.append(hashtag)
        if "user_mentions" in entities:
          for ent in entities["user_mentions"]:
            if ent is not None:
              if "screen_name" in ent:
                name = ent["screen_name"]
                if name is not None:
                  mentions.append(name)
      if status.created_at < end_date:
        break

    print
    print("Most mentioned Twitter users:")
    for item, count in Counter(mentions).most_common(10):
      print(item + "\t" + str(count))

    print
    print("Most used hashtags:")
    for item, count in Counter(hashtags).most_common(10):
      print(item + "\t" + str(count))

    print
    print "All done. Processed " + str(tweet_count) + " tweets."
    print