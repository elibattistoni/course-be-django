from django.urls import path
from usersapp import views

urlpatterns = [
    path("home", views.homepage, name="homepage"),
    path("users", views.users_list, name="users_list")
]