from django.db import models
from django.contrib.auth import get_user_model

from apps.product.models import Product


User = get_user_model()


class Favorite(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='favorite_prod',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name='favorite_user',
        on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.product.id} -- {self.user.username}'

    class Meta:
        ordering=['-create_at']