from django.urls import path

from apps.comment.views import *


urlpatterns = [
    path('list/', CommentAPIView.as_view()),
    path('detail/<int:pk>/', CommentDetailAPIView.as_view()),
    path('delete/<int:pk>/', CommentDeleteAPIView.as_view()),
    path('update/<int:pk>/', CommentUpdateAPIView.as_view()),
    path('create/', CommentCreateAPIView.as_view()),
]