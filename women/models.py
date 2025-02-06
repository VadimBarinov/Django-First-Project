from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    # blank=True можно не передавать значение при создании записи
    content = models.TextField(blank=True)
    # auto_now_add=True автозаполнение времени в момент первого появления
    time_create = models.DateTimeField(auto_now_add=True)
    # auto_now=True автозаполнение времени при любом изменении записи
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)