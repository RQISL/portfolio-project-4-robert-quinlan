from .models import Profile, ContactView
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""
This is for contact form,
use storage in Database.

"""


class ContactForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactView
        fields = '__all__'


"""
This is for CRUD in profile form,
use storage in Database. It is included
Add and Edit active in the from.

The Add is as create instead

"""


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['username']


class UserUpdateForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'name']


class BioUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['bio']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'username', 'name', 'bio']
