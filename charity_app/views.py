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

#Django Auth, leads to login in page, and uses signupform in forms.py

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
                    return redirect("users")

    else:
        form1 = LoginForm()
    data = {'form1': form1}
    return render(request, "login.html", data)


# goes to index.html, name="index". The current landing page
def index(request):
    data = {}
    return render(request, 'index.html', data)

# goes to base.html, name="home", was the old landing page. Its my backup, incase the parallax code breaks in index.html
def home(request):
    return render(request, "base.html")

@login_required
# goes to the charity_home page. The page is not used. Its there so I can test stuff.
def charity_home(request):
    charity = request.user.charity.get()
    print charity.name
    data = {'charity': charity}
    return render(request, "charities/charities.html", data)
@login_required
#goes to charities.html. This the page the user sees when he clicks the charity account button on users.html. name="charities"
def charities(request):
    activeuser = request.user.activeuser
    data = {'activeuser': activeuser}
    return render(request, "charities/charities.html", data)

@login_required
#goes to new_charity.html. Where a charity can be added. name="new_charity"
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

@login_required
# never used. Its there for code reference.
def view_charity(request, charity_id):
    charity = request.user.charity.get()
    print charity.name
    data = {'charity': charity}
    return render(request, "charities/view_charity.html", data)
@login_required
# used on the charity_info page as a "edit charity" button. So the charity can make cahnges to their profile
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
@login_required
# used on the charity_info page as a "delete charity" button. So the charity can delete their profile
def delete_charity(request, charity_id):
    charity = Charity.objects.get(id=charity_id)
    charity.delete()
    return redirect("/charities")
@login_required
# this is the charity profile page. Where they can view what there profile looks like for when others look at it
def charity_info(request):
    charity = request.user.charity
    data = {'charity': charity}
    return render(request, "charities/charity_info.html", data)
@login_required
# non of the videos views have been used yet. I might use them when I start showing videos
# in the charity, user and giver profile
def videos(request):
    videos = Video.objects.all()
    data = {'videos': videos}
    return render(request, "videos/videos.html", {'videos': videos}, data)

@login_required
#The only video view that I use. So the charity can upload as many donation vides as they want.
#It is the "add_video" button on charities.html
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
@login_required
#never used. Because i used angular to make one page that shows all the videos
def view_video(request, video_id):
    video = Video.objects.get(id= video_id)
    data = {"video": video}
    return render(request, "videos/view_video.html", data)
@login_required
# going to use this so a user can edit a videso url description. IT will be on there profle page
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

@login_required
#used to delete videos. On the charities profile page
def delete_video(request, video_id):
    video = Video.objects.get(id= video_id)
    video.delete()
    return redirect("/videos")

@login_required
def charity_view_videos(request):
    videos = Video.objects.all()
    data = {'videos': videos}
    return render(request, "viewvideos/all_videos.html", data)

@login_required
def charity_newsfeed(request):
    return render(request, "newsfeed/newsfeed.html")
@login_required
#stripe
def payment(request):
    return render(request, "payment/register.html")
@login_required
# the angular page where all the videos are shown in the ng-view
def angular(request):
    return render(request, "angular_videos.html")
@login_required
#this page is no longer used. I use it to save my auth_views redirects
def logs(request):
    return render(request, "logs.html")