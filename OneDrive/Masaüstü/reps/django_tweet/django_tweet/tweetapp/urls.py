from django.urls import path,include
from . import views

app_name="tweetapp"

urlpatterns = [
    path("",views.list_tweet,name="list_tweet"), #sarperuzun.com/tweetapp/
    path("add_tweet/",views.add_tweet,name="add_tweet"),#sarperuzun.com/tweetapp/add_tweet
    path("addtweetbyform/",views.addtweetbyform,name="addtweetbyform"),
    path("addtweetbymodelform/",views.addtweetbymodelform,name="addtweetbymodelform"),
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path('tweet_delete/<int:id>',views.tweet_delete,name="tweet_delete")      
]
    
