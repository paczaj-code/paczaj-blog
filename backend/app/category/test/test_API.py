
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.core.management import call_command

CATEGORY_URL = reverse('category:category-list')


def category_detail_url_by_id(category_id):
    """Create and return a recipe detail URL."""
    return reverse('category:category-by-id', args=[category_id])


def category_detail_url_by_slug(category_slug):
    """Create and return a recipe detail URL."""
    return reverse('category:category-by-slug', args=[category_slug])


class PublicCategoryListAPITests(TestCase):
    """Tests for public category list API endpoints"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures_API.json', verbosity=0)

    def setUp(self):
        self.client = APIClient()

    def test_method_post_not_allowed(self):
        res = self.client.post(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_put_not_allowed(self):
        res = self.client.put(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_patch_not_allowed(self):
        res = self.client.patch(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_delete_not_allowed(self):
        res = self.client.delete(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_categories_list(self):
        res = self.client.get(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(
            len(res.data[0]['subcategories']), res.data[0]['subcount'])
        self.assertEqual(res.data[0]['subcategories']
                         [0]['name'], 'Django')
        self.assertEqual(res.data[0]['subcategories'][1]['name'], 'SQL')
        self.assertEqual(res.data[0]['subcategories'][0]['slug'], 'django')
        self.assertEqual(res.data[0]['slug'], 'bazy-danych')


class PublicCategoryDetailAPITests(TestCase):
    """Tests for public category detail API endpoints"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures_API.json', verbosity=0)

    def test_method_post_not_allowed(self):
        url = category_detail_url_by_id(1)
        res = self.client.post(url)
        # res = self.client.post(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_put_not_allowed(self):
        url = category_detail_url_by_id(1)
        res = self.client.put(url)
        # res = self.client.post(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_patch_not_allowed(self):
        url = category_detail_url_by_id(1)
        res = self.client.patch(url)
        # res = self.client.post(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_delete_not_allowed(self):
        url = category_detail_url_by_id(1)
        res = self.client.delete(url)
        # res = self.client.post(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_result_detail_category_by_id(self):
        url = category_detail_url_by_id(1)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], 1)
        self.assertEqual(res.data['subcount'], 2)
        self.assertEqual(res.data['name'], 'Bazy danych')
        self.assertEqual(res.data['slug'], 'bazy-danych')

    def test_result_detail_category_by_slug(self):
        url = category_detail_url_by_slug('mongodb')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], 3)
        self.assertEqual(res.data['subcount'], 0)
        self.assertEqual(res.data['name'], 'MongoDB')
        self.assertEqual(res.data['slug'], 'mongodb')
        self.assertEqual(res.data['description'], 'Co to jest Mongo?')
