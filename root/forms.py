from django.db.models.base import Model
from django.forms import widgets
from django.forms.widgets import HiddenInput, PasswordInput
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class Signup_Form(UserCreationForm):
    username = forms.CharField(label="الإسم",widget=forms.TextInput())
    email = forms.EmailField(label="الإيميل",widget=forms.TextInput())
    password1 = forms.CharField(label="كلمة المرور",widget=PasswordInput(),min_length=8)
    password2 = forms.CharField(label="تأكيد كلمة المرور",widget=PasswordInput(),min_length=8)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")


class Login_Form(forms.ModelForm):
    username = forms.CharField(label="الإسم",widget=forms.TextInput())
    password = forms.CharField(label="كلمة المرور",widget=PasswordInput())
    class Meta:
        model = User
        fields = ("username","password")

class Update_User_Form(forms.ModelForm):
    username = forms.CharField(label="الإسم")
    email = forms.EmailField(label="الإيميل")
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name")




