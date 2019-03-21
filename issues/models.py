from django.db import models
from django.utils import timezone

# Create your models here.
class Issue(models.Model):
    """ Fields required for a single issue reported """
    STATUS_CHOICES = (
        ("O", "Open"),
        ("P", "In Progress"),
        ("F", "Fixed"),
        )
    CATEGORY_CHOICES = (
        ("C", "Category"),
        ("B", "Bug"),
        ("F", "Feature"),
        )
    title = models.CharField(max_length=128)
    description = models.TextField()
    screenshot = models.ImageField(upload_to="images", blank=True)
    reported_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="O")
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="C")
    votes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title