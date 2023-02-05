from rest_framework.views import APIView
from rest_framework.response import Response
# from django.contrib import messages
from django.http import Http404

from rest_framework import status
from .serializers import (PublicCategoryListSerializer,
                          PublicCategoryDetailSerializer)
from .models import Category
from blog.models import Post


class CategoryListAPIView(APIView):
    """View for category lists with recursive subcategories"""

    def get(self, request, *args, **kwargs):
        # TODO resolve problem with filtering by is_enebled in subcategories
        # categories = Category.objects.filter(category_type='P',
        #                                      is_enabled=True, parent__isnull=True).order_by('id')

        categories = Category.objects.raw('''
            WITH
                sub_query
                AS
                (
                    SELECT c.id,
                        c.name,
                        c.parent_id,
                        COUNT(p.id) as articles_count,
                        c.slug,
                        c.icon,
                        c.description
                    FROM category c
                    LEFT JOIN post p on p.category_id=c.id
                    WHERE parent_id IS NOT NULL and is_enabled = TRUE AND category_type='P' AND p.is_published=TRUE
                    GROUP BY c.id,
                        c.name,
                        c.parent_id,
                        c.slug
                    ORDER BY c.id
                )
            SELECT
            mc.id,
                mc.name,
                mc.description,
                mc.slug,
                mc.icon,
                COUNT(sc.parent_id) as subcategories_count,
                SUM(sc.articles_count ) as articles_count,
                json_agg(sc) AS sub_categories
            FROM category mc
            INNER  JOIN sub_query sc on sc.parent_id=mc.id
            WHERE mc.is_enabled=TRUE
            GROUP BY mc.id
            ORDER BY mc.id

        ''')

        if len(categories) == 0:
            raise Http404()

        serializer = PublicCategoryListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailAPIViewByPkOrSlug(APIView):
    """View for category details"""

    def get_object_by_pk(self, pk):
        try:
            return Category.objects.get(pk=pk, is_enabled=True, category_type='P',)
        except Category.DoesNotExist:
            raise Http404

    def get_object_by_slug(self, slug):
        try:
            return Category.objects.get(slug=slug, is_enabled=True, category_type='P',)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk:
            obj = self.get_object_by_pk(pk)
        else:
            obj = self.get_object_by_slug(slug)
        serializer = PublicCategoryDetailSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
