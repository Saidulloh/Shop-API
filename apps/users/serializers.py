from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.product.serializers import ProductSerializer
from apps.favorite.serializers import FavoriteSerializer
from apps.comment.serializers import CommentSerializer
from apps.category.serializers import CategorySerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password', 
            ]

        
class UserFullSerializer(serializers.ModelSerializer):
    prod_user = ProductSerializer(many=True, read_only=True)
    favorite_user = FavoriteSerializer(many=True, read_only=True)
    Usercomment = CommentSerializer(many=True, read_only=True)
    cat_owner = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password', 
            'cat_owner',
            'prod_user', 
            'favorite_user',
            'Usercomment',
            ]