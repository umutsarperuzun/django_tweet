from django.shortcuts import render,redirect
from . import models
from django .urls import reverse
from tweetapp.forms import AddTweetForm

# Create your views here.
def list_tweet(request):
    all_tweets= models.Tweet.objects.all()
    tweet_dict = {"Tweets": all_tweets}
    return render(request,"tweetapp/list_tweet.html",context=tweet_dict)

def add_tweet(request):
    if request.method == "POST":
        nickname=request.POST["nickname"]
        message=request.POST["message"]
        tweet = models.Tweet(nickname=nickname, message=message)
        tweet.save()
        return redirect(reverse('tweetapp:list_tweet'))
    else:
        
        return render(request,"tweetapp/add_tweet.html")
    
def addtweetbyform(request):
    if request.method == "POST":
        form= AddTweetForm(request.POST)
        if form.is_valid():
            nickname=form.cleaned_data["username"]
            message=form.cleaned_data["text"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('tweetapp:list_tweet'))
        else:
            print("error in form!")
            return render(request,'tweetapp/addtweetbyform.html',context={"form": form})
    else:
        form=AddTweetForm()
        return render(request,'tweetapp/addtweetbyform.html',context={"form": form})