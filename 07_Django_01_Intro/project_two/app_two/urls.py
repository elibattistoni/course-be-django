from django.urls import path
from app_two import views

urlpatterns = [
    path("", views.specific_app_view, name="specific_app_view"),
]
