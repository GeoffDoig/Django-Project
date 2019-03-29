from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #full_name = models.CharField(max_length=50, blank=True)
    #street_address1 = models.CharField(max_length=40, blank=True)
    #street_address2 = models.CharField(max_length=40, blank=True)
    #town_or_city = models.CharField(max_length=40, blank=True)
    #county = models.CharField(max_length=40, blank=True)
    #country = models.CharField(max_length=40, blank=True)
    #postcode = models.CharField(max_length=20, blank=True)
    #phone_number = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to="profile_images", default="/media/profile_images/default.png")
    
    def __str__(self):
        return self.user.username
