from sqlite3 import apilevel
import tweepy
from textblob import TextBlob
from django.conf import settings
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Create your views here.

def home(request):
    return render(request, "home.html")


def Search(request):
    Key = request.POST["Key"]
    #frame = request.POST["frame"]
    
    API_KEY= 'OrYIsElZ7PTS0x0LZfGTM4bxt'
    API_KEY_SECRET = 'dmhoVjhXiD9VSZNDxONEx7UG1kbxnS1VcfOYFMiYYS7nyihdAT'
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAJZemwEAAAAAqxsPqpsErJp717hpl5pmEo3%2FfSs%3DCn2lBdQXzUSkqf5bkzUpj81RnCuXMxuyFOFq2gr7rd8ltAAngS'
    ACCESS_TOKEN = '998534630490845184-2RVEqixomzdYjablWkkubx0JvEsy0dF'
    ACCESS_TOKEN_SECRET = 'lsblGMarnPam7PVimfyRkObIEmZlcoLgAS3Fkedk2LUY0'
    Cid ='Z3BoeHExRmZuRWxIcXpwUXlsbmE6MTpjaQ'
    Cids ='75dFF8dvPe2H152enu3Y3FRE3zYC425VOFo4sGI-Al5aK5L2Zi'
    auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth)
    all_tweet = api.search_tweets(Key)
    
    return render(request, 'result.html', {'result': all_tweet})
    # Use the Twitter API to search for tweets containing the query string
    #tweets = api.search_tweets(q=Key)
    
    # Return the list of tweets
    #tweets = []
    #limit = 100
    #for tweet in sntwitter.TwitterSearchScraper(Key).get_items():
	#	    tweets.append([])
	#	    
    

    #global public_tweets
    #public_tweets = SentimentAnalysis.find_tweets(Key)
    #global all_tweets
    #all_tweets = SentimentAnalysis.classify(public_tweets)
    #percentage = SentimentAnalysis.percent_calc()

    #context = {
    #    'search_key' : Key,
	#	'all_tweets' : all_tweets,
	#	'percentage' : percentage,
    #}
     

def classify(all_tweet):
	all_tweets = []

	global positive_count
	global neutral_count
	global negative_count

	positive_count = 0	
	neutral_count = 0
	negative_count = 0	

	for tweet in all_tweet:
		tweet_collection = {}		
		polarity = TextBlob(tweet.text).sentiment.polarity
		
		tweet_collection['username'] = tweet.user.screen_name
		tweet_collection['tweet'] = tweet.text
		tweet_collection['polarity'] = polarity

		if polarity > 0:
			tweet_collection['color'] = 'green'
			tweet_collection['sentiment'] = 'positive'
			positive_count += 1

		elif polarity < 0:
			tweet_collection['color'] = 'red'
			tweet_collection['sentiment'] = 'negative'
			negative_count += 1
		else:
			tweet_collection['color'] = 'blue'
			tweet_collection['sentiment'] = 'neutral'
			neutral_count += 1
		all_tweets.append(tweet_collection)

	return all_tweets

def percent_calc():
	count = {}

	total_tweets = positive_count + neutral_count + negative_count

	if max(positive_count,negative_count) == positive_count:
		count['max'] = 'Positive'
	elif max(positive_count,negative_count) == negative_count:
		count['max'] = 'Negative'
	else:
		count['max'] = 'Balanced'

	percent_positive = (float(positive_count)/float(total_tweets+1)) * 100
	percent_negative = (float(negative_count)/float(total_tweets+1)) * 100
	percent_neutral = 100 - percent_positive - percent_negative
	

	count['positive'] = "%.2f" % percent_positive 
	count['neutral'] = "%.2f" % percent_neutral
	count['negative'] = "%.2f" % percent_negative

	return count