from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Shop API')

urlpatterns = [
    path('admin/', admin.site.urls), # admin
    path('', schema_view), # swagger
    path('accounts/', include('allauth.urls')),
    path('product/', include('apps.product.urls')), # model Product
    path('chat/', include('apps.chat.urls')), # model Chat
    path('user/', include('apps.users.urls')), # model User
    path('favorite/', include('apps.favorite.urls')), # model Favorite
    path('comment/', include('apps.comment.urls')), # model Comment
    path('category/', include('apps.category.urls')), # model Category
    # path('auth/', include('djoser.urls')), # djoser регистрация
    # path('auth/', include('djoser.urls.authtoken')), # djoser вход и вызод из системы
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)