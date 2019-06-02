"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import PostView, json_list_published_posts
from posts.api.views import PostListView, PostDetailView, CategoryPostView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', PostView.as_view()),
    # path('api/posts/', json_list_published_posts),

    path('api/posts/', PostListView.as_view()),
    path('api/posts/<int:pk>', PostDetailView.as_view()),
    path('api/posts/category/', CategoryPostView.as_view()),
]
