from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from registration.models import User
from charity_app.forms import SignupForm, LoginForm
from charity_app.models import Video
from giver_app.forms import GiverForm
from giver_app.models import Giver



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
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
    return render(request, "givers/givers.html", data)

def login1(request):
    if request.method == "POST":
        form11 = LoginForm(request.POST)
        if form11.is_valid():
            user = authenticate(username=form11.cleaned_data['username'], password=form11.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("giver_home.html")

    else:
        form1 = LoginForm()
    data = {'form11': form11}
    return render(request, "login.html", data)


def index(request):
    data = {}
    return render(request, 'index.html', data)
@login_required
def givers(request):
    activeuser = request.user.activeuser
    data = {'activeuser': activeuser}
    return render(request, "givers/givers.html", data)

@login_required
def new_giver(request):
    if request.method == "POST":
        form3 = GiverForm(request.POST)
        if form3.is_valid():
            giver = form3.save(commit=False)
            giver.user = request.user
            giver.save()
            return redirect("/givers")
    else:
        form3 = GiverForm()
    data = {'form3': form3}
    return render(request, "givers/new_giver.html", data)

@login_required
def view_giver(request, giver_id):
    giver = Giver.objects.get(id= giver_id)
    data = {"giver": giver}
    return render(request, "givers/view_giver.html", data)

@login_required
def edit_giver(request, giver_id):
    giver = Giver.objects.get(id= giver_id)
    print giver
    if request.method == "POST":
        form3 = GiverForm(request.POST, instance= giver)
        print "POST"
        if form3.is_valid():
            if form3.save():
                return redirect("givers")
    else:
        form3 = GiverForm(instance= giver)

    data = {"giver": giver, "form3": form3}
    print form3
    return render(request, "givers/edit_giver.html", data)

@login_required
def delete_giver(request, giver_id):
    giver = Giver.objects.get(id= giver_id)
    giver.delete()
    return redirect("/givers")

@login_required
def giver_profil(request):
    giver = request.user.giver
    print giver.name
    data = {'giver': giver}
    return render(request, "givers/giver_profile.html", data)

@login_required
def giver_page(request):
    return render(request, "givervideos/all_videos_giver.html")
@login_required
def giver_info(request):
    giver = request.user.giver
    print giver.name
    activeuser = request.user.activeuser
    data = {'giver': giver, 'activeuser': activeuser}
    print activeuser.name
    return render(request, "givers/giver_info.html", data)