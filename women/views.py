from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    return render(request, "women/index.html")


def about(request):
    return render(request, "women/about.html")


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