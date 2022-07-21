# Generated by Django 4.0.4 on 2022-07-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Ссылка'),
        ),
    ]
