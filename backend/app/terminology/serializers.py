from rest_framework import serializers
from .models import Term


class PublicTermListSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['id', 'definition',  'slug']


class PublicTermDetailSerializer(PublicTermListSerialzer):
    class Meta:
        model = Term
        fields = PublicTermListSerialzer.Meta.fields + ['description']


# TODO add categories to view
