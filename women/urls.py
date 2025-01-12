from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    # лучше всего к маршрутам обращаться по имени (name="..."),
    # чтобы не было хардкодинга.
    path("", views.index, name="home"),      # http://127.0.0.1:8000/
    path("cats/<int:cat_id>/", views.categories, name="cats_id"),   # http://127.0.0.1:8000/cats/1/
    path("cats/<slug:cat_slug>/", views.categories_by_slug, name="cats"),   # http://127.0.0.1:8000/cats/dasda/
    path("archive/<year4:year>/", views.archive, name="archive"),
]