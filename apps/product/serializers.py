from rest_framework import serializers

from .models import *
from apps.comment.serializers import CommentSerializer
from apps.comment.models import Comment

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = '__all__'


class ProductFullSerializer(serializers.ModelSerializer):
    comm_prod = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        read_only_fields = ('id', 'user')
        fields = [
            'id',
            'user',
            'title',
            'image',
            'category',
            'time_create',
            'time_update',
            'price',
            'url',
            'comm_prod',
        ]