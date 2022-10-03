from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def initial_app_view(request):
    return HttpResponse("<em>My Second App - INITIAL VIEW</em>")


def specific_app_view(request):
    # in the browser go to /app_two
    tags_dict = {
        "my_template_tag": "TEMPLATE TAG! Hello, I am from views.py in app_two"
    }
    rendering = render(request, "app_two/specific_app_view.html", context=tags_dict)
    return rendering