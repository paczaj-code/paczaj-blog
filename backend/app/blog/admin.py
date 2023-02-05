import json
from django.contrib import admin
from django.utils.html import format_html

from django import forms
from .models import Post, Tag
from category.models import Category
# Register your models here.


# class PrettyJSONEncoder(json.JSONEncoder):
#     def __init__(self, *args, indent, sort_keys, **kwargs):
#         super().__init__(*args, indent=2, sort_keys=True, **kwargs)


# class PostForm(forms.ModelForm):
#     json_field = forms.JSONField(encoder=PrettyJSONEncoder)


class PostAdmin(admin.ModelAdmin):
    # form = PostForm
    list_display = ('upper_case_title', 'category', 'is_published',)
    list_filter = ('category', ('is_published', admin.BooleanFieldListFilter),)
    readonly_fields = ('slug', 'image', 'created_at',
                       'modified_at', 'image_view')

    fieldsets = (
        ('Content', {
            'fields': ('title', 'content')
        }),
        ('Matadata', {
            'fields': ('category', 'tag', 'related_posts', 'is_published', 'slug', 'created_at', 'modified_at', )
        }),
        ('Image', {
            'fields': ('image_id', 'image_view', 'image'),
        }),
        ('Demo CSS', {
            'fields': ('demo_css',),
        }),
        ('Demo JS', {
            'fields': ('demo_js',),
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(
                category_type="P", is_enabled=True, parent__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    @admin.display(description='Title')
    def upper_case_title(self, obj):
        return ("%s" % (obj.title)).upper()

    def image_view(self, obj):
        return obj.image_view()


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
