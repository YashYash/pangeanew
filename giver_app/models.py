from django.contrib.auth.models import User
from django.db import models
from charity_app.models import Charity


class Giver(models.Model):
    name = models.CharField(max_length=200, null=True)
    posted = models.DateTimeField(auto_now=True)
    giver_url = models.CharField(max_length=1000, null=True, blank=True)
    slogan = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to="images/giver_logo", null=True, blank=True)
    cover_photo = models.ImageField(upload_to="images/giver_coverphoto", null=True, blank=True)
    background_image = models.ImageField(upload_to="images/giver_background", null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    user = models.OneToOneField(User, related_name="giver")
    charities = models.ManyToManyField(Charity, related_name="givers")


    def __unicode__(self):
        return self.name

