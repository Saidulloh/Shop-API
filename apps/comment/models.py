from django.db import models
from django.contrib.auth import get_user_model

from apps.product.models import Product

User = get_user_model()


class Comment(models.Model):
    CHICES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    comment = models.CharField(
        max_length=255
        )
    product = models.ForeignKey(
        Product,
        related_name='comm_prod',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User, 
        related_name='Usercomment',
        on_delete=models.PROTECT
        )
    star = models.CharField(
        choices=CHICES, 
        max_length=10
        )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.comment.id} -- {self.owner.username}'

    class Meta:
        ordering = ['-create_at']
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'


class Children(models.Model):
    title = models.CharField(
        max_length=255
    )
    owner = models.ForeignKey(
        User, 
        related_name='children_rn',
        on_delete=models.CASCADE   
    )
    parent = models.ForeignKey(
        Comment,
        related_name='parent_rn',
        on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.id} -- {self.title} -- {self.owner.username}'

    class Meta:
        ordering = ['-create_at']
        verbose_name = 'Дочерний коммент'
        verbose_name_plural = 'дочерние комменты'