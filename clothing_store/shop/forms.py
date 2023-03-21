from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from shop.models import User


class RegisterUserForm(UserCreationForm):
    """Форма регистрации пользователя"""

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField(label='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    """Форма авторизации пользователя"""

    password = forms.CharField(label='ПАРОЛЬ', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField(label='')

'''
# попытка сделать форму 
    email = forms.EmailField(label='Эл.Почта', widget=forms.EmailInput(attrs={
        'class': 'modal__signin-classic-field-input',
        'id': 'signin-email',
        'maxlength': '255',
        'autocomplete': 'email',
        'required': True,
    }))

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'modal__signin-classic-field-input',
            'id': 'signin-password',
            'maxlength': '255',
            'autocomplete': 'current-password',
            'required': True,
        }),
    )
'''
    class Meta:
        model = User
