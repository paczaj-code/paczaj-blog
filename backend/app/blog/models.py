from django.db import models
from django.contrib import admin
from category.models import Category
from django.template.defaultfilters import slugify
import json
import requests
from django.utils.html import format_html


class Tag(models.Model):
    """Model for post tags"""
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tag'


# TODO Add file upload to mode
class Post(models.Model):
    """Model for posts"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    category = models.ForeignKey(
        Category, related_name='post_category', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag, blank=True)
    demo_css = models.TextField(null=True, blank=True)
    demo_js = models.TextField(null=True, blank=True)
    related_posts = models.ManyToManyField('Post', blank=True)
    image_id = models.CharField(max_length=255, blank=True, null=True)
    image = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.image_id:
            result = requests.get(
                f'https://api.unsplash.com/photos/{self.image_id}?client_id=eWnEhgP8URLT8IwJXSsslgayoKT2vkltpdJtfu-vrV8')

            image_data = {}

            image_data.update({'image_urls': result.json()['urls']})
            image_data.update({'author': {'id': result.json()['user']['id'], 'username': result.json()['user']['username'], 'name': result.json()['user']['name'],
                                          'html': result.json()['user']['links']['html']
                                          }})
            self.image = image_data
        else:
            self.image = None
        super().save(*args, **kwargs)

    def image_view(self):
        if self.image_id:
            urld = self.image
            url2 = urld['image_urls']['small']
            return format_html(
                f'<img src="{url2}"/>'
            )

        return format_html('<p>Brak obrazu</p>')
