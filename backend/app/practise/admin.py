from django.contrib import admin
from .models import Practice
from category.models import Category
# Register your models here.


class PractiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published',)
    list_filter = ('category', 'is_published',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(
                category_type="E", is_enabled=True, parent__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Practice, PractiseAdmin)
