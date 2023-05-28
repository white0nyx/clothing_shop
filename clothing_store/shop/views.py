from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.contrib.sessions.backends.db import SessionStore
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView

from qiwi import Payment
from shop.forms import RegisterUserForm, LoginUserForm, MainUserDataForm
from shop.models import *

ITEMS_IN_LINE = 3


def home_page(request):
    """Функция представления главной страницы"""

    return render(request, 'shop/home.html', context={'title': 'Главная страница'})


def split_list_into_chunks(items) -> [list]:
    """Функция для получения товаров разбитых на линии"""

    chunk_size = ITEMS_IN_LINE
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


class HomePage(LoginView, ListView):
    """Класс представления главной страницы"""

    model = Item
    template_name = 'shop/home.html'
    context_object_name = 'items'
    form_class = LoginUserForm

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        context = super().get_context_data(**kwargs)
        context['title'] = 'WearFit'
        context['form'] = LoginUserForm
        context['cart'] = cart
        return render(request, 'shop/home.html', context)

    def get_queryset(self):
        items = Item.objects.all()
        return split_list_into_chunks((list(items)))

    object_list = split_list_into_chunks((list(Item.objects.all())))


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
    object_list = split_list_into_chunks(list(Item.objects.all()))

    def get_queryset(self):
        items = Item.objects.filter(category__slug=self.kwargs['category_slug'], is_in_stock=True)
        return split_list_into_chunks(list(items))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']

        if self.request.user.is_authenticated:
            currency = self.request.user.currency
        else:
            currency = 'RUB'

        if not self.request.user.is_authenticated and self.request.session.get('temporary_currency'):
            currency = self.request.session['temporary_currency']

        # Конвертирование цен для каждого товара в выбранной категории
        items = context['items']
        for chunk in items:
            for item in chunk:
                item.converted_price = item.convert_price(currency)

        context['title'] = Category.objects.get(slug=category_slug).name + ' - WearFit'
        context['category_selected'] = Category.objects.filter(slug=category_slug)[0].id
        context['form'] = LoginUserForm
        context['currency'] = currency
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class ItemPage(DetailView):
    model = Item
    template_name = 'shop/item_page.html'
    slug_url_kwarg = 'item_slug'
    form_class = LoginUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['item']
        context['items'] = Item.objects.all().order_by('?')

        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user.username)
            currency = getattr(user, 'currency', 'RUB')
        else:
            currency = 'RUB'

        converted_price = self.object.convert_price(currency)

        context['converted_price'] = converted_price
        context['currency'] = currency
        return context


class RegistrationPage(CreateView, ListView):
    """Класс представления страницы регистрации нового пользователя"""

    model = Item
    context_object_name = 'items'
    form_class = RegisterUserForm
    template_name = 'shop/registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WearFit'
        return context

    def get_queryset(self):
        items = Item.objects.all()
        return split_list_into_chunks((list(items)))

    def form_valid(self, form):
        user = form.save()

        # user = authenticate(email=user.email, password=user.password)
        login(self.request, user)
        return redirect('home')

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)


class AccountPage(FormView):
    model = User
    template_name = 'shop/account_page.html'
    form_class = MainUserDataForm

    def get(self, request: WSGIRequest, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        user_data = {'first_name': user.first_name,
                     'last_name': user.last_name,
                     'father_name': user.father_name,
                     'phone': user.phone,
                     'country': user.country,
                     'city': user.city,
                     'address': user.address,
                     'post_index': user.post_index,
                     'region': user.region,
                     'email': user.email
                     }
        context = {
            'title': "Аккаунт",
            'form': MainUserDataForm(initial=user_data),
            'username': kwargs.get('username')
        }
        return render(request, 'shop/account_page.html', context)

    def post(self, request: WSGIRequest, *args, **kwargs):
        new_user_data = request.POST
        user = User.objects.get(username=request.user.username)
        user.first_name = new_user_data['first_name']
        user.last_name = new_user_data['last_name']
        user.father_name = new_user_data['father_name']
        user.phone = new_user_data['phone']
        user.country = new_user_data['country']
        user.city = new_user_data['city']
        user.address = new_user_data['address']
        user.post_index = new_user_data['post_index']
        user.region = new_user_data['region']
        user.email = new_user_data['email']

        password = new_user_data['password']
        password_confirmation = new_user_data['password_confirmation']
        if password and password_confirmation:
            if password == password_confirmation:
                user.password = make_password(password)  # Обновляем пароль
            else:
                # Если новые пароли не совпадают, можно вывести ошибку
                # или предпринять другие действия в зависимости от вашей логики
                pass

        user.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('account')


def cart(request):
    """Функция представления страницы корзины"""

    return render(request, 'shop/cart_test_page_2.html', context={'title': 'Корзина'})


def cart_add(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    size = request.POST['size']
    quantity = request.POST['quantity']

    cart = Cart(request)

    if size in ['S', 'M', 'L', 'XL', '2XL'] and 1 <= int(quantity) <= 20:
        cart.add(item=item, quantity=quantity, size=size, update_quantity=False)
    return redirect('home')


def cart_remove(request, item_code):
    cart = Cart(request)
    cart.remove(item_code)
    return redirect('home')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart_test_page.html', {'cart': cart})


def place_on_order_page(request: WSGIRequest):
    """Функция представления 1 страницы оформления заказа"""
    cart = Cart(request)
    if request.GET:
        order_data = OrderData(request)
        print(order_data)
        context = {'title': 'Оформление заказа', 'cart': cart, 'order_data': order_data}
        return render(request, 'shop/place_on_order_2.html', context)

    else:
        order_data = OrderData(request)
        print(order_data)
        context = {'title': 'Оформление заказа', 'cart': cart}
        cart.get_total_price()
        return render(request, 'shop/place_on_order.html', context)


def payment_page(request: WSGIRequest):
    """Оплата"""

    cart = Cart(request)
    order_data = OrderData(request).get_dict_of_data()
    first_name = order_data['first_name'][0]
    last_name = order_data['last_name'][0]
    middle_name = order_data['middle_name'][0]
    countries = order_data['countrys'][0]
    city = order_data['city'][0]
    region = order_data['region'][0]
    address = order_data['address'][0]
    zip_code = order_data['zip_code'][0]
    note = order_data['note'][0]

    print(request.user.pk)
    Order(len(Order.objects.all()), request.user.pk, first_name, last_name, middle_name, '+78888888888', 'TEST@mail.ru',
          countries, city, region, address, zip_code, note).save()
    # Order(request.user.pk, region, address, zip_code, note).save()
    payment = Payment(cart.get_total_price())
    payment.create()
    return redirect(payment.invoice)


# def change_currency(request):
#     if request.method == 'POST':
#         currency = request.POST.get('currency')
#         request.session['currency'] = currency
#     return redirect(request.META.get('HTTP_REFERER'))

def change_currency(request):
    if request.method == 'POST':
        currency = request.POST.get('currency')
        request.session['temporary_currency'] = currency
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            user.currency = currency
            user.save()
    return redirect(request.META.get('HTTP_REFERER'))
