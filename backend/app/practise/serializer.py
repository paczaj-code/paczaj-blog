from rest_framework import serializers
from .models import Practice
from category.models import Category


class PracticeByCategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.JSONField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'sub_categories']


class BasicPractiseByCategorySlug(serializers.ModelSerializer):
    category_slug = serializers.CharField()
    exersices_amount = serializers.IntegerField()

    class Meta:
        model = Practice
        fields = ['id', 'slug', 'title', 'description',
                  'category_slug', 'exersices_amount']


class PracticeDetailsSerializer(serializers.ModelSerializer):
    # practise = BasicPractiseByCategorySlug(many=True)
    exercises = serializers.JSONField()
    realted_posts = serializers.JSONField()

    class Meta:
        model = Practice
        fields = ['id', 'title', 'slug', 'description',
                  'realted_posts', 'exercises']
