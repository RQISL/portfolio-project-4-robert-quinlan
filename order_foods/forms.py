from .models import ProfileView, ContactView
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class ContactForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactView
        fields = '__all__'


class ItemForm(forms.ModelForm):
    class Meta:
        model = ProfileView
        fields = ['user', 'bio', 'image']
