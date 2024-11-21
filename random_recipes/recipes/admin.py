from django.contrib import admin

from .models import Category, Ingredient, Recipe, Step

admin.site.register([Category, Recipe, Step, Ingredient])