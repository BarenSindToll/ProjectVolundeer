from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=15,label='Username',
                               widget=forms.TextInput(attrs={'required':'required', 'placeholder':'Username'}))
    password = forms.CharField(max_length=15, label='Password',
                                widget=forms.PasswordInput(attrs={'required':'required', 'placeholder':'Password'}))
