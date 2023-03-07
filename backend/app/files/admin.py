from django.contrib import admin
from .models import Files


class AdminFiles(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'blog_file']


admin.site.register(Files, AdminFiles)
# Register your models here.
