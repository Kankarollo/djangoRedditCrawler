from django.db import models

# Create your models here.
class RedditSubreddit(models.Model):
    name = models.CharField(max_length=100)
