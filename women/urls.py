from tkinter.font import names

from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    # лучше всего к маршрутам обращаться по имени (name="..."),
    # чтобы не было хардкодинга.
    path("", views.index, name="home"),      # http://127.0.0.1:8000/
    path("about/", views.about, name="about"),      # http://127.0.0.1:8000/about/
    path("add_page/", views.add_page, name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("about/", views.about, name="about"),
    path("post/<slug:post_slug>/", views.show_post, name="post"),
    path("category/<slug:cat_slug>/", views.show_category, name="category"),
]