from django.db import models

# Create your models here.
class Tweet(models.Model):
    nickname= models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Nickname: {self.nickname}, Message: {self.message} , Create_Time : {self.created_at}"

    