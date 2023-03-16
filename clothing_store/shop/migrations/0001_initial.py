# Generated by Django 4.1.5 on 2023-03-16 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=63, unique=True, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('father_name', models.CharField(blank=True, max_length=255, verbose_name='ОТЧЕСТВО')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='ТЕЛЕФОН')),
                ('country', models.CharField(blank=True, max_length=255, verbose_name='СТРАНА')),
                ('region', models.CharField(blank=True, max_length=255, verbose_name='КРАЙ/ОБЛАСТЬ/РЕГИОН')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='ГОРОД')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='АДРЕС')),
                ('post_index', models.CharField(blank=True, max_length=255, verbose_name='ИНДЕКС')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='ЭЛ. ПОЧТА')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Сотрудник')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Администратор')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('main_photo', models.ImageField(upload_to='images/category/', verbose_name='Главное фото')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.BigIntegerField(verbose_name='Цена в рублях')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания товара')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления товара')),
                ('is_in_stock', models.BooleanField(default=False, verbose_name='Есть в наличии')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AdditionalImageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to='images/category/', verbose_name='Фото')),
                ('item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='shop.item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Дополнительное изображение товара',
                'verbose_name_plural': 'Дополнительные изображения товара',
            },
        ),
    ]
