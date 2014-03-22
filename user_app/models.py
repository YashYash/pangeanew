from django.db import models
from django.contrib.auth.models import User

class ActiveUser(models.Model):
    name = models.CharField(max_length=200, null=True)
    posted = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(upload_to="images/user_profile_pic", null=True)
    user = models.OneToOneField(User, related_name="activeuser")


    def __unicode__(self):
        return self.name

class Newsfeed(models.Model):
    title = models.CharField(max_length=500)
    posted = models.DateTimeField(auto_now=True)
    article = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="images/newsfeed", null=True, blank=True)
    quote = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, related_name="newsfeed")


    def __unicode__ (self):
        return self.title