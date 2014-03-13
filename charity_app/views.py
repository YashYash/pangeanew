from distutils.command import register
import urlparse
from django.shortcuts import render, redirect
from charity_app.forms import CharityForm, VideoForm
from charity_app.models import Charity, Video
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from charity_app import forms
from charity_app.forms import SignupForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["firstname"],
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
        return redirect("login")

    else:
        form = SignupForm()
    data = {'form': form}
    return render(request, "signup.html", data)


@login_required
def special_page(request):
    data = {}
    return render(request, "charities/charities.html", data)

def login1(request):
    if request.method == "POST":
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            user = authenticate(username=form1.cleaned_data['username'], password=form1.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("charity_home.html")

    else:
        form1 = LoginForm()
    data = {'form1': form1}
    return render(request, "login.html", data)


def index(request):
    data = {}
    return render(request, 'index.html', data)


def home(request):
    return render(request, "base.html")

def charity_home(request):
    charity = request.user.charity.get()
    print charity.name
    # charity = Charity.objects.get(user=user_id)
    # print charity.id
    # charities = Charity.objects.all()
    data = {'charity': charity}
    return render(request, "charities/charities.html", data)

def charities(request):
    charities = Charity.objects.all()
    data = {'charities': charities}
    return render(request, "charities/charities.html", data)


def new_charity(request):
    if request.method == "POST":
        form0 = CharityForm(request.POST)
        if form0.is_valid():
            charity = form0.save(commit=False)
            charity.user = request.user
            charity.save()
            return redirect("/charities")
    else:
        form0 = CharityForm()
    data = {'form0': form0}
    return render(request, "charities/new_charity.html", data)


def view_charity(request, charity_id):
    charity = Charity.objects.get(id=charity_id)
    data = {"charity": charity}
    return render(request, "charities/view_charity.html", data)


def edit_charity(request, charity_id):
    charity = Charity.objects.get(id= charity_id)
    if request.method == "POST":
        form1 = CharityForm(request.POST, instance=charity)
        if form1.is_valid():
            if form1.save():
                return redirect("/charities/{}".format(charity_id))
    else:
        form1 = CharityForm(instance=charity)
    data = {"charity": charity, "form1": form1}
    return render(request, "charities/edit_charity.html",data)


def delete_charity(request, charity_id):
    charity = Charity.objects.get(id=charity_id)
    charity.delete()
    return redirect("/charities")


def charity_info(request):
    charity = request.user.charity.get()
    print charity.name
    data = {'charity': charity}
    return render(request, "charities/charity_info.html", data)

def videos(request):
    videos = Video.objects.all()
    data = {'videos': videos}
    return render(request, "videos/videos.html", {'videos': videos})


def new_video(request):
    if request.method == "POST":
        form2 = VideoForm(request.POST)
        if form2.is_valid():
            if form2.save():
                return redirect("/videos")
    else:
        form2 = VideoForm()
    data = {'form2': form2}
    return render(request, "videos/new_video.html", data)


def view_video(request, video_id):
    video = Video.objects.get(id= video_id)
    data = {"video": video}
    return render(request, "videos/view_video.html", data)


def edit_video(request, video_id):
    video = Video.objects.get(id= video_id)
    print video
    if request.method == "POST":
        form2 = VideoForm(request.POST, instance= video)
        print "POST"
        if form2.is_valid():
            if form2.save():
                return redirect("/videos/{}".format(video_id))
    else:
        form2 = VideoForm(instance= video)

    data = {"video": video, "form2": form2}
    print form2
    return render(request, "videos/edit_video.html", data)


def delete_video(request, video_id):
    video = Video.objects.get(id= video_id)
    video.delete()
    return redirect("/videos")



def charity_view_videos(request):
    videos = Video.objects.all()
    data = {'videos': videos}
    return render(request, "viewvideos/all_videos.html", data)

def charity_newsfeed(request):
    return render(request, "newsfeed/newsfeed.html")

def payment(request):
    return render(request, "payment/register.html")

def angular(request):
    return render(request, "angular_videos.html")