from rest_framework import generics
from posts.models import Post, Category
from posts.api.serializers import PostSerializer, CategoryPostsSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryPostView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryPostsSerializer