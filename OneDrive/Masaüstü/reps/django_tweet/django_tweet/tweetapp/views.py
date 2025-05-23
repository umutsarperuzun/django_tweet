from django.shortcuts import render

# Create your views here.
def list_tweet(request):
    return render(request,"tweetapp/list_tweet.html")

def add_tweet(request):
    return render(request,"tweetapp/add_tweet.html")