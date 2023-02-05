from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.core.management import call_command


def posts_list_url_by_category_id(category_id):
    """Create and return a recipe detail URL."""
    return reverse('blog:post-by-category-id', args=[category_id])


def posts_list_url_by_category_slug(category_slug):
    """Create and return a recipe detail URL."""
    return reverse('blog:post-by-category-slug', args=[category_slug])


def post_detail_url_by_id(post_id):
    """Create and return a recipe detail URL."""
    return reverse('blog:post-by-id', args=[post_id])


def post_detail_url_by_slug(post_slug):
    """Create and return a recipe detail URL."""
    return reverse('blog:post-by-slug', args=[post_slug])


class PostsListTest(TestCase):
    """Tests for post list by category id or category slug API endpoints"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures_API.json', verbosity=0)

    def setUp(self):
        self.client = APIClient()

    def test_method_post_not_allowed(self):
        res_by_id = self.client.post(posts_list_url_by_category_id(1))
        res_by_slug = self.client.post(posts_list_url_by_category_slug('sql'))
        self.assertEqual(res_by_id.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res_by_slug.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_put_not_allowed(self):
        res_by_id = self.client.put(posts_list_url_by_category_id(1))
        res_by_slug = self.client.put(posts_list_url_by_category_slug('sql'))
        self.assertEqual(res_by_id.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res_by_slug.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_patch_not_allowed(self):
        res_by_id = self.client.patch(posts_list_url_by_category_id(1))
        res_by_slug = self.client.patch(posts_list_url_by_category_slug('sql'))
        self.assertEqual(res_by_id.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res_by_slug.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_delete_not_allowed(self):
        res_by_id = self.client.delete(posts_list_url_by_category_id(1))
        res_by_slug = self.client.delete(
            posts_list_url_by_category_slug('sql'))
        self.assertEqual(res_by_id.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res_by_slug.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_posts_by_category_id(self):
        res_by_id = self.client.get(posts_list_url_by_category_id(2))
        self.assertEqual(res_by_id.data['category']['id'], 2)
        self.assertEqual(res_by_id.data['category']['slug'], 'sql')
        self.assertEqual(res_by_id.data['category']['name'], 'SQL')
        self.assertEqual(res_by_id.data['category']['posts'], 2)
        self.assertEqual(len(res_by_id.data['posts']), 2)
        self.assertEqual(
            res_by_id.data['posts'][0]['title'], 'Co to jest relacyjna baza danych?')
        self.assertEqual(
            res_by_id.data['posts'][0]['slug'], 'co-to-jest-relacyjna-baza-danych')
        self.assertEqual(len(res_by_id.data['posts'][0]['tag']), 2)

    def test_get_posts_by_category_slug(self):
        res_by_slug = self.client.get(posts_list_url_by_category_slug('sql'))
        self.assertEqual(res_by_slug.data['category']['id'], 2)
        self.assertEqual(res_by_slug.data['category']['slug'], 'sql')
        self.assertEqual(res_by_slug.data['category']['name'], 'SQL')
        self.assertEqual(res_by_slug.data['category']['posts'], 2)
        self.assertEqual(len(res_by_slug.data['posts']), 2)
        self.assertEqual(
            res_by_slug.data['posts'][0]['title'], 'Co to jest relacyjna baza danych?')
        self.assertEqual(
            res_by_slug.data['posts'][0]['slug'], 'co-to-jest-relacyjna-baza-danych')
        self.assertEqual(len(res_by_slug.data['posts'][0]['tag']), 2)


class PostDetailsTest(TestCase):
    """Tests for post details by id or  slug API endpoints"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures_API.json', verbosity=0)

    def setUp(self):
        self.client = APIClient()

    def test_method_post_not_allowed(self):
        res_by_id = self.client.post(post_detail_url_by_id(1))
        res_by_slug = self.client.post(post_detail_url_by_slug('sql'))
        self.assertEqual(res_by_id.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res_by_slug.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_put_not_allowed(self):
        res_by_id = self.client.put(post_detail_url_by_id(1))
        res_by_slug = self.client.put(post_detail_url_by_slug('sql'))
        self.assertEqual(res_by_id.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res_by_slug.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_patch_not_allowed(self):
        res_by_id = self.client.patch(post_detail_url_by_id(1))
        res_by_slug = self.client.patch(post_detail_url_by_slug('sql'))
        self.assertEqual(res_by_id.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res_by_slug.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_delete_not_allowed(self):
        res_by_id = self.client.delete(post_detail_url_by_id(1))
        res_by_slug = self.client.delete(post_detail_url_by_slug('sql'))
        self.assertEqual(res_by_id.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(res_by_slug.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_details_by_id(self):
        res_by_id = self.client.get(post_detail_url_by_id(1))
        self.assertEqual(
            res_by_id.data['post']['title'], 'Co to jest relacyjna baza danych?')
        self.assertEqual(
            res_by_id.data['post']['slug'], 'co-to-jest-relacyjna-baza-danych')
        self.assertEqual(res_by_id.data['post']['id'], 1)
        self.assertEqual(res_by_id.data['post']['content'], '<h3>SQl</h3>')
        self.assertEqual(len(res_by_id.data['post']['tag']), 2)

        self.assertEqual(res_by_id.data['category']['id'], 2)
        self.assertEqual(res_by_id.data['category']['name'], 'SQL')
        self.assertEqual(res_by_id.data['category']['slug'], 'sql')
        self.assertEqual(res_by_id.data['category']['posts'], 2)
        self.assertEqual(res_by_id.data['category']['subcount'], 0)

    def test_post_details_by_slug(self):
        res_by_slug = self.client.get(
            post_detail_url_by_slug('co-to-jest-relacyjna-baza-danych'))
        self.assertEqual(
            res_by_slug.data['post']['title'], 'Co to jest relacyjna baza danych?')
        self.assertEqual(
            res_by_slug.data['post']['slug'], 'co-to-jest-relacyjna-baza-danych')
        self.assertEqual(res_by_slug.data['post']['id'], 1)
        self.assertEqual(res_by_slug.data['post']['content'], '<h3>SQl</h3>')
        self.assertEqual(len(res_by_slug.data['post']['tag']), 2)

        self.assertEqual(res_by_slug.data['category']['id'], 2)
        self.assertEqual(res_by_slug.data['category']['name'], 'SQL')
        self.assertEqual(res_by_slug.data['category']['slug'], 'sql')
        self.assertEqual(res_by_slug.data['category']['posts'], 2)
        self.assertEqual(res_by_slug.data['category']['subcount'], 0)
