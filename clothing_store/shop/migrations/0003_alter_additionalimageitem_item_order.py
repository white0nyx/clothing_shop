# Generated by Django 4.1.7 on 2023-05-25 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_additionalimageitem_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalimageitem',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='add_images', to='shop.item', verbose_name='Товар'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(verbose_name='Имя')),
                ('last_name', models.TextField(verbose_name='Фамилия')),
                ('father_name', models.TextField(verbose_name='Отчество')),
                ('phone', models.TextField(verbose_name='Телефон')),
                ('email', models.TextField(verbose_name='ЭЛ. ПОЧТА')),
                ('country', models.TextField(verbose_name='Страна')),
                ('city', models.TextField(verbose_name='Город')),
                ('region', models.TextField(verbose_name='Край / Область / Регион')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('mail_index', models.TextField(verbose_name='Почтовый индекс')),
                ('note', models.TextField(verbose_name='Примечание')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания товара')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления товара')),
                ('status', models.TextField(default='Не оплачен', verbose_name='Статус')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Аккаунт заказчика')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
