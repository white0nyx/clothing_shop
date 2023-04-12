from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.conf import settings

from clothing_store import settings


# from django.contrib.auth.models import AbstractUser, User, Group


# class Account(AbstractUser):
#     email = models.EmailField(
#         'email_address',
#         unique=True,
#         default='')
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     groups = models.ManyToManyField(
#         'auth.Group',
#         blank=True,
#         related_name='user_group_set',
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups'
#     )
#
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         blank=True,
#         related_name='user_permission_set',
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions'
#     )
#
#     # def get_absolute_url(self):
#     #     return reverse('account', kwargs={'account_slug': self.username})
class UserManager(BaseUserManager):

    def create_user(self, username, email, password, first_name='', last_name='', father_name='', phone='',
                    country='', region='', city='', address='', post_index=''):
        if not email:
            raise ValueError('У пользователя должен быть E-mail адрес')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            father_name=father_name,
            phone=phone,
            country=country,
            region=region,
            city=city,
            address=address,
            post_index=post_index,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, first_name='', last_name='', father_name='', phone='',
                         country='', region='', city='', address='', post_index=''):
        user = self.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            father_name=father_name,
            phone=phone,
            country=country,
            region=region,
            city=city,
            address=address,
            post_index=post_index,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='Имя пользователя', max_length=63, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=True)
    father_name = models.CharField(verbose_name='ОТЧЕСТВО', max_length=255, blank=True)
    phone = models.CharField(verbose_name='ТЕЛЕФОН', max_length=20, blank=True)
    country = models.CharField(verbose_name='СТРАНА', max_length=255, blank=True)
    region = models.CharField(verbose_name='КРАЙ/ОБЛАСТЬ/РЕГИОН', max_length=255, blank=True)
    city = models.CharField(verbose_name='ГОРОД', max_length=255, blank=True)
    address = models.CharField(verbose_name='АДРЕС', max_length=255, blank=True)
    post_index = models.CharField(verbose_name='ИНДЕКС', max_length=255, blank=True)
    email = models.EmailField(verbose_name='ЭЛ. ПОЧТА', max_length=255, unique=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    is_staff = models.BooleanField(verbose_name='Сотрудник', default=False)
    is_superuser = models.BooleanField(verbose_name='Администратор', default=False)
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_stuff(self):
        return self.is_staff

    def save(self, *args, **kwargs):
        super().save()

    def get_absolute_url(self):
        return reverse('account', kwargs={'username': self.username})


class Category(models.Model):
    """Модель категории"""

    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Item(models.Model):
    """Модель товара"""

    name = models.CharField(max_length=255, verbose_name='Название')
    main_photo = models.ImageField(upload_to="images/photo/", verbose_name='Главное фото')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    slug = models.SlugField(db_index=True, unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    price = models.BigIntegerField(verbose_name='Цена в рублях')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания товара')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления товара')
    is_in_stock = models.BooleanField(default=False, verbose_name='Есть в наличии')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']


class AdditionalImageItem(models.Model):
    """Модель изображения товара"""

    path = models.ImageField(upload_to="images/photo/", verbose_name='Фото')
    item = models.ForeignKey(Item, default=None, on_delete=models.CASCADE, verbose_name='Товар', related_name='add_images')

    class Meta:
        verbose_name = 'Дополнительное изображение товара'
        verbose_name_plural = 'Дополнительные изображения товара'

    # def get_absolute_url(self):
    #     return self.path

    def __str__(self):
        return self.item.name + ' ADD_Image'


class Cart(object):
    """Модель корзины"""

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item, size, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0,
                                  'price': str(item.price)}
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
            self.cart[item_id]['size'] = size
        else:
            self.cart[item_id]['quantity'] += quantity
            self.cart[item_id]['size'] = size

        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, item):
        """
        Удаление товара из корзины.
        """
        product_id = str(item.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        items_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        items = Item.objects.filter(id__in=items_ids)
        for product in items:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(int((item['price'])) * int(item['quantity']) for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
