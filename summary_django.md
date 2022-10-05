# Summary of Django commands
pip install django==4.1.1

https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3

1. create the project folder and set up `django-admin startproject name_of_the_project`
2. `cd name_of_the_project`
3. Create a "templates" folder: `mkdir templates`
4. reate a "static" folder: `mkdir static`
5. In the settings.py file, add the path of the templates folder and the static folder:
    ```
    #------------------------------
    TEMPLATE_DIR = BASE_DIR.joinpath('templates')
    STATIC_DIR = BASE_DIR.joinpath('static')
    #------------------------------
    # in the templates section
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [TEMPLATE_DIR],
            .....
    #------------------------------
    # in the static section
    STATIC_URL = "static/"
    STATICFILES_DIRS = [
        STATIC_DIR,
    ]
    #------------------------------
    ```
6. `python manage.py runserver`
7. `python manage.py migrate`
8. create app with `django-admin startapp templapp`
9. inside the templapp folder, create a *urls.py* file
10. in the settings.py file, add `"templapp"` in the list of installed apps