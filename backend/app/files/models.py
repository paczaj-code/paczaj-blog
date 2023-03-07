
from django.db import models


class Files(models.Model):
    """Model for files"""
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    blog_file = models.FileField(upload_to='files', blank=True, null=True)

    def __str__(self):
        return self.name
