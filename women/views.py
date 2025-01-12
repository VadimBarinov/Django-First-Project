from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    data = {
        "title": "Главная страница",
        "menu": menu,
        "float": 28.56,
        "lst": [1, 2, "abc", True],
        "set": {1, 2, 4, 6},
        "dict": {
            "key_1": "value_1",
            "key_2": "value_2",
        },
        "obj": MyClass(10, 20),
        # фильтры можно использовать и в самом питоне
        "url": slugify("The Main Page"),
    }
    return render(request, "women/index.html", context=data)


def about(request):
    data = {"title": "О сайте"}
    return render(request, "women/about.html", data)


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2025:
        # вычисление URL адреса
        uri = reverse("cats", args=("sport",))

        # перенаправление на главную страницу
        # если permanent=True, то код 301 (другой постоянный URL адрес)
        #      permanent=False(или не указан), то 302 (временный URL адрес)
        return redirect(uri, permanent=True)

        # второй способ через классы джанго
        # return HttpResponseRedirect(uri)
        # return HttpResponsePermanentRedirect(uri)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


# функция для обработки 404
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")