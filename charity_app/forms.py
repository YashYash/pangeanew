from django.forms import ModelForm
from charity_app.models import Charity, Video


__author__ = 'yash'


class CharityForm(ModelForm):
    class Meta:
        model=Charity


class VideoForm(ModelForm):
    class Meta:
        model=Video




