# Class Based Views (CBV)

Previously we have created views using functions, however Django provides really powerful tools to use OOP and classes to define views.
The CBV offers great functionality and for most experienced users of Django, it is their default choice for creating views.

We will talk also about mix-ins.

# Django View Class
We will use the simplest available Django View Class:

In the *views.py* file we will import this:
`from django.views.generic import View`

We will also have to lightly change the way we call a class based view in the *urls.py* file:
we will add `.as_view()` call off the class (this is an inhrited method of the View class)

# Template Views with CBV
Let's use the **TemplateView** that comes with Django.
There is a big difference between using a function to call a template versus the TemplateView.

*Function Based View*:
```
def index(request):
    return render(request,"index.html")
```

*Class Based View*:
```
class IndexView(TemplateView):
    template_name = "index.html"
```

# Detail View and List View

We have seen how to use CBVs to directly show a template, but what about models? Often, when we have models, we want to either list the records from the model, or show details of a single record.
Previously we did this wih calls using the Object Relation Mapper directly. This included things like: `MyModel.ibjects.all()` (this is how to connect the template to a call to show information from the db).
Since these operations are very common, Django has some generic view classes you can inherit to very quickly display information from your model: this is where the power of CBV comes to help us.

In this part we will create:
- New Models
- New Templates

Then we will focus on:
- **ListView**
- **DetailView**

Previously we have been putting all templates inside the templates folder within the matching app folder.
However, it is also common practice to have a template folder inside the app's folder (i.e. each application has its own templates folder inside).

- Let's create the models in the models.py file of the cbv_app.
- Register the models in the *admin.py* file inside the cbv_app
- create superuser
        Username (leave blank to use 'elisa'): 
        Email address: eli.battistoni@gmail.com
        Password: elisa
- create a population script (populate_models.py) and run it with python populate_models.py
- create a templates folder inside the cbv_app; this is another convention: in the templates folder of the project insert the html files that do not belong to the app; in the templates folder of the app insert the html files that belong to the app

# Important
For the Student model, we have defined a foreign key (School) but we did not define a primary key (it would not make sense to define a primary key e.g. with the name because the name is shared). Django automatically creates (if not specified otherwise) a primary key that is the id of the record (a serial number marker, i.e. increasing integer).
So if you call .id on the mìobject model, you will get the primary key id. Same goes for the model School (we did not define, at first, a primary key):
```
class School(models.Model):
    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name
```