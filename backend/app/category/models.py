from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    """Model for post categories"""

    POST = 'P'
    PRACTISE = 'E'
    TERM = 'T'
    CHOICES = (
        (POST, "Post"),
        (PRACTISE, "Practise"),
        (TERM, "Terminology"),
    )
    name = models.CharField(max_length=150)
    category_type = models.CharField(
        max_length=1, choices=CHOICES, default=POST)
    icon = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)
    parent = models.ForeignKey(
        'Category', related_name='subcategories', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category_type'], name='unique_category_type'),
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
