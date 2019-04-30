
from doc import *
import requests
import tweepy
import json

# scrape twitter for keywords and location


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def process_or_store(tweet):
    file = open('tweets.json', 'w+')
    file.write(json.dumps(tweet))
    file.close()
    # print(json.dumps(tweet), '\n')


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#     print(tweet.user.screen_name)
#     print(tweet.user.location)
#     print(tweet.created_at)
#     print(tweet.coordinates)


trending = api.trends_place(1)

x = 0
for i in trending:
    for trends in i['trends']:
        print(trends['name'])
        print(trends['tweet_volume'])
        # print(trends[x]['name'])
        # print(trends[x]['tweet_volume'])
        x += 1
        print(x)
