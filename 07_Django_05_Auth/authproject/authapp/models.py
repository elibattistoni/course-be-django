from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    # create relationship (do not inherit from User!)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # this means that this extra user profile info has a one to one relationship with the user model

    # add any additional attributes you want
    portfolio_site = models.URLField(blank=True)  # i.e. optional
    profile_pic = models.ImageField(
        upload_to="profile_pics", blank=True
    )  # media/profile_pics/

    def __str__(self):
        # built-in attribute of django.contrib.auth.models.User
        return self.user.username
