from django.urls import path
from .views import (PostListAPIViewByCategoryIdOrSlug,
                    PostDetailAPIViewByPostIdOrSlug)

urlpatterns = [
    # endpoint for post list by category id
    path('posts/<int:pk>', PostListAPIViewByCategoryIdOrSlug.as_view(),
         name='post-by-category-id'),
    # endpoint for post list by category slug
    path('posts/<str:slug>', PostListAPIViewByCategoryIdOrSlug.as_view(),
         name='post-by-category-slug'),
    path('post/<int:pk>', PostDetailAPIViewByPostIdOrSlug.as_view(),
         name='post-by-id'),
    # endpoint for post list by category slug
    path('post/<str:slug>', PostDetailAPIViewByPostIdOrSlug.as_view(),
         name='post-by-slug'),
]

app_name = 'blog'
