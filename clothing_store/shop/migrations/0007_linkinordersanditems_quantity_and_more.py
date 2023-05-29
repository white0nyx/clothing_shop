# Generated by Django 4.1.7 on 2023-05-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkinordersanditems',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linkinordersanditems',
            name='size',
            field=models.TextField(default=1, verbose_name='Размер'),
            preserve_default=False,
        ),
    ]
