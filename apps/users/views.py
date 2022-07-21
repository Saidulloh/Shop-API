from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from apps.users.permissions import IsOwnerOrReadOnly
from apps.users.serializers import UserSerializer, UserFullSerializer
from apps.users.models import User
from apps.product.models import Product


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UserProfileAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserFullSerializer
