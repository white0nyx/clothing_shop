# Generated by Django 4.1.5 on 2023-02-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='about_yourself',
            field=models.TextField(default=None, verbose_name='О себе'),
            preserve_default=False,
        ),
    ]
