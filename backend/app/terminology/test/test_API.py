from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from terminology.models import Term
from terminology.serializers import PublicTermDetailSerializer, PublicTermListSerialzer
from django.core.management import call_command
TERMINOLOGY_URL = reverse('terminology:term-list')


def detail_id_url(term_id):
    return reverse('terminology:term-detail-id', args=[term_id])


def detail_slug_url(term_slug):
    return reverse('terminology:term-detail-slug', args=[term_slug])


class PublicTerminologyApiTests(TestCase):
    """Test public terminology  API endpoints."""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures_API.json', verbosity=0)

    def setUp(self):
        self.client = APIClient()

    def test_method_post_is_not_allowed(self):
        res = self.client.post(TERMINOLOGY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_put_is_not_allowed(self):
        res = self.client.put(TERMINOLOGY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_patch_is_not_allowed(self):
        res = self.client.patch(TERMINOLOGY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_delete_is_not_allowed(self):
        res = self.client.delete(TERMINOLOGY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_of_terms_OK(self):
        terms = Term.objects.all()
        serializer = PublicTermListSerialzer(terms, many=True)
        res = self.client.get(TERMINOLOGY_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)
        self.assertEqual(res.data[0]['definition'], 'What is 1')
        self.assertEqual(res.data[0]['slug'], 'what-is-1')
        self.assertEqual(res.data, serializer.data)

    def test_detail_of_term_with_id_API(self):
        term = Term.objects.get(id=1)
        serializer = PublicTermDetailSerializer(term)
        url = detail_id_url(1)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['definition'], 'What is 1')
        self.assertEqual(res.data['slug'], 'what-is-1')
        self.assertEqual(res.data['description'], 'Term 1 is')
        self.assertEqual(res.data, serializer.data)

    def test_detail_of_term_with_slug_API(self):
        term = Term.objects.get(id=3)
        serializer = PublicTermDetailSerializer(term)
        url = detail_slug_url('what-is-3')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['definition'], 'What is 3')
        self.assertEqual(res.data['slug'], 'what-is-3')
        self.assertEqual(res.data['description'], 'Term 3 is')
        self.assertEqual(res.data, serializer.data)


# TODO add test fot 404 errors
