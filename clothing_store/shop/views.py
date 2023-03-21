import math

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.handlers.wsgi import WSGIRequest
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


def split_list_into_chunks(items) -> [list]:
    """Функция для получения товаров разбитых на линии"""

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


class CategoryPage(ListView, LoginView):
    """Класс представления главной страницы"""

    model = Item
    template_name = 'shop/category_page.html'
    context_object_name = 'items'
    form_class = LoginUserForm

    def get_queryset(self):
        items = Item.objects.filter(category__slug=self.kwargs['category_slug'], is_in_stock=True)
        return split_list_into_chunks((list(items)))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['category_slug']).name + ' - WearFit'
        context['category_selected'] = Category.objects.filter(slug=self.kwargs['category_slug'])[0].id
        context['form'] = LoginUserForm
        return context


    def get_success_url(self):
        return reverse_lazy('home')


class ItemPage(DetailView):
    model = Item
    template_name = 'shop/item_page.html'
    slug_url_kwarg = 'item_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['item']
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

    def form_valid(self, form):
        user = form.save()
        print(user.email, user.password)

        # user = authenticate(email=user.email, password=user.password)
        login(self.request, user)
        return redirect('home')

'''
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
'''

class AccountPage(DetailView):
    model = User
    template_name = 'shop/account_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['user']
        return context

    def get(self, request: WSGIRequest, *args, **kwargs):
        username = kwargs.get('username')
        return render(request, 'shop/account_page.html', {'username': username})
