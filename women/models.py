from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    # blank=True можно не передавать значение при создании записи
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    # auto_now_add=True автозаполнение времени в момент первого появления
    time_create = models.DateTimeField(auto_now_add=True)
    # auto_now=True автозаполнение времени при любом изменении записи
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    # чтобы отображался только title записи
    def __str__(self):
        return self.title

    # класс для сортировки по умолчанию
    class Meta:
        ordering = ['-time_create']
        # индексация для быстрой сортировки
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    # возвращает полноценный url адрес для каждой записи
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})