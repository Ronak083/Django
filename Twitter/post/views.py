from django.shortcuts import redirect, render
import tweepy
from django.conf import settings

# Create your views here.
def index(request):
    if request.method=='POST':
        content = request.POST.get('content', '')

        if content:
            print ('Content', content)

            auth = tweepy.OAuthHandler(settings.API_KEY,settings.API_KEY_SECRET)
            auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
            global api
            api = tweepy.API(auth)

            return redirect('post')

    return render(request, 'index.html')