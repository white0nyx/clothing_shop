# Generated by Django 4.1.7 on 2023-05-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_linkinordersanditems'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0, verbose_name='Сумма заказа'),
        ),
    ]
