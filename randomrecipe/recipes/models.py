from django.db import models
from django.urls import reverse


class RecipeModel(models.Model):
    recipe_name = models.CharField(max_length=100, unique=True, verbose_name='Название рецепта')
    recipe_feature = models.TextField(verbose_name='Описание рецепта')
    recipe_ingredients = models.TextField(verbose_name='Список ингредиентов')
    steps_content = models.TextField(verbose_name='Пошаговая инструкция')
    images_content = models.TextField(verbose_name='Фотографии к шагам', blank=True, default=None, null=True)
    is_active = models.BooleanField(verbose_name='Активность')

    def __str__(self):
        return self.recipe_name

