from django.contrib import admin

from apps.comment.models import Comment, Children

admin.site.register(Comment)
admin.site.register(Children)