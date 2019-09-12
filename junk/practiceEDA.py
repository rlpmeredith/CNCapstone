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

# define a handle to inspect for quicker reference
handle = '@realdonaldtrump' # for example purposes; prop any handle you want!
tweets = api.user_timeline(screen_name=handle, count=100)

# write tweet data to a JSON file
tweet_list = []
for tweet in tweets:
    # pprint(tweet._json)  # uncomment to see the tweet data
    tweet_list.append(tweet._json)

with open('data.json', 'w') as f:
    json.dump(tweet_list, f)

# read data back in from json file into a list of strings
with open('data.json') as json_file:
    data = json.load(json_file)

tweet_text = []
for my_dict in data:
    pprint(my_dict['text'])
    tweet_text.append(my_dict['text'])

# calculate average length of tweets
tweet_words = []
for tweet in tweet_text:
    words = tweet.split()
    tweet_words.append(len(words))

avg_words = sum(tweet_words) / len(tweet_words)
print(f"The average number of words per tweet is {avg_words:.1f}")