from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse

from posts.models import Post
from posts.api.serializers import PostSerializer


class PostView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = "posts"
    template = "posts/post_list.html"


def json_list_published_posts(request):
    posts = Post.objects.filter(status='published')

    return JsonResponse(
        {
            "posts": [
                {
                    "title": p.title,
                    "slug": p.slug,
                    "id": p.id,
                    "published": p.when_published,
                }
                for p in posts
            ]
        }
    )


