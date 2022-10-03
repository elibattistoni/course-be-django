# User Authentication
In this section we will focus on User Authentication.

So far we have created applications that assume everyone will see the same page.

Django has many available tools and external packages that enhance functionality.

We will mainly focus on the available tools:
- Users and User Model
- Permissions
- Groups
- Passwords and Authentication
- Loggin In and Out


¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
# Django Passwords
We will discuss the general setup to begin getting ready for User Authentication.
We will talk about passwords in general and also discuss some additional library options for security.

The first thing we need to take care of is setting up our ability to authenticate a User: we need to use some built-in apps and make sure they are under the **INSTALLED_APPS** list in *settings.py*.
These apps are: **django.contrib.auth** and **django.contrib.contenttypes**
Often they are already pre-loaded in the list, but if you add them, remember to migrate.

The next thing we need to do is make sure we store our passwords safely. **Never store a password as plain text!**
We will begin by using the default **PBKDF2 algorithm** with an **SHA256 hash** that is built-in to Django.
This is quite secure for most aplications, because it requires a massive amount of computing power to crack it.
But if you want more security you can upgrade to even more secure hashing algorithms.
Django makes this really easy: we will see how to use the **bcrypt library** and the **Argon2 library**.
In your virtual environment:
```
pip install bcrypt
pip install django[argon2]
```
Depending on your Django version, you may already have these installed (these are if you want super secure hashing algorithm).
In *settings.py* you can pass in the list of **PASSWORD_HASHERS** to try the hashing algorithms in the order you want to try them.
If for some reason you don't have the library support, it will not throw an error, but you will fall back on to the original PBKDF2 (which is built-in in Django).
```
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]
```

Sometimes users will also try to use a very weak password, such as "password123". We can also add a validator to prevent a user from doing that. We'll keep things simple and only require a minimum length for now.

### SHA
##### What an SHA looks like?
Go to www.xorbin.com/tools/sha256-hash-calculator

SHA = Secure Hash Algorithm
designed by the NSA (National Security Agency)
it is a cryptographic hash function that can run on ditigal data.
How it works: you input a string, it passes through the algorithm, it gets converted to a hash, this hash is used to compare to other input hash data. So the user will input their password and we will save its hash. So, if someone enters our DB and steal the data, they steal the hash of the user passwords, not the passwords themselves. And it is extremely difficult to convert the hased string into the original string.

### Password validators
In the *settings.py* file after the password hashers, you can define all the passwords contraints/validators:
https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
```
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length":9} #! you an add options like these, check documentation
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
```

### MEDIA_DIR
In the *settings.py* file:
```
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
STATIC_DIR = os.path.join(BASE_DIR,"static")
MEDIA_DIR = os.path.join(BASE_DIR,"media")
```
Usually you want to have also a media directory in which you can store e.g. the pictures and things that an user uploads.
You want to keep separated the media that the user uploads from the static media files that you define in your project.
So, static is stuff that belongs to you as website creator and administrator; media is stuff that more or less belongs to the users.

In the *settings.py* file add:
```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = "static/"
STATICFILES_DIR = [STATIC_DIR,]

# Media
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = "/media/"
```

¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
# User Models
We will discuss how to use Django built-in tools to create User Authorization Models.
We will also discuss how to set-up media files in your project.

Previously when we have logged on to the Amdin page, we have seen that there is already a built-in Authentication and Authorization model set in place.
In the DB there were "Users" and "Groups".

P.S. Better not to name "Users" one of your models, in order to avoid confusion.

The built-in **User** object has a few key features:
- Username
- Email
- Password
- First Name
- Surname
There are also some other attributes for the **User** object, such as `is_active`, `is_staff`, `is_superuser`.

Sometimes you will also want to add more attributes to a user, such as their own links or profile image. You can do this in your application's *models.py* file by creating another class that has a relationship to the **User** class.

NB for the one to one field: https://docs.djangoproject.com/en/4.1/topics/db/examples/one_to_one/

Example inside the *models.py* file:
```
from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    # create relationship (do not inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE) # this means that this extra user profile info has a one to one relationship with the user model

    # add any additional attributes you want
    portfolio_site = models.URLField(blank=True) #i.e. optional
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) # media/profile_pics/

    def __str__(self):
        # built-in attribute of django.contrib.auth.models.User
        return self.user.username
```
The ImageField will allow you to store images to a model, typically we will keep this kind of content uploaded by the user in the media folder.
In order to work with images with Python we need to install the Python Imaging Library with:
`pip install pillow`

Once you have created the extension of the User model, you have to register it in the *admin.py* file with:
`admin.site.register(UserProfileInfo)` then run:
- `python manage.py migrate`
- `python manage.py makemigrations`

**Typically images, CSS, JS, etc all go in the static folder of your project, with the STATIC_ROOT variable path defined inside of settings.py. User uploaded content will go to the media folder, with MEDIA_ROOT.**

Next we want to implement a Django form that the User can use to work with the website. An example inside *forms.py* would be:
```
from django import forms
from django.contrib.auth.models import User
from authapp.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")
```

Let's code through the set-up of what we have discussed:
- User Model
- Media Directory
- Handling Images
- User Form

¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
# Registration: see the views.py file

¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
# Logging in and out

Once a user is registered, we want to make sure that they can log in and out of the site.
We will go through the entire process of creating log in/ log out functionality.

This process involves:
- Setting up the login views
- Using built-in decorators for access
- Adding the LOGIN_URL in settings
- Creating the login.html
- Editing the urls.py files

NB: if you need a view to be shown only for users who have logged in, the view should be decorated with the following decorator:
from django.contrib.auth.decorators import login_required
@login_required
def kjgksjfgb:
    ...