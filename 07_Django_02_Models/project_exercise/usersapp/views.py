from django.shortcuts import render
from usersapp.models import User

def landing(request):
    rendering = render(request, "landing.html")
    return rendering

def homepage(request):
    rendering = render(request, "usersapp/homepage.html")
    return rendering

def users_list(request):
    
    users_list = User.objects.all().order_by("last_name")
    users_dict = {"users": users_list}
    rendering = render(request, "usersapp/users_list.html", context = users_dict)
    return rendering