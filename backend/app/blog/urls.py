from django.urls import path
from .views import (PostListAPIViewByCategorySlug,
                    PostDetailAPIView, AllPublishedPostsAPIView)

urlpatterns = [
    path('posts/', AllPublishedPostsAPIView.as_view(),
         name='post-by-category-id'),
    path('posts/<str:slug>', PostListAPIViewByCategorySlug.as_view(),
         name='post-by-category-slug'),
    path('post/<str:slug>', PostDetailAPIView.as_view(),
         name='post-by-slug'),
]

app_name = 'blog'
