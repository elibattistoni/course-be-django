from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def example_view(request):
    return HttpResponse("<em>My Second App - INITIAL VIEW</em>")


def image_view(request):
    # in the browser go to /app_one
    rendering = render(request, "app_one/show_image.html")
    return rendering