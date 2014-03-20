from django.forms import ModelForm
from user_app.models import ActiveUser

__author__ = 'yash'


class ActiveUserForm(ModelForm):
    class Meta:
        model= ActiveUser
        exclude = ["user"]