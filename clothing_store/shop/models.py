from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.urls import reverse


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
    item = models.ForeignKey(Item, default=None, on_delete=models.CASCADE, verbose_name='Товар', )

    class Meta:
        verbose_name = 'Дополнительное изображение товара'
        verbose_name_plural = 'Дополнительные изображения товара'

    def __str__(self):
        return self.item.name + ' Image'
