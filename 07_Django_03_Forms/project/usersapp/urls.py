from django.urls import path
from usersapp import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("home", views.homepage, name="homepage"),
    path("signup", views.signup, name="signup"),
    path("users", views.users_list, name="users_list")
]