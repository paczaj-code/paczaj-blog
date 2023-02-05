from django.contrib import admin
from .models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'category_type', 'is_enabled', 'parent')
    list_filter = ('category_type', 'is_enabled', 'parent')


admin.site.register(Category, CategoryAdmin)
