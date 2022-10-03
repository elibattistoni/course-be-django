from django.urls import path
from authapp import views

# SET UP TEMPLATE TAGGING!!
# django will automatically look for app_name
# tells django to look into templapp and find the urls that match
app_name = "authapp"

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.user_login, name="user_login"),
]
