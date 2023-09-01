from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя (username)', min_length=5, max_length=150)
    password1 = forms.CharField(label='Пароль (password)', widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(label='Подтвердите пароль (Confirm password)', widget=forms.PasswordInput, min_length=8)
    email = forms.EmailField(label='Эл. почта (email)')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Такой пользователь уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email зарегистрирован")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        password_error = password1 and password2 and password1 != password2
        number_error = password2.isdigit()
        if number_error and password_error:
            raise ValidationError("Пароли не совпадают; Пароль не должен быть полностью цифровым")
        elif password_error:
            raise ValidationError('Пароли не совпадают')
        elif number_error:
            raise ValidationError("Пароль не должен быть полностью цифровым")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


