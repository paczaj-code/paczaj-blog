from .models import Post, Tag
from category.models import Category
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import (PostsByCategorySlugSerializer, PostDetailSerializer,
                          AllPublishedPostsSerializer
                          )


class PostListAPIViewByCategorySlug(APIView):
    """View for posts list with category data"""

    def get_objects_by_category_slug(self, slug):
        try:
            posts = Post.objects.raw(
                f'''
                SELECT P.ID,
	                P.TITLE,
	                P.SLUG,
	                TO_CHAR(P.CREATED_AT,
		            'DD-MM-YYYY') AS CREATED_AT,
	                TO_CHAR(P.MODIFIED_AT,
		            'DD-MM-YYYY') AS MODIFIED_AT,
	                IMAGE::JSON->'image_urls'->'small' AS IMAGE_URL,
	                IMAGE::JSON-> 'author' AS IMAGE_AUTHOR_DATA,
	                ARRAY_AGG(DISTINCT T.NAME) AS ARTICLE_TAGS
                    FROM POST AS P
                    INNER JOIN CATEGORY AS C ON C.ID = P.CATEGORY_ID
                    LEFT JOIN POST_TAG AS PT ON PT.POST_ID = P.ID
                    LEFT JOIN TAG AS T ON T.ID = PT.TAG_ID
                    WHERE C.SLUG = '{slug}' AND p.is_published=TRUE
                    GROUP BY P.ID
                    ORDER BY P.CREATED_AT;

                '''
            )
            category = Category.objects.get(
                slug=slug, is_enabled=True, category_type='P',)
            tags = Tag.objects.raw(f'''
                        SELECT t.id,  ARRAY_AGG(DISTINCT  t.name) FROM tag t
            INNER JOIN post_tag pt ON pt.tag_id = t.id
            INNER JOIN post p ON pt.post_id=p.id
            INNER JOIN category c ON p.category_id=c.id
            WHERE c.slug = '{slug}' AND p.is_published=TRUE
            GROUP BY t.id
            ''')
            obj = {'posts': posts, 'category': category, 'tags': tags}

            if len(posts) == 0:
                raise Http404
            return obj
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        obj = self.get_objects_by_category_slug(slug)
        serializer = PostsByCategorySlugSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailAPIView(APIView):
    def get_object_by_slug(self, slug):
        try:
            post = Post.objects.raw(
                """
                    SELECT post.id,
                        post.title,
                        post.content,
                        post.is_published,
                        post.slug,
                        to_char(post.created_at, 'DD-MM-YYYY') AS created_at,
                        to_char(post.modified_at, 'DD-MM-YYYY') AS modified_at,
                        category.name AS category_name,
                        category.icon AS category_icon,
                        category.slug AS category_slug,
                        array_agg(DISTINCT tag.name) AS article_tags,
                        image::JSON->'image_urls'-> 'small' AS image_url,
                        image::JSON-> 'author' AS image_author_data,
                        array(SELECT array_to_string(regexp_matches(post.content, '<span.*data-slug.*</span>', 'gm'),'')) AS glossary_items,
                        array(SELECT array_to_string(regexp_matches(content,'<h3.*class="chapter".*\n.*\n<\/h3>', 'gm'),'')) as chapters,
                        (SELECT json_agg(e)
                        FROM (
                        SELECT p.title, p.slug, p.id FROM post_related_posts
                        INNER JOIN post AS p ON p.id = post_related_posts.to_post_id
                        WHERE post_related_posts.from_post_id = post.id
                            ORDER BY post.id
                            ) e) AS related_post,
                          (SELECT row_to_json(t)
                                FROM (
                                (SELECT p.id,
                                        p.title,
                                        p.slug
                                    FROM post AS p
                                    WHERE p.id < post.id AND p.category_id = post.category_id AND p.is_published=TRUE
                                    ORDER BY p.id DESC 
                                    LIMIT 1)) AS t) AS prev_article,
                            (SELECT row_to_json(t)
                            FROM (
                            (SELECT p.id,
                                    p.title,
                                    p.slug
                                FROM post AS p
                                WHERE p.id > post.id AND p.category_id = post.category_id AND p.is_published=TRUE
                                ORDER BY p.id
                                LIMIT 1

                                )) AS t) AS next_article


                    FROM post
                    JOIN category ON category.id = post.category_id
                    LEFT JOIN post_tag ON post_tag.post_id = post.id
                    INNER JOIN tag ON tag.id = post_tag.tag_id
                    WHERE post.slug = %s AND post.is_published=TRUE
                    GROUP BY post.id,
                            category.name,
                            category.icon,
                            category.slug;
            """, [slug]
            )
# TODO zmienić f stringi w zapytaniach
            if post == None:
                raise Http404()

            return post[0]
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        obj = self.get_object_by_slug(slug)

        serializer = PostDetailSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllPublishedPostsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.raw(
            '''SELECT post.id, post.slug , category.slug AS category_slug
                FROM post 
                JOIN category ON category.id = post.category_id
                WHERE post.is_published = TRUE'''
        )

        serializer = AllPublishedPostsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
