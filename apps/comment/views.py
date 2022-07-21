from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.comment.permissions import IsOwner
from apps.comment.serializers import CommentSerializer, ChildrenSerializer
from apps.comment.models import Comment


class CommentAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser or IsAuthenticatedOrReadOnly or IsOwner]

    def get(self, request):
        f = Comment.objects.filter(owner=request.user)
        return Response(CommentSerializer(f, many=True).data)


class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CommentDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner, IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CommentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)