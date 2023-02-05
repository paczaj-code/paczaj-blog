from django.test import TestCase
from django.core.management import call_command
from category.models import Category


class CategoryTest(TestCase):
    """Test for Category models"""

    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures.json', verbosity=0)

    def test_inserted_fixtures(self):
        """Test inserted fixtures"""
        self.assertEqual(Category.objects.get(id=1).name, 'Category 1')
        self.assertEqual(Category.objects.get(id=2).slug, 'category-2')
        self.assertEqual(Category.objects.get(id=3).category_type, 'P')
        self.assertEqual(Category.objects.get(
            id=1).description, "I'm category 1")
        self.assertEqual(Category.objects.get(id=2).icon, 'icon 2')
        self.assertEqual(Category.objects.get(id=1).is_enabled, True)
        self.assertEqual(Category.objects.get(
            id=3).parent, Category.objects.get(id=1))

    def test_create_category_without_name_raises_error(self):
        """Test creating category without name should raise error"""
        with self.assertRaises(Exception):
            Category.objects.create(name=None)

    def test_create_category_with_existing_name_raises_error(self):
        """Test creating category with existing name should raise error"""
        with self.assertRaises(Exception):
            Category.objects.create(name=Category.objects.get(id=1).name)

    def test_creating_new_category(self):
        """Test creating new category"""
        Category.objects.create(
            name="category 5", icon='icon 5', category_type='E')

        self.assertEqual(Category.objects.count(), 5)
        self.assertEqual(Category.objects.last().name, 'category 5')
        self.assertEqual(Category.objects.last().slug, 'category-5')
        self.assertEqual(Category.objects.last().category_type, 'E')

    def test_updating_category(self):
        """Tests updating category"""

        category = Category.objects.get(id=1)
        category.name = "New name"
        category.icon = "new icon"
        category.category_type = "T"
        category.description = "new desc"
        category.parent = Category.objects.get(id=3)
        category.save()

        self.assertEqual(Category.objects.get(id=1).name, 'New name')
        self.assertEqual(Category.objects.get(id=1).slug, 'new-name')
        self.assertEqual(Category.objects.get(id=1).icon, 'new icon')
        self.assertEqual(Category.objects.get(id=1).category_type, 'T')
        self.assertEqual(Category.objects.get(
            id=1).parent, Category.objects.get(id=3))

    def test_deleting_category(self):
        Category.objects.last().delete()
        self.assertEqual(Category.objects.count(), 3)
