from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'avatar']