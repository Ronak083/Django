import snscrape.modules.twitter as sntwitter
import pandas as pd

Key = "adani"

for tweet in sntwitter.TwitterSearchScraper(Key).get_items():
	print(tweet.)
	break

#import tweepy
#
#auth = tweepy.OAuthHandler('MrOZwmnsez7PayuFrKKI1oQIc', 'hV3vzMkiRUYe3IvN8XUJoEuRpsIuZGwnW2zyYZHXCMaKXQhxah')
#auth.set_access_token('998534630490845184-EPWL2TcrdSMbAyMJ9efp53tI3KRoOxn', '3yAXm0shxfOrlvbIJcxAJtPekV8dFKJKApaanIWiroiBX')
#
#api = tweepy.API(auth)
#Key = 'adani'
#res = api.search_tweets(Key)
#print(res)

