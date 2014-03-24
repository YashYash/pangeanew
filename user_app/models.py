from django.db import models
from django.contrib.auth.models import User

class ActiveUser(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    posted = models.DateTimeField(auto_now=True, blank=True)
    profile_pic = models.ImageField(upload_to="images/user_profile_pic", null=True, blank=True)
    user = models.OneToOneField(User, related_name="activeuser", null=True, blank=True)


    def __unicode__(self):
        return self.name

class Newsfeed(models.Model):
    title = models.CharField(max_length=500)
    posted = models.DateTimeField(auto_now=True)
    article = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="images/newsfeed", null=True, blank=True)
    quote = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, related_name="newsfeed")
    activeuser = models.ForeignKey(ActiveUser, related_name="newsactiveuser", null=True, blank=True)

    def __unicode__ (self):
        return self.title

class Newsfeedfb(models.Model):
    title = models.CharField(max_length=500)
    posted = models.DateTimeField(auto_now=True)
    article = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="images/newsfeed", null=True, blank=True)
    quote = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, related_name="newsfeedfb")

    def __unicode__ (self):
        return self.title