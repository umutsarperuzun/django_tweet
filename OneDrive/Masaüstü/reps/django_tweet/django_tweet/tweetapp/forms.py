from django import forms

class AddTweetForm(forms.Form):
    username=forms.CharField(label="Username", max_length=50)
    text=forms.CharField(label="text",max_length=100)