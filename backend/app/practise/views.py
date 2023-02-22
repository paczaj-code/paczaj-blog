# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Practice
from category.models import Category
from .serializer import PracticeByCategorySerializer, BasicPractiseByCategorySlug, PracticeDetailsSerializer


class PractiseListAPIView(APIView):
    """View for category lists with recursive subcategories"""

    def get(self, request, *args, **kwargs):
        practices = Category.objects.raw('''
            WITH sub_query AS
                    (SELECT category.id AS category_id,
                            category.name AS cat_name,
                            category.parent_id,
                            count(practice.id) AS practice_count,
                            category.slug,
                            category.icon,
                            category.description
                    FROM category
                    JOIN practice ON practice.category_id = category.id
                    WHERE category.parent_id IS NOT NULL
                        AND category.is_enabled = TRUE
                        AND category_type = 'E'
                    GROUP BY category.name,
                            category.parent_id,
                            category.id),
                    sub_query2 AS
                    (SELECT sub_query.cat_name,
                            sub_query.slug,
                            sub_query.icon,
                            sub_query.practice_count,
                            count(exercise.id) AS exercise_count,
                            sub_query.parent_id as cat_parent_id
                    FROM practice
                    JOIN sub_query ON sub_query.category_id = practice.category_id
                    LEFT JOIN exercise ON exercise.practise_id = practice.id
                    GROUP BY sub_query.category_id,
                            sub_query.cat_name,
                            sub_query.practice_count,
                            sub_query.parent_id,
                            sub_query.slug,
                            sub_query.icon
                    ORDER BY sub_query.category_id DESC)
                SELECT category.id,
                    category.name,
                    json_agg(sub_query2) AS sub_categories
                from category
                inner join sub_query2 ON category.id = sub_query2.cat_parent_id

                GROUP BY category.name,
                        category.id

        ''')

        if len(practices) == 0:
            raise Http404()

        serializer = PracticeByCategorySerializer(practices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PractiseListByCategorySlugAPIView(APIView):
    def get_object_by_slug(self, slug):
        try:
            practise = Practice.objects.raw(
                """
       SELECT 
			 practice.id,
			 practice.title,
       practice.description,
			 practice.slug,
       category.slug AS category_slug,
       count(exercise.exercise) AS exersices_amount
        FROM practice
        JOIN category ON category.id = practice.category_id
        JOIN exercise ON exercise.practise_id = practice.id
        WHERE category.slug = %s AND practice.is_published = TRUE
            AND category.category_type = 'E'
        GROUP BY practice.title,
                category.slug,
         practice.description,
				 practice.slug,
				 practice.id
                 """, [slug])
            if practise == None:
                raise Http404()

            return practise
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        obj = self.get_object_by_slug(slug)

        serializer = BasicPractiseByCategorySlug(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PracticeDeatilsAPIView(APIView):
    def get_object_by_slug(self, slug):
        try:
            practise = Practice.objects.raw(
                """
       SELECT practice.id,
       practice.title,
       practice.slug,
       practice.description,

    (SELECT json_agg(e)
     FROM
         (SELECT exercise.id,
                 exercise.difficulty,
                 exercise.exercise,
                 exercise.tip,
                 exercise.solution, number
          FROM practice AS pr
          INNER JOIN exercise ON exercise.practise_id = pr.id
          WHERE pr.slug = practice.slug
          ORDER BY exercise.number) e) AS exercises,

    (SELECT json_agg(e)
     FROM
         (SELECT post.title,
                 post.id,
                 post.slug
          FROM practice as pr
          JOIN practice_related_posts ON practice_related_posts.practice_id = pr.id
          JOIN post ON post.id = practice_related_posts.post_id
          WHERE pr.slug = practice.slug ) e) AS realted_posts
            FROM practice
            WHERE practice.slug = %s
                 """, [slug])
            if practise == None:
                raise Http404()

            return practise[0]
        except Practice.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        obj = self.get_object_by_slug(slug)

        serializer = PracticeDetailsSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
