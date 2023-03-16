# Generated by Django 4.1.5 on 2023-03-16 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalimageitem',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.item', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='additionalimageitem',
            name='path',
            field=models.ImageField(upload_to='images/photo/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='item',
            name='main_photo',
            field=models.ImageField(upload_to='images/photo/', verbose_name='Главное фото'),
        ),
    ]
