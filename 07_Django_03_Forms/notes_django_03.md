## HTTP, GET, POST
we are going to use HTTP, GET, POST to connect our form to the backend:

- **HTTP** (Hypertext Transfer Protocol) is designed to enable communication between a client and a server: the client submits a request, the server then responds. The most commonly used methods for this request/response protocol are GET and POST
- **GET** requests data from a resource
- **POST** submits data to be processed to a resource

Check https://www.w3schools.com/tags/ref_httpmethods.asp for more details (e.g. what remains in browser history, what can be cached for future use)

# Django Forms

In this section we will cover how to use Django Forms to accept User Input and connect it to the database and retrieve it later on.


Advantages of Django Forms:
- quickly generate HTML Form widgets
- validate data and process it into Python data structure
- create Form versions of our Models, quickly update models from Forms

The first thing we need to do is to create a forms.py file inside the application. After that we call Django's built in form classes (it looks very similar to creating models).

Example of code inside *forms.py*

```
from django import forms

class FormName(forms.Form):
    name = forms.Charfield()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
```

Now that we have the form created inside the application's forms.py file, we need to show it by using a view.

Inside the *views.py* file we need to import the forms.
There are two ways to do this:
`from . import forms` (the . indicates to import from the same directory as the current .py file)
or
`from forms import FormName`

Then we can create a new view for the form
```
def form_name_view(request):
    form = FormName()
    return render(request,"form_name.html",{"form":form})
```

Then we add the view to the app's urls either directly or with include()
Directly (in the *urls.py of the app*)
```
from app import views
urlpatterns = [
    url(r"formpage/", views.form_name_view, name="form_name")
]
```

We can then create the templates folder along with the html file that will hold the template tagging for the form (**remember to update the settings.py file to reflect the TEMPLATE_DIR variable and also remember that your views should reflect subdirectories inside templates**)

Then go into the form_name.html file inside the templates folder and add in the actual template tagging that will create the Django Form.

There are several ways you can inject the form using template tagging.
1) you can pass in the key from the contect dictionary: `{{ form }}`
Now you should be able to see a very basic and ugly form on the page
However, there is no <form> tag there
A more complete form page:
`form.as_p` uses <p> (paragraph) which allows to have a nicer layout

```
<div class="container">
    <form method="POST">
        {{ form.as_p }}
        {% csrf_token %}
        <input type="submit" class="btn btn-primary" value="Submit">
    </form>
</div>
```

**{% csrf_token %}** is about site security measures: it is a Cross-Site Request Forgery (CSRF) token, which secures the HTTP POST action that is initiated on the subsequent submission of a form. So, when you click submit, you have this cross-site request forgery token that helps protect the user or your website from getting false data or from a user accidentally sending that data somewhere else.
The Django framework *requires* the CSRF token to be present (if it is not there, the form does not work): it works by using a "hidden input" which is a random code and checking that it matches the user's local site page.

### How to handle the form in a view
We need to inform the view that if we get a POST back, we should check if the data is valid and if so, grab that data.
We can do this by editing the view; we will talk a lot more about form validation later on, but upon receiving a validated form, we can access a dictionary like attribute of the "cleaned_data"

# Form Field Validation
**Hidden fields and how we can use them for custom field validation**
The form that we have right now is pretty open to not only users but also potential bots.
Django has built-in validators you can use to validate your forms (to check user's response or check for bots).
All this part is limited to the *forms.py* file. We will add:
- a check for empty fields
- a check for a bot
- a clean method for the entire form

A hidden field is somthing that remains in the HTML but is actually hidden from the user; and a lot of times we can use these to try to catch malicious bots on our website.

# Model Forms
We have seen that we can use Django Forms to grab information from the user and then do something with it. So far we've only printed out that information, but what if we want to save it to a model? e.g. a user that signs up in a website, we want to save that information to a model in the DB.

Instead of inheriting from the *forms.Form* class, we will use *forms.ModelForm* in our *forms.py* file.
The **forms.ModelForm helper class** allows us to create a form from a **pre-existing model**; we then add an inline class called **Meta** that provides information connecting the model to the form.

```
from django import forms
from myapp.models import myModel

class MyNewForm(forms.ModelForm):
    
    # !!! form fields go here
    
    class Meta:
        model = MyModel
        fields = # let's see the options!
```
the *fields* attribute will connect to model; there are many ways to make this connection.
You need to carefully think about **security** for fields!
You can have the form directly be generated from the model, without the need of specifying the fields (# !!! form fields go here). But if you want to use custom validators, then you have to pass those fields with the validators params. Otherwise the constraints of your field inside the definition of that model will act as validators.

#### option 1: set fields = "__all__"
```
from django import forms
from myapp.models import myModel

class MyNewForm(forms.ModelForm):
    
    # !!! form fields go here
    
    class Meta:
        model = MyModel
        fields = "__all__"
```
with __all__ you grab all fields of the model and place them into the form.

#### option 2: exclude certain fields
```
from django import forms
from myapp.models import myModel

class MyNewForm(forms.ModelForm):
    
    # !!! form fields go here
    
    class Meta:
        model = MyModel
        exclude = ['field1','field2']
```
#### option 3: pass the included fields
```
from django import forms
from myapp.models import myModel

class MyNewForm(forms.ModelForm):
    
    # !!! form fields go here
    
    class Meta:
        model = MyModel
        fields = ('field1','field2')
```


We will work on the usersapp, which had the User Model.
We are going to add a sign up page: connected to a ModelForm, the user will sign up on the user page and be taken back to the home page.
