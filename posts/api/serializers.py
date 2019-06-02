from rest_framework import serializers
from posts.models import Post, Category
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['slug', 'title']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'category']


class CategoryPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['slug', 'title', 'posts']