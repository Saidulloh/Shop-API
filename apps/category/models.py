from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.CharField(
        'Название', 
        max_length=255,
        unique=True
        )
    owner = models.ForeignKey(
        User,
        related_name='cat_owner',
        on_delete=models.CASCADE
    )
    url = models.SlugField(
        'Ссылка', 
        max_length=255,
        unique=True
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
