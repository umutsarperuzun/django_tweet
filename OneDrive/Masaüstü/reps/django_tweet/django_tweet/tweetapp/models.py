from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    message=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Tweet Owner: {self.username}, Message: {self.message} , Create_Time : {self.created_at}"

    