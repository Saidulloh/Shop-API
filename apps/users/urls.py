from django.urls import path

from apps.users.views import *


urlpatterns = [
    path('list/', UserAPIView.as_view()),
    path('profile/<int:pk>/', UserProfileAPIView.as_view()),
    path('create/', UserCreateAPIView.as_view()),
    path('detail/<int:pk>/', UserDetailAPIView.as_view()),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view()),
    path('update/<int:pk>/', UserUpdateAPIView.as_view()),
]