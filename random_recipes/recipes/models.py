from django.contrib.sessions.base_session import AbstractBaseSession
from django.contrib.sessions.models import Session
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название', max_length=120)
    url_parameter = models.CharField('Параметр url', max_length=3,
                                     default=None, blank=True, null=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ("Категории")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk": self.pk})


class Recipe(models.Model):
    user = models.ForeignKey(Session, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    title = models.CharField('Название', max_length=120)
    slug = models.SlugField('Слаг', unique=True)
    tags = models.CharField('Тэги поиска', max_length=255,
                            default=None, blank=True, null=True)
    description = models.TextField('Описание')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, verbose_name='Категория',
        default=None, blank=True, null=True)

    def recipe_title_image_upload_to(self, filename):
        return f'recipes/{self.slug}/{filename}'

    title_image = models.ImageField(
        upload_to=recipe_title_image_upload_to,
        default=None, blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        default_related_name = 'recipes'


class Ingredient(models.Model):
    title = models.CharField('Название', max_length=120)
    count = models.CharField('Количество', max_length=120)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='ingredients')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Step(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='steps')

    def step_image_upload_to(self, filename):
        return f'recipes/{self.recipe.slug}/steps/{filename}'

    image = models.ImageField(
        upload_to=step_image_upload_to,
        default=None, blank=True, null=True, verbose_name="Фото")

    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'
