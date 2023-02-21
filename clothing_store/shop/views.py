from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shop.forms import RegisterUserForm


def home_page(request):
    """Функция представления главной страницы"""

    return render(request, 'shop/home.html', context={'title': 'Главная страница'})


class RegistrationPage(CreateView):
    """Класс представления страницы регистрации нового пользователя"""

    form_class = RegisterUserForm
    template_name = 'shop/registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
