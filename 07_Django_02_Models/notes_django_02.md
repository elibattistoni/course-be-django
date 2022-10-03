### Topics

- models and databases and how to use them with django
- how to use the admin interface

<br/>

An essential part of any website is the ability to accept information from a user, input it into a db, retrieve information from a db, and use it to generate content for the user. We use **Models** to incorporate a database into a Django Project.

<br/>

# Django Models

- we can define models as just classes
- we use **Models** to incorporate a database into a Django Project
- Django comes equipped with **SQLite** (a SQL engine), which we'll use here, but Django can connect to a variety of SQL engine backends (POSTGRESQL, MYSQL)
- in the *settings.py* file you can edit the *ENGINE* parameter used for *DATABASES* (you can edit the engine backend in this file if you don't want SQLite)
- to create an actual model, we use a class structure inside of the relevant applications *models.py*:
    + this class object will be a subclass of Django's built-in class `django.db.models.Model`
    + each attribute of the class represents a field (like a column name with contraints in SQL)
- *models can reference each other* --> for this referencing to work, we use the concepts of *Foreign Keys* and *Primary Keys*
- e.g. we have 2 models (i.e. 2 tables in the db), one to store website information, another to store date information; we could say that the WebsiteId column is a primary key in the left table and foreign key in the right table:
    - *a primary key is a unique identifier for each row in a table*
    - *a foreign key just denotes that the column coicides with a primary key of another table*

<br/>

## Example fo the Model class

This example goes into the *models.py* file of your application

The two classes below (Topic and Webpage) inherit from the built-in `models.Model` class of Django

```
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

class Webpage(models.Model):
    category = models.ForeignKey(Topic)
    name = models.CharField(max_length=264)
    url = models.URLField()

    def __str__(self): # method that returns the name (if you do print(Webpage) it will return the name)
        return self.name
```

After you've set up the models, you can *migrate* the database --> this lets Django do the heavy lifting of creating SQL databases that correspond to the models we created.

1. Django can do this entire process with a simple command: `python manage.py migrate`;
2. Then register the changes to your app: `python manage.py makemigrations name_of_the_app`;
3. Migrate the database one more time: `python manage.py migrate`

You can then use the shell from the *manage.py* file to play around with the models.

<span style="color:green">In order to use the more convenient Admin interface with the models,
you need to register them to your application's *admin.py* file.</span>

```
from django.contrib import admin
from name_of_the_app.models import Model1,Model2 # in the previous example is Topic,Webpage

admin.site.register(Model1)
admin.site.register(Model2)
```

Then with the models and database created, we can use Django's great Admin interace to interact with the database. **The Admin interface is one of the key features of Django**.
In order to fully use the database and the Admin, we will need to create a **superuser**; we can do this with the following: `python manage.py createsuperuser`. Then you have to provide a name, email and password.

Once you've set up the models, it's always good idea to populate them with some test data. We will use a library ("Faker") to help with this and create a script.

<br/>

## Creating Models

We will contiue working with the 2 project folders from Django Level One.

1. Open **models.py** at *07_Django_02/project_one/app_one/models.py* and write 3 models (see file)
        NB: https://docs.djangoproject.com/en/4.1/ref/models/fields/

2. **Create the SQL databases** behind these modules: you just need some commands and Django will do the hard work:
    - In the terminal, under *07_Django_02/project_one/*, run: `python manage.py migrate`
    - Register the changes to your app: run `python manage.py makemigrations app_one` (if you have only one app, you do not need to specify also 'app_one' otherwise you should)
    - Migrate the database one more time: run `python manage.py migrate`

3. Check: open an interactive console with:
    ```
    python manage.py shell
    from app_one.models import Topic
    print(Topic.objects.all())
    t = Topic(top_name="Social Network")
    t.save()
    print(Topic.objects.all())
    quit()
    ```

4. Add and view data with the *admin interface*. We are not going to use the shell every time we want to add something, view the models or get an idea of what the DB contains. A more convenient way is the admin interface. In order to have the admin interface with the models, we need to register them to the application.
   Register the models to your app *admin.py* file (*07_Django_02/project_one/app_one/admin.py*) and see the code written
   (the aim with this code is to tell the application that your models exist)
   In *admin.py*:
   ```
   from django.contrib import admin
    from app_one.models import Topic, Webpage, AccessRecord

    admin.site.register(Topic)
    admin.site.register(Webpage)
    admin.site.register(AccessRecord)
   ```

5. In order to fully use the database with the Admin interface, you need to create a **superuser** so that there is some security on who can access the db.
   ```
   python manage.py createsuperuser
   ```
   Username: elisa
   Email address: elisa.battistoni@bluetensor.ai
   Password: Elis9194

   Run the server and check the admin interface in the browser.
   `python manage.py runserver`

    if you go to http://127.0.0.1:8000/admin you get a login page where you can provide username and password (defined above), you can use the admin interface to add data, e,g you created anew Webpage called Google.

<br/>

# Populating Models

It's usually a good idea to create a script that will populate your models with some dummy data; let's use the Faker library to create this script.

- `pip install Faker`
- in *07_Django_02/project_one*, create a file named *populate_app_one.py* and look at the code inside
- in the terminal:
  - `cd course_2022/07_Django_02/project_one/`
  - `python populate_app_one.py`
- now let's test it: run `python manage.py runserver`, then go to the  page http://127.0.0.1:8000/admin


<br/>

# Models - Templates - Views (MTV) Paradigm

Django operates on what is known as Models - Templates - Views paradigm (MTV in short).
This MTV paradigm encompasses the idea of how to connect everything we've talked about so far: models, templates and views.

There are a few basics steps to achieving the goal of serving dynamic content to a user based off the connection of the models, views and templates.

1. In the *views.py* file: import the models we want to use;
2. Use the view to query the model for data that we want;
3. Pass results from the model to the template;
4. Edit the template so that it is ready to accept and display the data from the model;
5. Map a URL to the view.

We can practice this methodology by changing what we display on the front index page. To begin our understanding of this process we will start by generating a table on that index page.
The table will display all the webpages and access records from the AccessRecord database we created and populated. We will use template tagging to connect the model to the html page.


1. Open the file *07_Django_02/project_one/app_one/views.py*: and add the `models_view` function which calls the models and returns the context in an html in *07_Django_02/project_one/templates/app_one/show_models.html*

2. Open the html in the templates folder and insert the template tags like in the code; style the linked css file

3. In *07_Django_02/project_one/app_one/urls.py* add the path to the view