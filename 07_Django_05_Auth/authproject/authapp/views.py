from multiprocessing.util import is_abstract_socket_namespace
from django.shortcuts import render
from authapp.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, "authapp/index.html")


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(
                user.password
            )  # this goes into the settings.py file, and uses a specific hasing method to hash the file
            user.save()

            profile = profile_form.save(
                commit=False
            )  # False because you don't want to save on DB because otherwise you will get errors as it tries to override the user
            profile.user = user  # this sets up the one to one relationship

            if "profile_pic" in request.FILES:
                #! you have to use request.FILES whenever you are uploading a csv, pdf, image,...
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True

        else:
            # if any of the two forms is invalid
            print(user_form.errors, profile_form.errors)
    else:
        # in this case it was not an HTTP request, there was no POST
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "registered": registered,
    }
    return render(request, "authapp/registration.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")
    else:
        # i.e. if they have not submitted anything
        return render(request, "authapp/login.html", {})

#! show the logout page only if a user has logged in
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))