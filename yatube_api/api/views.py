from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post, Group
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author', 'group')
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        post = self.get_post()
        return post.comments.select_related('author')

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)
