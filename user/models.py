from django.db import models

# Create your models here.
class userdata(models.Model):
    user_name = models.CharField(max_length=255)
    user_file=models.TextField()