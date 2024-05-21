from django.db import models
from django.urls import reverse


class RecipeModel(models.Model):
    recipe_name = models.CharField(max_length=100, unique=True, verbose_name='Название рецепта')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    recipe_feature = models.TextField(verbose_name='Описание рецепта')
    ingredient = models.ManyToManyField('Ingredients', related_name='ingredients', verbose_name='Ингредиенты')
    step = models.ManyToManyField('Steps', related_name='steps', verbose_name='Шаги приготовления')
    image = models.ManyToManyField('StepImages', related_name='images', verbose_name='Картинки к шагам')
    is_active = models.BooleanField(verbose_name='Активность')
    #cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')

    def __str__(self):
        return self.recipe_name

class Ingredients(models.Model):
    ingredient = models.TextField(verbose_name='Ингредиент')

    def __str__(self):
        return str(self.pk)


class StepImages(models.Model):
    image = models.ImageField(upload_to='step_images/',
                                       default=None, blank=True, null=True, verbose_name='Фотография к шагу')

    def __str__(self):
        return str(self.pk)

class Steps(models.Model):
    step = models.TextField(verbose_name='Шаг приготовления')

    def __str__(self):
        return str(self.pk)


# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True, verbose_name='Категория')
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')



