from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from shop.models import User


class RegisterUserForm(UserCreationForm):
    """Форма регистрации пользователя"""

    # username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # username = forms.CharField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # captcha = CaptchaField(label='')

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'modal__signup-classic-field-input',
        'id': 'signup-username',
        'maxlength': "255",
        'autocomplete': 'username',
        'required': True,
    }))

    email = forms.CharField(label='Эл.почта', widget=forms.EmailInput(attrs={
        'class': 'modal__signup-classic-field-input',
        'id': 'signup-email',
        'maxlength': "255",
        'autocomplete': 'email',
        'required': True,
    }))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'modal__signup-classic-field-input',
        'id': 'signup-password',
        'maxlength': "255",
        'autocomplete': 'new-password',
        'required': True,
    }))

    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'modal__signup-classic-field-input',
        'id': 'signup-confirmation',
        'maxlength': "255",
        'autocomplete': 'new-password',
        'required': True,
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    """Форма авторизации пользователя"""


    username = forms.EmailField(label='ЭЛ.ПОЧТА', widget=forms.EmailInput(attrs={
            'class': 'modal__signin-classic-field-input',
            'id': 'signin-email',
            'maxlength': '255',
            'autocomplete': 'email',
            'required': True,
        }))

    password = forms.CharField(label='ПАРОЛЬ', widget=forms.PasswordInput(attrs={
        'class': 'modal__signin-classic-field-input',
        'id': 'signin-password',
        'maxlength': '255',
        'autocomplete': 'current-password',
        'required': True,
    }))


    class Meta:
        model = User
