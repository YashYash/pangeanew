from django.forms import ModelForm
from charity_app.models import Charity, Video
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

__author__ = 'yash'




class UserForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]
        widgets = {
            "password": forms.PasswordInput
        }



class SignupForm(UserForm):
    confirm_password = forms.CharField(
        widget = forms.PasswordInput
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        password_conf = self.cleaned_data.get("confirm_password")
        if password is not None and password != password_conf:
            raise forms.ValidationError(
                "Password confirmation does not match password"
            )

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class CharityForm(ModelForm):
    class Meta:
        model=Charity
        exclude = ["user"]


class VideoForm(ModelForm):
    class Meta:
        model=Video




