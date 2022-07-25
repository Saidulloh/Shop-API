from django.db import models
from django.contrib.auth import get_user_model

from apps.category.models import Category

User = get_user_model()


class Product(models.Model):
    title = models.CharField(
        'Название', 
        max_length=255
        )
    image = models.ImageField(
        'Картинка', 
        upload_to='products/'
        )
    category = models.ForeignKey(
        Category,
        related_name='prod_cat',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    time_create = models.DateTimeField(
        'Время создания', 
        auto_now_add=True
        )
    time_update = models.DateTimeField(
        'Время изменения', 
        auto_now=True
        )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='prod_user'
        )
    price = models.DecimalField(
        verbose_name='Цена товара', 
        max_digits=1000000, 
        decimal_places=1
        )

    url = models.SlugField(
        'Ссылка', 
        max_length=255
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
