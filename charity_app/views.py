from django.shortcuts import render, redirect
from charity_app.forms import CharityForm, VideoForm
from charity_app.models import Charity, Video

def home(request):
    return render(request, "home.html")


def charities(request):
    charities = Charity.objects.all()
    data = {'charities': charities}
    return render(request, "charities/charities.html", data)


def new_charity(request):
    if request.method == "POST":
        form1 = CharityForm(request.POST)
        if form1.is_valid():
            if form1.save():
                return redirect("/charities")
    else:
        form1 = CharityForm()
    data = {'form1': form1}
    return render(request, "charities/new_charity.html", data)


def view_charity(request, charity_id):
    charity = Charity.objects.get(id= charity_id)
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
