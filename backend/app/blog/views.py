from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import (
    PostsListByCategorySerializer, PostDetailByPostIdOrSlug)
from category.models import Category
from .models import Post, Tag


class PostListAPIViewByCategoryIdOrSlug(APIView):
    """View for posts list with category data"""

    def get_objects_by_pk(self, pk):
        try:
            posts = Post.objects.filter(
                category_id=pk, is_published=True).order_by('created_at')
            category = Category.objects.get(
                pk=pk, is_enabled=True, category_type='P',)
            obj = {'posts': posts, 'category': category}
            return obj
        except Category.DoesNotExist:
            raise Http404

    def get_objects_by_slug(self, slug):
        try:
            posts = Post.objects.filter(
                category__slug=slug, is_published=True).order_by('created_at')
            category = Category.objects.get(
                slug=slug, is_enabled=True, category_type='P',)
            tag = Tag.objects.raw(f'''
                        SELECT t.id,  ARRAY_AGG(DISTINCT  t.name) FROM tag t
            INNER JOIN post_tag pt ON pt.tag_id = t.id
            INNER JOIN post p ON pt.post_id=p.id
            INNER JOIN category c ON p.category_id=c.id
            WHERE c.slug = '{slug}'
            GROUP BY t.id
            ''')
            obj = {'posts': posts, 'category': category, 'tags': tag}
            return obj
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk:
            obj = self.get_objects_by_pk(pk)
        else:
            obj = self.get_objects_by_slug(slug)
        serializer = PostsListByCategorySerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailAPIViewByPostIdOrSlug(APIView):
    def get_objects_by_pk(self, pk):
        try:
            post = Post.objects.get(pk=pk, is_published=True)
            category = Category.objects.get(
                id=post.category.id, is_enabled=True)
            obj = {'post': post, 'category': category}
            return obj
        except Post.DoesNotExist:
            raise Http404

    def get_objects_by_slug(self, slug):
        try:
            post = Post.objects.get(
                slug=slug, is_published=True)
            category = Category.objects.get(
                id=post.category.id, is_enabled=True)
            obj = {'post': post, 'category': category}
            return obj
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk:
            obj = self.get_objects_by_pk(pk)
        else:
            obj = self.get_objects_by_slug(slug)
        serializer = PostDetailByPostIdOrSlug(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
