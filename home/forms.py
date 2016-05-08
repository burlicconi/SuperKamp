# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password.widget = forms.PasswordInput(attrs={'placeholder': 'Lozinka'})
    username = forms.CharField(widget=forms.TextInput())
    username.widget = forms.TextInput(attrs={'placeholder': 'Korisničko ime'})
    class Meta:
        model = User
        fields = ['username','password',]