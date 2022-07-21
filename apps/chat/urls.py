from django.urls import path

from . import views


urlpatterns = [
    # URL form : "/api/messages/1/2"
    path('messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('messages/', views.message_list, name='message-list'),   # For POST
    # URL form "/api/users/1"
    path('users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    path('users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
]