from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from user.models import Profile


class Userform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'birthday']