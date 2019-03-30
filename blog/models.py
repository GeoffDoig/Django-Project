from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """ A single blog post """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    avatar = models.ImageField(default="default.png")
    tag = models.CharField(max_length=30, blank=True, null=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
