from django.urls import path

from .views import *

urlpatterns = [
    path('list/', ProductAPIView.as_view()),
    path('detail/<int:pk>/', ProductDetailAPIView.as_view()),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view()),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('create/', ProductCreateAPiView.as_view()),
]