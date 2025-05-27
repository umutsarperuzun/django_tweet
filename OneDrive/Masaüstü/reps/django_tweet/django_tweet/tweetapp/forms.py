from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    username=forms.CharField(label="username", max_length=50)
    text=forms.CharField(label="text",max_length=100,widget=forms.Textarea(attrs={"class":"tweetmessage"}))
    
    

class AddTweetModelForm(ModelForm):
    class Meta:
        model=Tweet
        fields=["nickname","message"]
    