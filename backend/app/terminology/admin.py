from django.contrib import admin
from .models import Term
from django import forms
from category.models import Category
# Register your models here.


class TermAdmin(admin.ModelAdmin):
    # pass
    list_display = ('definition', 'slug', 'category', 'is_enabled',)
    readonly_fields = ('slug', 'created_at', 'modified_at')

    fieldsets = (
        ('Content', {
            'fields': ('definition', 'description')
        }),
        ('Matadata', {
            'fields': ('category', 'is_enabled', 'slug', 'created_at', 'modified_at', )
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(
                category_type="T", is_enabled=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Term, TermAdmin)
