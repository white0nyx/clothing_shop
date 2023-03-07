# Generated by Django 4.1.5 on 2023-03-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name='АДРЕС'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='ГОРОД'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=255, verbose_name='СТРАНА'),
        ),
        migrations.AddField(
            model_name='user',
            name='father_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='ОТЧЕСТВО'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='ТЕЛЕФОН'),
        ),
        migrations.AddField(
            model_name='user',
            name='post_index',
            field=models.CharField(blank=True, max_length=255, verbose_name='ИНДЕКС'),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, max_length=255, verbose_name='КРАЙ/ОБЛАСТЬ/РЕГИОН'),
        ),
    ]