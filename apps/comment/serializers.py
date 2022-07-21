from rest_framework import serializers

from apps.comment.models import Comment, Children


class ChildrenSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Children
        read_only_fields = ('id', 'owner')
        fields = (
            'id',
            'title',
            'parent',
            'create_at'
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        read_only_fields = ('id', 'owner')
        fields = (
            'id',
            'comment',
            'star',
            'create_at',
            'product',
        )