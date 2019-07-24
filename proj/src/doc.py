import tweepy
import os

auth = tweepy.OAuthHandler('zPKVwvIEQh8g0nJnQEH0ZEQjB', 'G2mXQMFFJRvXHbhrDLNRFwLWjDm8P3VIwVxwmWspxyPfQ8q   H1e')
auth.set_access_token('2409002919-M5pmvGY9hfakVDvL5ZgvMJuXBm92TNdvLULnLmF   ', 'WkaMbwO0g7sxZYWjo76qcmpxcueRd2J69jY4iyNfLS2   XD')

tweepyAPI = tweepy.API(auth)
