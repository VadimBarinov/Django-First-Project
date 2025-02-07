from django.db import models
from django.urls import reverse


# класс для кастомного менеджера
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    # класс для отображения в форме вместо (0/1) будет (черновик/опубликован)
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликован'

    title = models.CharField(max_length=255)
    # blank=True можно не передавать значение при создании записи
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    # auto_now_add=True автозаполнение времени в момент первого появления
    time_create = models.DateTimeField(auto_now_add=True)
    # auto_now=True автозаполнение времени при любом изменении записи
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=Status.DRAFT, choices=Status.choices)

    # создаем связь один ко многим
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')

    # связь многие ко многим
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')

    objects = models.Manager()
    # новый менеджер
    published = PublishedManager()

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


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag