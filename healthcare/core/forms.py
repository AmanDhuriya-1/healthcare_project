from django import forms
from .models import Info
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['full_name', 'age', 'notes']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
