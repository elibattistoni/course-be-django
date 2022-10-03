from django.urls import path
from app_one import views

urlpatterns = [
    path("", views.image_view, name="image_view"),
]
