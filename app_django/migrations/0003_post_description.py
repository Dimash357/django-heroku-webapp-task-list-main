# Generated by Django 4.1.7 on 2023-02-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]
