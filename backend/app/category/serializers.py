from rest_framework import serializers
from collections import OrderedDict
from .models import Category
from blog.models import Post


class BasicCategorySerializer(serializers.ModelSerializer):
    """Serializer template for categories to be inherited"""
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'slug', 'posts', 'description']

    def get_posts(self, obj):
        """Add field post as count of related articles"""
        posts = Post.objects.filter(
            category_id__in=[obj], is_published=True).count()
        return posts


class PublicCategoryListSerializer(BasicCategorySerializer):
    """Serilazer for category list API with recursive subcategories"""
    subcategories_count = serializers.IntegerField()
    articles_count = serializers.IntegerField()
    sub_categories = serializers.ListField(child=serializers.JSONField())

    class Meta:
        model = Category
        fields = ['id', 'name', 'description',
                  'slug', 'icon', 'subcategories_count', 'articles_count', 'sub_categories']

    def to_representation(self, instance):
        """Clean of empty values and add count of subcategories"""
        result = super(PublicCategoryListSerializer,
                       self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None and result[key] != "" and result[key] != 0])


class PublicCategoryDetailSerializer(BasicCategorySerializer):
    """Serializer for category detail API """
    class Meta:
        model = Category
        fields = BasicCategorySerializer.Meta.fields + ['description']
