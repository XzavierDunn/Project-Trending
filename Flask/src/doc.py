
import tweepy

consumer_key = '8wvga0Q8U0tafSGrp1F3JBAZQ'
consumer_secret = 'U4LTztQPhGkUSpsZu3Uu3dwJVLKJNiLlaBJH3EVpbm8VVsoQuP'
access_token = '2409002919-E7K0ebT7IKsvxbBJgV6YvUJdSaIk35PlQ1riv8d'
access_token_secret = 'VRQgM2YWF5lm9uianPXaUwmpdfnrHIBQVprefyUoYYnni'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweepyAPI = api