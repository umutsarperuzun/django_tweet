from django.contrib import admin
from tweetapp.models import Tweet #Import to model

class TweetAdmin(admin.ModelAdmin): #For admin previllages management and specifications
    fieldsets = [
        ('Message Group',{"fields":["message"]}),
        ('Nickname Group',{"fields":["nickname"]})
    ]
    # fields=['message','nickname']



admin.site.register(Tweet,TweetAdmin)