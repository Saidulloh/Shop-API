from django.urls import path

from apps.category.views import *   


urlpatterns = [
    path('list/', CategoryAPIView.as_view()),
    path('detail/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('delete/<int:pk>/', CategoryDeleteAPIView.as_view()),
    path('update/<int:pk>/', CategoryUpdateAPIView.as_view()),
    path('create/', CategoryCreateAPIView.as_view()),
]