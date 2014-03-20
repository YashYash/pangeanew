from django.contrib.auth.models import User
from django.db import models


class Charity(models.Model):
    name = models.CharField(max_length=200, null=True)
    posted = models.DateTimeField(auto_now=True)
    charity_url = models.CharField(max_length=1000, null=True, blank=True)
    slogan = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=6000, null=True, blank=True)
    cover_photo = models.ImageField(upload_to="images/charity_coverphoto", null=True, blank=True)
    background_image = models.ImageField(upload_to="images/charity_background", null=True, blank=True)
    image = models.ImageField(upload_to="images/charity_logo", null=True, blank=True)
    user = models.OneToOneField(User, related_name="charity")

    def __unicode__(self):
        return self.name


class Video(models.Model):
    charity = models.ForeignKey(Charity)
    title = models.CharField(max_length=250)
    posted = models.DateTimeField(auto_now=True)
    video_url = models.URLField()
    description = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.title


class ClickCount(models.Model):

    like = 'fb_like'
    share = 'fb_share'
    send = 'fb_send'
    action = (
        (like, 'like'),
        (share, 'share'),
        (send, 'send'),
    )

    facebook_count = models.CharField(max_length=10, choices=action,)

    video = models.ForeignKey(Video)
    user = models.ForeignKey(User, related_name="click_count")





