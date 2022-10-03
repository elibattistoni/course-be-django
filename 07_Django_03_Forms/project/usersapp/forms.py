from django import forms
from usersapp.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"