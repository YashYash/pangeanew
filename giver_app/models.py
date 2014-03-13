from django.contrib.auth.models import User
from django.db import models
from charity_app.models import Charity


class Giver(models.Model):
    name = models.CharField(max_length=200)
    posted = models.DateTimeField(auto_now=True)
    giver_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="images/giver_logo")
    user = models.ForeignKey(User, related_name="giver")
    charities = models.ManyToManyField(Charity)


    def __unicode__(self):
        return self.name

