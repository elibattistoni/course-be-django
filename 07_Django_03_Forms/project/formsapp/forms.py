from wsgiref.validate import validator
from django import forms
from django.core import validators


class FormName1(forms.Form):
    """
    Example with hidden field to catch a bot

    if a bot fills in the form, it will fill in also this field (that is hidden from humans users)
    to create your custom validator:
    django is going to automatically look for methods inside this Form class that start with
    "clean_" and then see if the following part of the name of the function (i.e. "bot_catcher")
    matches any of the fields in the form
    """

    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_bot_catcher(self):
        bot_catcher = self.cleaned_data["bot_catcher"]
        if bot_catcher:
            raise forms.ValidationError("GOTCHA BOT!")
        return bot_catcher


class FormName2(forms.Form):
    """
    Example with Django built-in validators (more common validations)
    """

    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
    )


def check_for_z(value):
    """
    The input parameter value tell Django that it should look in value
    """
    if value[0].lower() != "z":
        raise forms.ValidationError("NEEDS O START WITH Z")


class FormName3(forms.Form):
    """
    Example with custom validators
    """

    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
    )



class FormName4(forms.Form):
    """
    Example with cleaning the form all at once

    the method clean without anything else will tell Django that it is not specific
    to any variable and it will check the whole form
    """

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        # this will return all the cleaned data all at once
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]
        if email != verify_email:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")