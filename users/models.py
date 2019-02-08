from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#class for likes incl. price
#class likes(models.Model):
 #   price = models.IntegerField()

#class for follower incl. price
#class followers(models.Model):
 #   price = models.IntegerField()

#class for orders with, link to instaprofile, amount of likes
class order_like(models.Model):
    picture_link = models.CharField(max_length=300)
    likes = models.IntegerField()
    discount = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    infos = models.TextField(blank=True)
    followers_price = 4
    likes_price = 2
    price = followers_price*10

class order_follower(models.Model):
    profile_link = models.CharField(max_length=300)
    follower = models.IntegerField()
    discount = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    infos = models.TextField(blank=True)

#Extending User model and add some variables
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profil'