from django.shortcuts import render, redirect

# Create your views here.
from user_app.forms import ActiveUserForm, NewsfeedForm, NewsfeedfbForm
from user_app.models import ActiveUser, Newsfeed, Newsfeedfb


def users(request):
    activeuser = request.user.activeuser
    data = {'activeuser': activeuser}
    return render(request, "users/users.html", data)

def fbusers(request):
    return render(request, "fbusers/fbusers.html")



def user_profile(request):
    activeuser = request.user.activeuser
    data = {'activeuser': activeuser}
    return render(request, "users/user_profile.html", data)

def fbuser_profile(request):
    user = request.user
    data = {'user': user}
    return render(request, "fbusers/fbuser_profile.html", data)

def users_home(request):
    activeuser = request.user.activeuser
    data = {'activeuser': activeuser}
    return render(request, "users/user_home.html", data)


def fbusers_home(request):
    user = request.user
    data = {'user': user}
    return render(request, "fbusers/fbuser_home.html", data)


def fbaddprofile(request):
    return render(request, "fbusers/fbaddprofile.html")

def addprofile(request):
    return render(request, "users/addprofile.html")



def new_user(request):
    if request.method == "POST":
        form = ActiveUserForm(request.POST)
        if form.is_valid():
            activeuser = form.save(commit=False)
            activeuser.save()
            activeuser.user = request.user
            return redirect("users")
    else:
        form = ActiveUserForm()
    data = {'form': form}
    return render(request, "users/new_user.html", data)

def newsfeed(request):
    if request.method == "POST":
        form5 = NewsfeedForm(request.POST)
        if form5.is_valid():
            newsfeed = form5.save(commit=False)
            newsfeed.user = request.user
            newsfeed.save()
            return redirect("newsfeed")
    else:
        form5 = NewsfeedForm()
    user = request.user
    activeuser = request.user.activeuser
    newsfeedfb = Newsfeedfb.objects.all()
    newsfeed = Newsfeed.objects.all()
    data = {'form5': form5, 'newsfeed': newsfeed, 'user': user, "activeuser":activeuser, "newsfeedfb": newsfeedfb}
    return render(request, "users/newsfeed.html", data)

def fbnewsfeed(request):
    if request.method == "POST":
        form5 = NewsfeedfbForm(request.POST)
        if form5.is_valid():
            newsfeedfb = form5.save(commit=False)
            newsfeedfb.user = request.user
            newsfeedfb.save()
            return redirect("fbnewsfeed")
    else:
        form5 = NewsfeedfbForm()
    user = request.user
    newsfeedfb = Newsfeedfb.objects.all()
    newsfeed = Newsfeed.objects.all()
    data = {'form5': form5, 'newsfeed': newsfeed, 'user': user, "newsfeedfb": newsfeedfb}
    return render(request, "fbusers/fbnewsfeed.html", data)



def view_user(request, user_id):
    user = ActiveUser.objects.get(id= user_id)
    data = {"user": user}
    return render(request, "users/view_user.html", data)


def edit_user(request, user_id):
    user = ActiveUser.objects.get(id= user_id)
    print user
    if request.method == "POST":
        form = ActiveUserForm(request.POST, instance= user)
        print "POST"
        if form.is_valid():
            if form.save():
                return redirect("/users/{}".format(user_id))
    else:
        form = ActiveUserForm(instance= user)

    data = {"user": user, "form": form}
    print form
    return render(request, "users/edit_user.html", data)


def delete_user(request, user_id):
    user = ActiveUser.objects.get(id= user_id)
    user.delete()
    return redirect("/users")

def compiledlist(request):
    list = zip(newsfeed, fbnewsfeed)
    return render(request, "fbusers/fbnewsfeed.html", {"list":list})
