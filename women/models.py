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

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    # blank=True можно не передавать значение при создании записи
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    # auto_now_add=True автозаполнение времени в момент первого появления
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    # auto_now=True автозаполнение времени при любом изменении записи
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=Status.DRAFT,
                                       # для правильного отображения в админ панели
                                       choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       verbose_name='Статус')

    # создаем связь один ко многим
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категории')

    # связь многие ко многим
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='Теги')

    # связь один к одному
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='women', verbose_name='Муж')

    objects = models.Manager()
    # новый менеджер
    published = PublishedManager()

    # чтобы отображался только title записи
    def __str__(self):
        return self.title

    # класс для сортировки по умолчанию
    class Meta:
        # для отображения в админ панели
        verbose_name = 'Известная женщина'
        # множественное число
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create']
        # индексация для быстрой сортировки
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    # возвращает полноценный url адрес для каждой записи
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name