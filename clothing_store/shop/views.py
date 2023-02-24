from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from shop.forms import RegisterUserForm
from shop.models import *


def home_page(request):
    """Функция представления главной страницы"""

    return render(request, 'shop/home.html', context={'title': 'Главная страница'})


class CategoryPage(ListView):
    model = Item
    template_name = 'shop/category_page.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.filter(category__slug=self.kwargs['category_slug'], is_in_stock=True)

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
        return context
