from django.urls import path
from .views import (CategoryListAPIView, CategoryDetailAPIViewByPkOrSlug)

urlpatterns = [
    # endpoint for categpry list
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    # endpoint for categpry detail by category id
    path('category/<int:pk>', CategoryDetailAPIViewByPkOrSlug.as_view(),
         name='category-by-id'),
    # endpoint for categpry detail by category slug
    path('category/<str:slug>', CategoryDetailAPIViewByPkOrSlug.as_view(),
         name='category-by-slug'),
]


app_name = 'category'
