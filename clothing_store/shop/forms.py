from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from shop.models import User


class RegisterUserForm(UserCreationForm):
    """Форма регистрации пользователя"""

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


class MainUserDataForm(forms.Form):

    first_name = forms.CharField(label='ИМЯ', widget=forms.TextInput(attrs={
        'name': 'first_name',
        'class': 'account__details-personal-data-item-input',
        'maxlength': "30"
    }))

    last_name = forms.CharField(label='ФАМИЛИЯ', widget=forms.TextInput(attrs={
        'name': 'last_name',
        'class': 'account__details-personal-data-item-input',
        'maxlength': "30"
    }))

    father_name = forms.CharField(label='ОТЧЕСТВО', widget=forms.TextInput(attrs={
        'name': 'middle_name',
        'class': 'account__details-personal-data-item-input',
        'maxlength': "30"
    }))

    phone = forms.CharField(label='ТЕЛЕФОН', widget=forms.TextInput(attrs={
        'name': 'phone',
        'class': 'account__details-personal-data-item-input'
    }))

    email = forms.EmailField(label='ЭЛ.ПОЧТА', widget=forms.TextInput(attrs={
        'name': 'email',
        'class': 'account__details-personal-data-item-input unchangable'
    }))
    country = forms.CharField(label='СТАРНА', widget=forms.TextInput(attrs={
        'name': 'country',
        'class': 'account__details-delivery-item-input',
        'maxlength': "30"
    }))

    city = forms.CharField(label='ГОРОД', widget=forms.TextInput(attrs={
        'name': 'city',
        'class': 'account__details-delivery-item-input',
        'maxlength': "30"
    }))

    address = forms.CharField(label='АДРЕС', widget=forms.TextInput(attrs={
        'name': 'address',
        'class': 'account__details-delivery-item-input',
        'maxlength': "30"
    }))

    post_index = forms.CharField(label='ПОЧТОВЫЙ ИНДЕКС', widget=forms.TextInput(attrs={
        'name': 'post_index',
        'class': 'account__details-delivery-item-input',
        'maxlength': "30"
    }))

    region = forms.EmailField(label='РЕГИОН', widget=forms.TextInput(attrs={
        'name': 'region',
        'class': 'account__details-delivery-item-input',
        'maxlength': "30"
    }))

    password = forms.CharField(label='Новый Пароль', widget=forms.PasswordInput(attrs={
        'class': 'account__details-personal-data-item-input1',
        'name': 'password',
        'maxlength': "255"
    }))

    password_confirmation = forms.CharField(label='Повторите Пароль', widget=forms.PasswordInput(attrs={
        'class': 'account__details-personal-data-item-input1',
        'name': 'password_confirmation',
        'maxlength': "255"
    }))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'father_name', 'phone', 'email', 'country', 'city',
                  'address', 'post_index', 'region', 'password', 'password_confirmation')


