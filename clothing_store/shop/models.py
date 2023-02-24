from django.db import models
from django.urls import reverse


class Category(models.Model):
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
    name = models.CharField(max_length=255, verbose_name='Название')
    main_photo = models.ImageField(upload_to="images/category/", verbose_name='Главное фото')
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
