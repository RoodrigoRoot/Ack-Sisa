from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
# Create your views here.

class RegisterUserForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(
        label="Nombre(s)",
        required=True
    )
    last_name=forms.CharField(
        label="Apellidos",
        required=True
    )
    username = forms.SlugField(
        label='Username', 
        help_text='Sin espacios, sin acentos, sin ñ / puedes usar - y _', required=True)

    password = forms.CharField(
        widget=forms.PasswordInput(), 
        label='Contraseña')

    password2 = forms.CharField(
        widget=forms.PasswordInput(), 
        label='Repetir contraseña')
    # captcha = ReCaptchaField()


    def clean_username(self):
        username = str.lower(self.cleaned_data['username'])
        if len(username) <= 3:
            raise ValidationError("El nombre necesita tener mas de 3 caracteres")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este Usuario ya esta en uso")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este Email ya esta en uso")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        return password

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError('Contraseñas no coinciden')
        return password2


class RegisterProfileForm(ModelForm):
    model=Profile
    fields=("area","position")

    def clean_area(self):
        area = self.clean_data['area']
        
        return area
    
    def clean_position(self):
        position = self.cleaned_data['position']
        return position