from django.db import models
from django.contrib.auth.models import User

class ActiveUser(models.Model):
    name = models.CharField(max_length=200, null=True)
    posted = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(upload_to="images/user_profile_pic", null=True)
    user = models.OneToOneField(User, related_name="activeuser")


    def __unicode__(self):
        return self.name
