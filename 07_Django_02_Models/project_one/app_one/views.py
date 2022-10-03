from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import Topic, Webpage, AccessRecord

"""
urls: http://127.0.0.1:8000/
urls: http://127.0.0.1:8000/app_one/
urls: http://127.0.0.1:8000/static/app_one/images/mountain.jpg
"""


# Create your views here.
def example_view(request):
    return HttpResponse("<em>My Second App - INITIAL VIEW</em>")


def image_view(request):
    # in the browser go to /app_one
    rendering = render(request, "app_one/show_image.html")
    return rendering

def models_view(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dictionary = {"access_records":webpages_list}
    rendering = render(request, "app_one/show_models.html", context = date_dictionary)
    return rendering
