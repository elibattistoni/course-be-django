from django.urls import path
from app_one import views

urlpatterns = [
    path("show_image", views.image_view, name="image_view"),
    path("show_models", views.models_view, name="models_view"),
]
