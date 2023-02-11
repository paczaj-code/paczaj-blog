from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import (PublicCategoryListSerializer,
                          PublicCategoryDetailSerializer)
from .models import Category
from blog.models import Post


class CategoryListAPIView(APIView):
    """View for category lists with recursive subcategories"""

    def get(self, request, *args, **kwargs):
        categories = Category.objects.raw('''
            WITH
                sub_query
                AS
                (
                    SELECT category.id,
                        category.name,
                        category.parent_id,
                        count(post.id) AS articles_count,
                        category.slug,
                        category.icon,
                        category.description
                    FROM category
                    LEFT JOIN post  ON post.category_id = category.id
                    WHERE parent_id IS NOT NULL AND is_enabled = TRUE AND category_type = 'P' AND post.is_published = TRUE
                    GROUP BY category.id,
                        category.name,
                        category.parent_id,
                        category.slug
                    ORDER BY category.id
                )
            SELECT
            category.id,
                category.name,
                category.description,
                category.slug,
                category.icon,
                count(sub_query.parent_id) AS subcategories_count,
                sum(sub_query.articles_count ) AS articles_count,
                json_agg(sub_query) AS sub_categories
            FROM category
            INNER  JOIN sub_query ON sub_query.parent_id = category.id
            WHERE category.is_enabled = TRUE
            GROUP BY category.id
            ORDER BY category.id

        ''')

        if len(categories) == 0:
            raise Http404()

        serializer = PublicCategoryListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailAPIViewBySlug(APIView):
    """View for category details"""

    def get_object_by_slug(self, slug):
        try:
            return Category.objects.get(slug=slug, is_enabled=True, category_type='P',)
            # )
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        obj = self.get_object_by_slug(slug)
        serializer = PublicCategoryDetailSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
