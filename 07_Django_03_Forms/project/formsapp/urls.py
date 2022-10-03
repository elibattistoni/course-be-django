from django.urls import path
from formsapp import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("home", views.homepage, name="homepage"),
    path("basicform", views.basic_form, name="basic_form"),
]