import math

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, _get_queryset
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from shop.forms import RegisterUserForm, LoginUserForm
from shop.models import *

ITEMS_IN_LINE = 3


def home_page(request):
    """Функция представления главной страницы"""

    return render(request, 'shop/home.html', context={'title': 'Главная страница'})


def split_list_into_chunks(items):
    chunk_size = ITEMS_IN_LINE
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


class HomePage(ListView):
    """Класс представления главной страницы"""

    model = Item
    template_name = 'shop/category_page.html'
    context_object_name = 'items'

    def get_queryset(self):
        items = Item.objects.all()
        return split_list_into_chunks((list(items)))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WearFit'
        return context


def logout_user(request):
    """Деавторизация пользователя"""

    logout(request)
    return redirect('home')


class CategoryPage(ListView):
    model = Item
    template_name = 'shop/category_page.html'
    context_object_name = 'items'

    def get_queryset(self):
        items = Item.objects.filter(category__slug=self.kwargs['category_slug'], is_in_stock=True)
        return split_list_into_chunks((list(items)))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['category_slug']).name + ' - WearFit'
        context['category_selected'] = Category.objects.filter(slug=self.kwargs['category_slug'])[0].id
        return context


class RegistrationPage(CreateView):
    """Класс представления страницы регистрации нового пользователя"""

    form_class = RegisterUserForm
    template_name = 'shop/registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class LoginPage(LoginView):
    """Класс представления страницы авторизации"""

    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'

        return context

    def get_success_url(self):
        return reverse_lazy('home')
