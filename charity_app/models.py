from django.db import models


class Charity(models.Model):
    name = models.CharField(max_length=200)
    posted = models.DateTimeField(auto_now=True)
    charity_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.name


class Video(models.Model):
    charity = models.ForeignKey(Charity)
    title = models.CharField(max_length=250)
    posted = models.DateTimeField(auto_now=True)
    video_url = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title



