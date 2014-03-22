from django.forms import ModelForm
from user_app.models import ActiveUser, Newsfeed

__author__ = 'yash'


class ActiveUserForm(ModelForm):
    class Meta:
        model= ActiveUser
        exclude = ["user"]


class NewsfeedForm(ModelForm):
    class Meta:
        model = Newsfeed
        exclude = ["user"]