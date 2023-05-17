from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from Twitter.Search.SentimentAnalysis import authenticate, percent_calc, search_twitter, classify
from .forms import SearchForm
import csv

consumer_key = "#"
consumer_secret = "#"
access_token = "#"
access_token_secret = "#"

def index(request, *args, **kwargs):
	form = SearchForm()
	context = {
		'form': form,
	}
	return render(request, 'search/index.html', context)

def get_name(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			search = form.cleaned_data['search']
	else:
		form = SearchForm()

	authenticate(consumer_key, consumer_secret, access_token, access_token_secret)
	global public_tweets
	public_tweets = search_twitter(search)
	global all_tweets
	all_tweets = classify(public_tweets)
	percentage = percent_calc()
	
	context = {
		'search' : search,
		'all_tweets' : all_tweets,
		'percentage' : percentage,
	}

	return render(request, 'search/search-results.html', context)

def download_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="analysis.csv"'

	fieldnames = ['Tweet', 'Sentiment']
	writer = csv.DictWriter(response, fieldnames=fieldnames)
	writer.writeheader()

	for d in all_tweets:    
		writer.writerow({
				'Tweet' : d['tweet'].encode('ascii', 'ignore').decode('ascii'),
				'Sentiment' : 'Postive',
			})
	return response