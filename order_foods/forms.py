from .models import ProfileView
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass


class ItemForm(forms.ModelForm):
    class Meta:
        model = ProfileView
        fields = ['user', 'bio', 'image']

