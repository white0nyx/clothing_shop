import codecs

import datetime

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.contrib.sessions.backends.db import SessionStore
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView
from pyqiwi.types import Transaction

import qiwi
from qiwi import Payment
from shop.forms import RegisterUserForm, LoginUserForm, MainUserDataForm
from shop.models import *


ITEMS_IN_LINE = 3 # items

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
        context['cart'] = Cart(self.request)
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

        if not self.request.user.is_authenticated and self.request.session.get('temporary_currency'):
            currency = self.request.session['temporary_currency']

        converted_price = self.object.convert_price(currency)

        context['converted_price'] = converted_price
        context['currency'] = currency
        context['cart'] = Cart(self.request)
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

    if request.user.pk is None:
        return redirect('registration')

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



    cart = [item for item in Cart(request)]

    for item in cart:
        item['product'] = str(item['product']).split('_')[-1]

    total_price = sum([item['total_price'] for item in cart])

    if request.GET:
        order_data = OrderData(request, recreate=True)
        context = {'title': 'Оформление заказа', 'cart': cart, 'order_data': order_data, 'total_price' : total_price}
        return render(request, 'shop/place_on_order_2.html', context)

    else:
        order_data = OrderData(request, recreate=True)
        context = {'title': 'Оформление заказа', 'cart': cart, 'total_price' : total_price}
        return render(request, 'shop/place_on_order.html', context)


def payment_page(request: WSGIRequest):
    """Оплата"""

    cart = Cart(request)
    order_data = OrderData(request, recreate=False).get_dict_of_data()
    first_name = order_data['first_name'][0]
    last_name = order_data['last_name'][0]
    middle_name = order_data['middle_name'][0]
    phone = order_data['telephone'][0]
    email = order_data['email'][0]
    countries = order_data['countrys'][0]
    city = order_data['city'][0]
    region = order_data['region'][0]
    address = order_data['address'][0]
    zip_code = order_data['zip_code'][0]
    note = order_data['note'][0]

    payment = Payment(cart.get_total_price())
    payment.create()

    order = Order(user_id=request.user,
                  first_name=first_name,
                  last_name=last_name,
                  father_name=middle_name,
                  phone=phone,
                  email=email,
                  country=countries,
                  city=city,
                  region=region,
                  address=address,
                  mail_index=zip_code,
                  note=note,
                  total_price=cart.get_total_price(),
                  payment_code=str(payment.id),
                  )

    order.save()

    for item in cart:
        product = item.get('product')
        quantity = item.get('quantity')
        size = item.get('size')
        LinkinOrdersAndItems(order=order, item=product, quantity=quantity, size=size).save()


    cart.clear()
    return redirect(payment.invoice)


def my_orders(request: WSGIRequest, context=None):

    if context == 'no_payment':
        alert_message = 'Платёж не обнаружен'
    elif context == 'success':
        alert_message = 'Платёж обнаружен. Статус заказа обновлен.'
    else:
        alert_message = ''

    cart = Cart(request)
    user_id = request.user.pk
    user_orders = Order.objects.filter(user_id=user_id)
    context = {
        'title': "Мои заказы",
        'cart': cart,
        'orders': user_orders,
        'alert_message': alert_message,
    }



    return render(request, 'shop/my_orders.html', context)


def check_payment(request: WSGIRequest, order_slug):

    payment_code, total_price = order_slug.split('__')
    start_date = datetime.datetime.now() - datetime.timedelta(days=2)
    transactions : [Transaction] = qiwi.wallet.history(start_date=start_date).get("transactions")
    for t in transactions:
        t: Transaction = t
        if t.comment:
            if str(payment_code) in str(t.comment):
                if float(t.total.amount) >= float(total_price):
                    order = Order.objects.get(payment_code=payment_code)
                    order.status = "Оплачен"
                    order.save()
                    return redirect('my_orders', context='success')


                else:
                    return redirect('my_orders', context='not_enough_money')

    else:
        return redirect('my_orders', context='no_payment')


def change_currency(request):
    if request.method == 'POST':
        currency = request.POST.get('currency')
        request.session['temporary_currency'] = currency
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            user.currency = currency
            user.save()
    return redirect(request.META.get('HTTP_REFERER'))






def chart_page(request):
    """Функция представления страницы с аналитикой"""

    return render(request, 'shop/chart_page.html')


import csv
from django.http import HttpResponse


def export_products_to_csv(request):
    # Создаем HTTP-ответ с указанием типа контента
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    # Создаем объект writer для записи в CSV
    writer = csv.writer(response, delimiter=';')

    # Записываем заголовки столбцов
    writer.writerow(['Product ID', 'Name', 'Category', 'Slug', 'Description', 'Price', 'Creation Date', 'Update Date', 'In Stock'])

    # Получаем все товары
    products = Item.objects.all()

    # Записываем данные по каждому товару
    for product in products:
        writer.writerow([
            product.id,
            product.name,
            product.category.name,
            product.slug,
            product.description,
            product.price,
            product.date_create,
            product.date_update,
            product.is_in_stock
        ])

    return response


def export_users_to_csv(request):
    # Создаем HTTP-ответ с указанием типа контента
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    # Используем контекстный менеджер для записи данных в CSV
    writer = csv.writer(response, delimiter=';', quoting=csv.QUOTE_MINIMAL)

    # Записываем заголовки столбцов
    writer.writerow(['User ID', 'Username', 'First Name', 'Last Name', 'Email', 'Date Joined', 'Is Staff', 'Is Active'])

    # Получаем всех пользователей
    users = User.objects.all()

    # Записываем данные по каждому пользователю
    for user in users:
        writer.writerow([
            user.id,
            user.username,
            user.first_name,
            user.last_name,
            user.email,
            user.date_joined,
            user.is_staff,
            user.is_active
        ])

    return response