
from doc import *
import requests
import tweepy
import json

# scrape twitter for keywords and location


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# def process_or_store(tweet):
#     file = open('tweets.json', 'w+')
#     file.write(json.dumps(tweet))
#     file.close()
#     # print(json.dumps(tweet), '\n')


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#     print(tweet.user.screen_name)
#     print(tweet.user.location)
#     print(tweet.created_at)
#     print(tweet.coordinates)


# trending = api.trends_place(2427032)
# print(trending)

# x = 0
# for i in trending:
#     for trends in i['trends']:
#         print(trends['name'])
#         print(trends['url'])
#         print(trends['tweet_volume'])
#         x += 1
#         print(x)

# 39.771726, -86.156114

# location = api.trends_closest(39.771726, -86.156114)
# print(location[0]['woeid'])


# mapquest api key G7GTGs1Pf62DjHNWUAcsu8Jn7bxjNJvz

# r = requests.get('http://www.mapquestapi.com/geocoding/v1/address?key=G7GTGs1Pf62DjHNWUAcsu8Jn7bxjNJvz&location=indianapolis')
# for i in r.json()['results']:
#         x = i['locations'][0]['latLng']

# print(x['lat'])
# print(x['lng'])
