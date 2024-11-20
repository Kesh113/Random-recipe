from django.contrib.sessions.models import Session
from django.db import models








class Recipe(models.Model):
    user = models.ForeignKey(Session, on_delete=models.CASCADE,
                             related_name='recipes')
    title = models.CharField('Название', max_length=120)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание')

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


class Ingredient(models.Model):
    title = models.CharField('Название', max_length=120)
    count = models.CharField('Количество', max_length=120)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='ingredients')


class Step(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='steps')

    def step_image_upload_to(self, filename):
        return f'recipes/{self.recipe.slug}/steps/{filename}'

    image = models.ImageField(
        upload_to=step_image_upload_to,
        default=None, blank=True, null=True, verbose_name="Фото")
