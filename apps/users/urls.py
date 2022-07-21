from django.urls import path

from apps.users.views import *


urlpatterns = [
    path('list/', UserAPIView.as_view()),
    path('profile/<int:pk>/', UserProfileAPIView.as_view()),
]