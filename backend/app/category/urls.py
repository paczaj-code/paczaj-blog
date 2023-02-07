from django.urls import path
from .views import (CategoryListAPIView, CategoryDetailAPIViewBySlug)

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<str:slug>', CategoryDetailAPIViewBySlug.as_view(),
         name='category-by-slug'),
]

app_name = 'category'
