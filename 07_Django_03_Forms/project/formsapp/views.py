from django.shortcuts import render
from formsapp import forms


def homepage(request):
    rendering = render(request, "formsapp/homepage.html")
    return rendering


def basic_form(request):
    """
    FormName1 has an example of validation with hidden inputs (check for bots)
    FormName2 has an example of validation with django built-in validators
    FormName3 has an example of validation with custom validator
    FormName4 has an example of cleaning the whole form
    """

    # form = forms.FormName1() # with example of validation/check for bots
    # form = forms.FormName2() # with example of django built-in validation
    # form = forms.FormName3() # with example of custom validation
    form = forms.FormName4() # with example of custom validation

    if request.method == "POST":
        # form = forms.FormName1(request.POST)
        # form = forms.FormName2(request.POST)
        # form = forms.FormName3(request.POST)
        form = forms.FormName4(request.POST)
        
        if form.is_valid():
            print("VALIDATION SUCCESS")
            print(f"name: {form.cleaned_data['name']}")
            print(f"email: {form.cleaned_data['email']}")
            print(f"text: {form.cleaned_data['text']}")

    rendering = render(request, "formsapp/basic_form.html", {"form": form})

    return rendering
