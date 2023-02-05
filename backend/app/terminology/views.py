from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Term
from .serializers import PublicTermListSerialzer, PublicTermDetailSerializer


class TermListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        terms = Term.objects.filter(is_enabled=True).order_by('definition')
        serializer = PublicTermListSerialzer(terms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TermDetailAPIViewByPK(APIView):
    def get_object(self, pk):
        try:
            return Term.objects.get(pk=pk)
        except Term.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        term = self.get_object(pk)
        serializer = PublicTermDetailSerializer(term)
        return Response(serializer.data)


class TermDetailAPIViewBySlug(APIView):
    def get_object(self, slug):
        try:
            return Term.objects.get(slug=slug)
        except Term.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        term = self.get_object(slug)
        serializer = PublicTermDetailSerializer(term)
        return Response(serializer.data)
