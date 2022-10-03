from django.shortcuts import render
from usersapp.models import User
from usersapp import forms

def index(request):
    rendering = render(request, "index.html")
    return rendering

def homepage(request):
    rendering = render(request, "usersapp/homepage.html")
    return rendering

def signup(request):
    form = forms.SignupForm()
    
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return homepage(request) # return to homepage
        else:
            print("error: form invalid")

    rendering = render(request, "usersapp/signupform.html", {"form": form})
    return rendering

def users_list(request):
    
    users_list = User.objects.all().order_by("last_name")
    users_dict = {"users": users_list}
    rendering = render(request, "usersapp/users_list.html", context = users_dict)
    return rendering