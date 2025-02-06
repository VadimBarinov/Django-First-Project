from django import template
import women.views as views


# регистрация новых тегов
register = template.Library()

# простой тег для получения категорий
@register.simple_tag(name='get_cats')
def get_categories():
    return views.cats_db


# включающий тег
@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {'cats': cats, 'cat_selected': cat_selected}