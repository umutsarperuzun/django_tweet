from django.shortcuts import render,redirect
from . import models
from django .urls import reverse,reverse_lazy
from tweetapp.forms import AddTweetForm,AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.
def list_tweet(request):
    all_tweets= models.Tweet.objects.all()
    tweet_dict = {"Tweets": all_tweets}
    return render(request,"tweetapp/list_tweet.html",context=tweet_dict)

@login_required(login_url="/login")
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
    

def addtweetbymodelform(request):
    if request.method == "POST":
        form= AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname=form.cleaned_data["nickname"]
            message=form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('tweetapp:list_tweet'))
        else:
            print("error in form!")
            return render(request,'tweetapp/addtweetbymodelform.html',context={"form": form})
    else:
        form=AddTweetModelForm()
        return render(request,'tweetapp/addtweetbymodelform.html',context={"form": form})   
    
class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy("login") #reverse lazy kullanmamizin sebebi bu view az kullanilacagi icin sistemi yormamak adina daha yavas olan reverse versiyonunu koyduk
    template_name="registration/signup.html"