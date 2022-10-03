# TEMPLATES

So far we have only used templates as a way of injecting simple pieces into our HTML files; but templates are capable of much more.

For example, so far we have been manually creating everything individually for each .html file; however, we can use templates to have a "base" template nad inherit that template in the .html files.

This saves you a lot of time and will help create a unified look and feel across every page of your website.

Templates are also used to solve issues with relative paths and working with variables:
- templates can help solve issues by avoiding hard-coded URL paths
- templates come with built-in filter capabilities so you can adjust variables on the actual individual page

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
# Relative URLs with Templates

So far when we have had to use an anchor tag with an href we have passed in a hardcoded path to the file (we have written the path to the html file or in the view); but this is poor practice if we want our Django project to work on any system.

How can we replace a hardcoded URL path in an href with a URL Template?

#### Option 1: using urls tags
Previously:
```
<a href="basicapp/thankyou">Thanks</a>
```
Can be changed into:
```
<a href="{% url 'thnks' %}">Thanks</a>
```
and `name='thnks'` is in the urls.py file

#### Option 2: using views tags
Previously:
```
<a href="basicapp/thankyou">Thanks</a>
```
Can be changed into:
```
<a href="{% url 'basicapp.views.thankyou' %}">Thanks</a>
```

### Option 3: in the urls.py file (most future-proof method)
- in the *urls.py* file, add the variable **app_name**
- set this variable equal to a string that is the same as you app name
Previously:
```
<a href="basicapp/thankyou">Thanks</a>
```
Can be changed into:
```
<a href="{% url 'basicapp:thankyou' %}">Thanks</a>
```
This requires that app_name variable to be created inside the urls.py file.

**Using templates for relative URLs will really help in projects with multiple applications.**

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
# URL Template Inheritance
We can use Django Template Inheritance to practice DRY coding principles:

**DRY = Don't Repeat Yourself**

**Template Inheritance allows us to create a base template we can inherit from.**

Template Inheritance saves us a lot of repetitive works and makes it much easier to maintain the same base look and feel across our entire website.

For example, if we wanted a navbar at the top of our page, it would not make sense to continually have the same navbar HTML code in each individual .html file. Instead we set it to the *base.html* file and inherit it using template inheritance.
This idea is sometimes also known as **template extending**, as in extending the base.html to other .html files.
The inheritance does not need to just be limited to one base.html file, **you can extend multiple templates.**

Before you begin any Django project, it is always a good idea to sketch out the main idea and organization by hand. This will help you realize what can be used for template inheritance and what applications you should create.

The main steps for inheritance:
1. Find the repetivive parts of your prject
2. Create a base template of them
3. Set the tags in the base template
4. Extend and call those tags anywhere

In *base.html*: all things that you want the other pages to inherit
```
<links to JSS, CSS, Bootstrap>
<bunch of html like navbars>
    <body>
        {% block body_block %}
        {% endblock %}
    </body>
</More footer html>
```

In *other.html*: all things specific for individual pages
```
<!DOCTYPE html>
{% extends "templapp/base.html" %}
{% block body_block %}
<HTML specific for other.html>
<HTML specific for other.html>
{% endblock %}
```

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
# Templates Features and Filters

Imagine that you had some information from your model that you wished to use across various views/pages, but perhaps you wanted to make a slight edit to the information before injecting it, like string operations, or arithmetic.

Django provides many template filters that allow you to affect the injection before displaying it to the user: this allows for flexibility from a single source (so you do not have to worry about editing the source from the Python side).

The general form for a template filter is:
`{{ value | filter:"parameter" }}`
NB: not all filters take in parameters, and many of these filters are based off of common built-in Python functions.

Django filters: https://docs.djangoproject.com/en/4.1/topics/templates/#filters

Built-in filters: https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#ref-templates-builtins-filters

Creating custom filters: https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/#howto-writing-custom-template-filters

### Custom filters
1. Create a new folder inside the templapp folder, called **"templatetags"** with therefore path "templproject/templapp/templatetags" **This is a convention that you should folow!!**
2. Inside this folder, create an *__init__.py* file and another file (with any name you want, here *custom_filters.py*) in which you will write your functions
3. In the html in which you want to use the custom filters, add `{% load custom_filters %}`

Example of *custom_filters.py*:
```
from django import template

# register this script
register = template.Library()

# my custom function filters
#@register.simple_tag # it should be this or register.filter(...) after the function
def cut(value,arg):
    """This cuts out all the values of 'arg' from the string

    Args:
        value (_type_): _description_
        arg (_type_): _description_
    """
    return value.replace(arg,"")

# register the filter
register.filter("cut",cut)
# first parameter: then name you want to use in the html to refer to this filter;
# second parameter: the function itself
```
