# High level overview of Django
https://kruizerchick.gitlab.io/static/images/dj_overview.png

Startup:
- create virtual environment, activate it
- install Django (when you install Django, it also installs a command line tool called *django-admin*, see the commands below)

<br/>

# Steps to create a Django App

### 1. create the project folder with the command

`django-admin startproject name_of_the_project`

`cd name_of_the_project`

inside the new project folder, you will find several .py files. 
The *wsgi.py* file is a Python script that acts as the 
Web Server Gateway Interface (it will later on help us deploy our web app to production)

### 2. Run the project to test the installation of Django

`python manage.py runserver`

`python manage.py migrate`

- a *migration* allows you to move databases from one design to another (this is also reversible)
(so far you have only installed Django and tested the installation of Django)
- a *Django Project* is a collection of applications and configurations that when combined together will make up the full web application (your complete website running with Django).
- a *Django Application* is created to perform a particular functionality for your entire web application. e.g. you could have a registration app, a polling app, comments app, etc. These Django Apps can then be plugged into other Django Projects, so you can reuse them (or use other people's apps).

### 3. Create a simple Django app

`python manage.py startapp name_of_the_app`

- in the *admin.py* file you can register the models that Django will use to create the Django's Admin interface
- in the *apps.py* you can insert application-specific configurations
- in the *models.py* you store the application's data models
- in the *tests.py* file you can insert the tests for your application
- in the *views.py* file you have functions that handle requests and return responses
- the *migrations* folder stores database specific information as it relates to the models

So the *views.py* and *models.py* are application-specific.

You have to tell Django the existence of this application:
in the *settings.py* file in the project folder add *name_of_the_app* in the list of the *INSTALLED_APPS*.

# COMMANDS FOR STARTING THE PROJECT
```

django-course-udemy$ source env/bin/activate

django-course-udemy$ cd course_2022/07_Django_01/project_two/

django-course-udemy/course_2022/07_Django_01/project_two$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 24, 2022 - 08:47:10
Django version 4.1, using settings 'project_two.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
### 4. Create a view

Go to the *views.py* file in the app folder and create a simple view (a view is a function or class that has the purpose of displaying the output on the webpage).

In order to see the view you just created, you have to map this view to the *url.py* file in the project folder.
- **from name_of_the_app import views**

add this in the urlpatterns list:
- **path("", views.initial_app_view, name="initial_app_view")** which maps that application's view to this url

### 5. Double URL mappings

We previously saw a very direct mapping from the views.py (app folder) to the urls.py (project folder).

Now we want to use the ability of using the *include()* function from *django.conf.urls*

The *include()* function allows to look for a match with regexp and link back to our app's *urls.py*. This allows every application to have its own *urls.py* file (NB: you have to manually add this file in the *app folder*; on the contrary of the urls.py file in the project folder which is automatically created). This is also good practice to keep everything modular.

- in the the *urls.py* file *of the project folder*:
    - import the include function with **from django.conf.urls import include**
    - add the included url patterns: **urlpatterns = [..., path("app_two/",include("app_two.urls")), ..]** the include() function tells Django to look at the *urls.py* file inside the app_two folder
- create a *urls.py* file *in the applciation "app_two" folder*:
    - **from django.urls import path**
    - **from app_two import views**
    - **urlpatterns = [ path("", views.specific_app_view, name="specific_app_view") ]**
- run **python manage.py runserver** and if in the browser url you add **app_two** you wil be redirected to the view whose url is defined in the urls.py of the app folder


<br/>

# Templates -- connecting HTML pages to the views (example in project_two)

*Templates* contain the static parts of the html page (the skeleton of the page).

*Template tags* have their own special syntax, and this syntax allows to inject dynamic content that your Django App's will produce, effecting the final HTML.

- Create a templates directory, and a subdirectory for each specific app's templates:
  - *project_two/templates/app_two* (inside the project folder)

- in the *settings.py* file in the *project folder*, tell Django about the templates by editing the *DIR* key inside of the *TEMPLATES* dictionary:
  - **TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")**
  - add **TEMPLATE_DIR** inside the list of the **TEMPLATES** dictionary

- add html templates in the templates directory (and subdirectories -- one per app)
  - create an html file called *initial_app_view.html* inside of the */templates/app_two* folder; along with normal HTML, in this file we will insert template tags (a.k.a. *Django Template Variable*) and this template variables will allow us to inject content into the html directly from Django. i.e. in the *TEMPLATE_DIR* file, in the body, we insert the following template tag **{{ insert_me }}**
  - you have to connect the variable **insert_me** to the actual project and our app. In order to do this, i.e. to use Python code to inject content into the HTML, we use the **render()** function and place it into the function for our view in the *views.py* file. Edit the *views.py* file of the app, specifically the function for the view. NB: **you should separate our templates per application**.

<br/>

# Django Static Files -- Inserting static media files (example in project_one)

So far, we've used **templates** and **template tags** to insert simple text.

But what about other types of media, e.g. photos?

1. Create a **/static/** folder, at the same level of the templates folder (i.e. in the project directory). Add one subdirectory for each app. Inside each of these subdirectories, create a directory named **/images/**, and place an image inside it.
2. in the *settings.py* file in the project folder, add:
   1. the **path** of the static directory:
        ```
        STATIC_DIR = BASE_DIR.joinpath('static')
        ```
   2. below the **STATIC_URL** variable at the bottom of the file, add **STATICFILES_DIRS** (check that it does not exist already), so it should look like this:
        ```
        STATIC_URL = "static/"

        STATICFILES_DIRS = [
            STATIC_DIR,
        ]
        ```
   3. in the browser go to the url **http://127.0.0.1:8000/static/app_one/images/mountain.jpg**

But let's use template tags for loading images inside the HTML:
  - at the top of the HTML (after the <!DOCTYPE html> line) in which you want to show the file, add **{% load staticfiles %}** (for Django 4.1 **{% load static %}**)
  - insert the image with: **<img src={%static "images/mountain.jpg" alt="Uh Oh, didn't show!" %} />** or **<img src="{%static "app_one/images/mountain.jpg" alt="Uh Oh, didn't show!" %}" />**

A static file can also be CSS or Javascript:
- in the 'static/app_one' folder, create a 'css' folder and inside of it, a css file named 'mystyle.css'
- in the html file show_image.html insert **<link rel="stylesheet" href={% static "app_one/css/mystyle.css" %}>** or **<link rel="stylesheet" href="{% static "app_one/css/mystyle.css" %}">**