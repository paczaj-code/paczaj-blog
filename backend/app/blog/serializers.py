from rest_framework import serializers
from collections import OrderedDict
from blog.models import Tag, Post
from category.serializers import PublicCategoryDetailSerializer


class BasicPostSerializer(serializers.ModelSerializer):
    """Serializer template for post to be inherited"""

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug']


class PostListSerializer(BasicPostSerializer):
    image_url = serializers.CharField()
    image_author_data = serializers.JSONField()
    created_at = serializers.CharField()
    modified_at = serializers.CharField()
    article_tags = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = Post
        fields = BasicPostSerializer.Meta.fields + \
            ['image_url', 'image_author_data', 'created_at',
                'modified_at', 'article_tags',]


class PostsByCategorySlugSerializer(serializers.Serializer):
    posts = PostListSerializer(many=True)
    category = PublicCategoryDetailSerializer()
    tags = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        fields = ['posts', 'category', 'tags']


class PostDetailSerializer(BasicPostSerializer):
    image_url = serializers.CharField()
    image_author_data = serializers.JSONField()
    created_at = serializers.CharField()
    modified_at = serializers.CharField()
    article_tags = serializers.ListSerializer(
        child=serializers.CharField())
    content = serializers.CharField()
    category_name = serializers.CharField()
    category_icon = serializers.CharField()
    category_slug = serializers.CharField()
    glossary_items = serializers.ListSerializer(child=serializers.CharField())
    chapters = serializers.ListSerializer(child=serializers.CharField())
    related_post = serializers.ListSerializer(child=serializers.CharField())
    next_article = serializers.JSONField()
    prev_article = serializers.JSONField()

    class Meta:
        model = Post
        fields = BasicPostSerializer.Meta.fields + \
            ['image_url', 'image_author_data', 'created_at',
                'modified_at', 'article_tags', 'content', 'category_name', 'category_icon', 'category_slug',
                'glossary_items', 'next_article', 'prev_article', 'chapters', 'related_post']

    def to_representation(self, instance):
        """Clean of empty values and add count of subcategories"""
        result = super(PostDetailSerializer,
                       self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None and result[key] != "" and result[key] != 0])


class AllPublishedPostsSerializer(BasicPostSerializer):
    category_slug = serializers.CharField()

    class Meta:
        model = Post
        fields = BasicPostSerializer.Meta.fields + ['category_slug']
