# Django: Other Topics

There are still many topics to learn:
- ORMs
- Advanced User Authorization
- Social Login e.g. through Facebook)
- Payments
- REST APIs
- Encryption
- Testing
- Sessions
- Cookies
- Class-based views
- ...

We will cover these topics in a mix of clone projects and the "Advanced" Django Topic Sections


# Django Deployment

### Deployment Options
There are many options for deploying your site, and each option comes with trade-offs on price, scalability, security, ease of use, etc...
**Deploying to Python Anywhere**: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
**Deploying to Heroku Guide**: https://devcenter.heroku.com/articles/deploying-python
**Deploying to Amazon Web Services**: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
**Deploying to VPS with Digital Ocean**: https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps

In this lecture we will see how to deploy with a very simple and easy to use host: pythonanywhere.com; later we will see how to deploy to a VPS like Digital Ocean or another hosting service like Heroku.

Understanding this basic process on a simple site like pythonanywhere.com will really help you when it comes to deploying on more technical platforms. If you are interested in deploying to a particular platform or service, usually a simple google search of the service name plus Django will result in many guides.
It is in the best interest of these services that well writtend deployment guides are available, otherwise they won't make any money.

When we think about deploying our project, it is useful to have your code hosted somewhere online: this way we can easily call it from the virtual server or hosting service we are using.

# pythonanywhere.com
Here: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
click on "pricing and signup"
sign up and create a free account

We will try to deploy the project that you find here:
*/home/elisa/bitbucket/altro/github-django-deployment/django-deployment-exercise*
which contains a copy of the project:
*/home/elisa/bitbucket/altro/django-course-udemy/07_Django_04_Templates/templproject*


my username: elisabattistoni
psw: usual
email: eli.battistoni@gmail.com

(https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
In the *Console* tab, click on *bash* which opens a console
```
$ mkvirtualenv --python=python3.10 myproj
$ pip list
$ pip install -U django==4.1.1
$ git clone https://github.com/elibattistoni/django-deployment-exercise.git
$ clear
$ ls
$ cd django-deployment-exercise/
$ cd templproject/
$ python manage.py migrate
$ python manage.py makemigrations templapp
$ python manage.py migrate
$ python manage.py createsuperuser
```
for the superuser:
elisa
eli.battistoni@gmail.com
elisapassword
now you are ready to set up your application and that involves setting up the WSGI settings (i.e. tell pythonanywhere to serve my applicatin if someone visits my page).

- Go to the Dashboard and click on the *Web* tab; click on *add a new web app*
- Click on *manual configuration*
- This will redirect you to *https://www.pythonanywhere.com/user/elisabattistoni/webapps/#tab_id_elisabattistoni_pythonanywhere_com*
- click on *Configuration for elisabattistoni.pythonanywhere.com*
- then go back to return to the web app setup page (https://www.pythonanywhere.com/user/elisabattistoni/webapps/#tab_id_elisabattistoni_pythonanywhere_com)
- go to the section *Virtualenv* and click on *Enter path to a virtualenv, if desired* and enter */home/elisabattistoni/.virtualenvs/myproj*

Now set up the source code. Go to the *Code* section. Set up the link to the project folder. If you forgot, click on *Start a console in this virtualenv*. Get the path, i.e. "/home/elisabattistoni/django-deployment-exercise/templproject" and paste it into *Source code: Enter the path to your web app source code*

Set up the WSGI file: always in the Console section, click on "WSGI configuration file: ....."
This will open up an editable python file:
delete everything that relates to the hello world page (from line 13 to line 47)
uncomment the part of django
change the path:
path = '/home/elisabattistoni/mysite'
to
path = '/home/elisabattistoni/django-deployment-exercise/templproject'

So, overall the django part should be changed in this way:
```
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/elisabattistoni/mysite/mysite/settings.py'
## and your manage.py is is at '/home/elisabattistoni/mysite/manage.py'
path = '/home/elisabattistoni/django-deployment-exercise/templproject'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","templproject.settings")
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

In the navbar click on *Web* and click on the link as above (*elisabattistoni.pythonanywhere.com*).

If you go to *Admin* in your web app, you see that the formatting is not good. You need to tell pythonanywhere where to find the static files.
Go to the *Web* tab and go to the Static files section. You need to add two static files:
1) the static files for the admin page
2) for your own pages
The static for the admin is usually always the same: in the URL column, add: **/static/admin/**; in the Directory column, add: **/home/elisabattistoni/.virtualenvs/myproj/lib/python3.10/site-packages/django/contrib/admin/static/admin**
Set up the link to the other staticfiles for your project:
URL: **/static/**
Directory: /home/elisabattistoni/django-deployment-exercise/templproject/static


Remove debug mode. Go to the tab *Files* and navigate to the settings.py file of the templproject
(https://www.pythonanywhere.com/user/elisabattistoni/files/home/elisabattistoni/django-deployment-exercise/templproject/templproject/settings.py?edit)
and set Debug equal to False.
