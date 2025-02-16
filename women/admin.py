from django.contrib import admin
from women.models import Women, Category


# admin.site.register(Women, WomenAdmin)
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    # отображаемые поля
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat')
    # кликабельные поля
    list_display_links = ('id', 'title')
    # порядок сортировки
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')