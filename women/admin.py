from django.contrib import admin, messages

from women.models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull = False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull = True)


# admin.site.register(Women, WomenAdmin)
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    # отображаемые поля
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brif_info')
    # кликабельные поля
    list_display_links = ('title',)
    # порядок сортировки
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'is_published', MarriedFilter]

    @admin.display(description='Краткое описание')
    def brif_info(self, women: Women):
        return f"Описание {len(women.content)} символов."


    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published = Women.Status.PUBLISHED)
        self.message_user(request, f"{count} записей опубликованы.")

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        # messages.WARNING - изменяет иконку сообщения на тип WARNING
        self.message_user(request, f"{count} записей снято с публикации.", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')