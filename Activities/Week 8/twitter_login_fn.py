''' Provides function that connects to Twitter
    Usage is shown in main test program
'''

import tweepy

# put the authorization codes here from your Twitter developer application
CONSUMER_KEY = 'NeMSryEx2Uc6YFi8t74fHsFNe'
CONSUMER_SECRET = 'XlzCSmkKQM2OhrfO9r10p9fWNRNB1W2Qd8fLOHo0VcCET0ELqM'
OAUTH_TOKEN = '1259973954166456320-b5xXXSu7WUfTVLEjhXagRvYF6wzmiL'
OAUTH_SECRET = 'G3AbUXGLUEcobVTeJYlAzz29uiTQIKchSUfb1rVUFgoHI'

# API key: NeMSryEx2Uc6YFi8t74fHsFNe
# API secret key: XlzCSmkKQM2OhrfO9r10p9fWNRNB1W2Qd8fLOHo0VcCET0ELqM
# Access Token: 1259973954166456320-b5xXXSu7WUfTVLEjhXagRvYF6wzmiL
# Secret Token: G3AbUXGLUEcobVTeJYlAzz29uiTQIKchSUfb1rVUFgoHI

# login to Twitter with ordinary rate limiting
def oauth_login():
  # get the authorization from Twitter and save in the Tweepy package
  auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
  auth.set_access_token(OAUTH_TOKEN,OAUTH_SECRET)
  tweepy_api = tweepy.API(auth)

  # if a null api is returned, give error message
  if (not tweepy_api):
      print ("Problem Connecting to API with OAuth")

  # return the Twitter api object that allows access for the Tweepy api functions
  return tweepy_api

# login to Twitter with extended rate limiting
#  must be used with the Tweepy Cursor to wrap the search and enact the waits
def appauth_login():
  # get the authorization from Twitter and save in the Tweepy package
  auth = tweepy.AppAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
  # apparently no need to set the other access tokens
  tweepy_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

  # if a null api is returned, give error message
  if (not tweepy_api):
      print ("Problem Connecting to API with AppAuth")

  # return the Twitter api object that allows access for the Tweepy api functions
  return tweepy_api
    
# Test program to show how to connect
if __name__ == '__main__':
  tweepy_api = oauth_login()
  print ("Twitter OAuthorization: ", tweepy_api)
  tweepy_api = appauth_login()
  print ("Twitter AppAuthorization: ", tweepy_api)