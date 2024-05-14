from django.db import models
from django.urls import reverse


class RecipeModel(models.Model):
    recipe_name = models.CharField(max_length=100, unique=True, verbose_name='Название рецепта')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    recipe_feature = models.TextField(verbose_name='Описание рецепта')
    recipe_ingredients = models.TextField(verbose_name='Список ингредиентов')
    steps_content = models.TextField(verbose_name='Пошаговая инструкция')
    images_content = models.TextField(verbose_name='Фотографии к шагам', blank=True, default=None, null=True)
    is_active = models.BooleanField(verbose_name='Активность')

    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('generation_recipe', kwargs={'recipe_slug': self.slug})