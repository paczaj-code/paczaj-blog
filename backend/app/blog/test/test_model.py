from blog.models import Post, Tag
from category.models import Category
from django.test import TestCase
from django.core.management import call_command


class TagTest(TestCase):
    """Tests for tag model"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures.json', verbosity=0)

    def test_inserted_fixtures(self):
        self.assertEqual(Tag.objects.all().count(), 3)

    def test_create_tag_without_name_raise_error(self):
        with self.assertRaises(Exception):
            Tag.objects.create(
                name=None)

    def test_create_tag_with_existing_name_raises_error(self):
        with self.assertRaises(Exception):
            Tag.objects.create(
                name=Tag.objects.get(id=1).name)

    def test_create_tag_successfull(self):
        Tag.objects.create(
            name="Tag 4", description="I'm tag 4", icon='some icon')

        self.assertEqual(Tag.objects.all().count(), 4)
        self.assertEqual(Tag.objects.last().name, 'Tag 4')
        self.assertEqual(Tag.objects.last().slug, 'tag-4')
        self.assertEqual(Tag.objects.last(
        ).description, "I'm tag 4")
        self.assertEqual(Tag.objects.last().icon, 'some icon')

    def test_update_category_successfull(self):
        tag = Tag.objects.last()
        tag.name = 'Tag 123'
        tag.description = 'New tag description'
        tag.icon = 'icon newest'
        tag.save()
        self.assertEqual(Tag.objects.last().name, 'Tag 123')
        self.assertEqual(Tag.objects.last().slug, 'tag-123')
        self.assertEqual(Tag.objects.last().description, 'New tag description')
        self.assertEqual(Tag.objects.last().icon, 'icon newest')

    def test_delete_tag(self):
        Tag.objects.last().delete()
        self.assertEqual(Tag.objects.all().count(), 2)


class PostTest(TestCase):
    """Tests for post model"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures.json', verbosity=0)

    def test_inserted_fixtures(self):
        self.assertEqual(Post.objects.all().count(), 2)
        self.assertEqual(Post.objects.get(id=1).title, 'Post 1 title')
        self.assertEqual(Post.objects.get(id=1).slug, 'post-1-title')
        self.assertEqual(Post.objects.get(id=1).content, 'Post 1 content')
        self.assertEqual(Post.objects.get(id=1).is_published, True)
        self.assertEqual(Post.objects.get(id=1).category.id, 1)
        self.assertEqual(Post.objects.get(id=1).tag.first().id, 1)
        self.assertEqual(Post.objects.get(id=1).tag.count(), 1)

    def test_create_post_with_without_title_raises_error(self):
        with self.assertRaises(Exception):
            Post.objects.create(
                title=None)

    def test_post_created_successfull(self):
        Post.objects.create(title='New title',
                            content='New content', category=Category.objects.get(id=3))
        Post.objects.last().tag.add(Tag.objects.last())
        Post.objects.last().tag.add(Tag.objects.first())
        Post.objects.last().related_posts.add(Post.objects.get(id=1))

        self.assertEqual(Post.objects.all().count(), 3)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().slug, 'new-title')
        self.assertEqual(Post.objects.last().content, 'New content')
        self.assertEqual(Post.objects.last().category.id, 3)
        self.assertEqual(Post.objects.last().tag.count(), 2)
        self.assertEqual(Post.objects.last().tag.first().id, 1)
        self.assertEqual(Post.objects.last().tag.last().id, 3)
        self.assertEqual(Post.objects.last().related_posts.last().id, 1)

    def test_update_post_success(self):
        post = Post.objects.last()
        post.title = 'Post 55'
        post.content = '<p>paragraph</p>'
        post.is_published = False
        post.category = Category.objects.get(id=3)
        post.tag.remove(Tag.objects.get(id=1))
        post.tag.add(Tag.objects.get(id=2))
        post.tag.add(Tag.objects.get(id=3))
        # post.related_posts.remove(Post.objects.get(id=1))
        post.save()
        self.assertEqual(Post.objects.last().title, 'Post 55')
        self.assertEqual(Post.objects.last().slug, 'post-55')
        self.assertEqual(Post.objects.last().content, '<p>paragraph</p>')
        self.assertEqual(Post.objects.last().is_published, False)
        self.assertEqual(Post.objects.last().category.id, 3)
        self.assertEqual(Post.objects.last().tag.count(), 2)
        self.assertEqual(Post.objects.last().related_posts.count(), 1)

    def test_delete_post_successfull(self):
        Post.objects.last().delete()
        self.assertEqual(Post.objects.all().count(), 1)


# # TODO dodać slug i powiązane ćwiczenia do post
