from django.db import models
from django.contrib import admin
from category.models import Category
from blog.models import Post
from django.template.defaultfilters import slugify
from django.db.models import Max


class Practice(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    related_posts = models.ManyToManyField(Post, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'practice'


class Exercise(models.Model):
    EASY = 'E'
    MEDIUM = 'M'
    DIFFICULT = 'D'
    CHOICES = (
        (EASY, "Easy"),
        (MEDIUM, "Medium"),
        (DIFFICULT, "Difficult"),
    )

    number = models.IntegerField(blank=True)
    practise = models.ForeignKey(Practice, on_delete=models.CASCADE)
    difficulty = models.CharField(
        choices=CHOICES, default=MEDIUM, max_length=1)
    exercise = models.TextField()
    tip = models.TextField(blank=True)
    solution = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        already_created = Exercise.objects.filter(pk=self.pk).exists()
        last_number = Exercise.objects.filter(
            practise=self.practise).values('number').order_by('-number').first()

        if already_created:
            self.number = self.number

        elif last_number and already_created == False:
            self.number = last_number['number'] + 1
        else:
            self.number = 1
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return f'{self.practise}-{self.number}'


admin.site.register(Exercise)
