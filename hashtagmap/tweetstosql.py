import os
import tweepy
import json
from pprint import pprint


# fetch the secrets from our virtual environment variables
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

# authenticate to the service we're accessing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# create the connection
api = tweepy.API(auth)

# setup query
search_words = "#datascience"
date_since = "2000-09-01"
tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since).items(100)
count = 1
print(type(tweets))
for tweet in tweets:
    print(tweet.coordinates)
