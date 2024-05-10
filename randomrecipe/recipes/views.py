from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from . import generate_recipe
from .models import RecipeModel


def main(request):
    data = {
            'name_button': 'Йеах, получить рандомный рец!',
            'head_title': 'Главная страница',
            'page_title': 'Страница получения ресайпа!!',
            }
    return render(request, 'recipes/main.html', data)

def recipe(request):
     recipe_model = RecipeModel.objects.get(pk=3)
     data = {
         'recipe': recipe_model
     }
     return render(request, 'recipes/recipe.html', data)

# class Recipe(ListView):
#     model = RecipeModel
#     template_name = 'recipes/recipe.html'
#     context_object_name = 'recipe'
#     data_dct = generate_recipe.get_recipe()
#     if not RecipeModel.objects.filter(recipe_name=data_dct['recipe_name']):
#         data = RecipeModel(**data_dct)
#         data.save()
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(RecipeModel.objects)