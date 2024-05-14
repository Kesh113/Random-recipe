from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .generate_recipe import get_recipe
from .models import RecipeModel


def index(request):
    data = {
            'name_button': 'Йеах, получить рандомный рец!',
            'head_title': 'Главная страница',
            'page_title': 'Страница получения ресайпа!!',
            }
    return render(request, 'recipes/index.html', data)

def generation_recipe(request):
    data = get_recipe()
    if not RecipeModel.objects.get(slug=data['slug']):
        random_recipe = RecipeModel.objects.create(**data)
    else:
        random_recipe = RecipeModel.objects.get(slug=data['slug'])
    url = reverse('recipe', kwargs={'recipe_slug': random_recipe.slug})
    return HttpResponseRedirect(url)

def recipe(request, recipe_slug):
    get_recipe = RecipeModel.objects.get(slug=recipe_slug)
    return render(request, 'recipes/recipe.html', {'data': get_recipe})

# class Recipe(ListView):
#     model = RecipeModel
#     template_name = 'recipes/recipe.html'
#     context_object_name = 'recipe'
#     data_dct = get_recipe()
#     if not RecipeModel.objects.filter(recipe_name=data_dct['recipe_name']):
#         data = RecipeModel(**data_dct)
#         data.save()
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(RecipeModel.objects)
