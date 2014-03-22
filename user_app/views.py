from django.shortcuts import render, redirect

# Create your views here.
from user_app.forms import ActiveUserForm, NewsfeedForm
from user_app.models import ActiveUser, Newsfeed


def users(request):
    activeuser = request.user.activeuser
    data = {'activeuser': activeuser}
    return render(request, "users/users.html", data)


def user_profile(request):
    activeuser = request.user.activeuser
    data = {'activeuser': activeuser}
    return render(request, "users/user_profile.html", data)

def users_home(request):
    activeuser = request.user.activeuser
    data = {'activeuser': activeuser}
    return render(request, "users/user_home.html", data)


def new_user(request):
    if request.method == "POST":
        form = ActiveUserForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/users")
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
    newsfeed = Newsfeed.objects.all()
    data = {'form5': form5, 'newsfeed': newsfeed}
    return render(request, "users/newsfeed.html", data)


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