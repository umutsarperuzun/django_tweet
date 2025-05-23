from django.shortcuts import render
from . import models

# Create your views here.
def list_tweet(request):
    all_tweets= models.Tweet.objects.all()
    tweet_dict = {"Tweets": all_tweets}
    return render(request,"tweetapp/list_tweet.html",context=tweet_dict)

def add_tweet(request):
    if request.method == "POST":
        print(request.POST["nickname"])
    return render(request,"tweetapp/add_tweet.html")