from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .generate_recipe import get_recipe
from .models import RecipeModel, Ingredients, Steps, StepImages


def index(request):
    data = {
            'name_button': 'Йеах, получить рандомный рец!',
            'head_title': 'Главная страница',
            'page_title': 'Страница получения ресайпа!!',
            }
    return render(request, 'recipes/index.html', data)


def generation_recipe(request):
    pass
#     data = get_recipe()
#     random_recipe, _ = RecipeModel.objects.get_or_create(defaults=data[0], recipe_name=data[0]['recipe_name'])
#     for ing in data[1]['ingredient']:
#         i = Ingredients.objects.create(ingredient=ing)
#         random_recipe.ingredient.set(Ingredients.objects.filter(id=i.id))
#     for st in data[2]['step']:
#         i = Steps.objects.create(step=st)
#         random_recipe.step.set(Steps.objects.filter(id=i.id))
#     for im in data[3]['image']:
#         i = StepImages.objects.create(image=im)
#         random_recipe.image.set(StepImages.objects.filter(id=i.id))
#     url = reverse('recipe', kwargs={'recipe_slug': random_recipe.slug })
#     return HttpResponsePermanentRedirect(url)

def recipe(request, recipe_slug):
    get_recipe = get_object_or_404(RecipeModel, slug=recipe_slug)
    ingredients = get_recipe.ingredient.all()
    images = get_recipe.image.all()
    steps = get_recipe.step.all()
    data = {
        'main_info': get_recipe,
        'images': images,
        'ingredients': ingredients,
        'steps': steps,
    }
    return render(request, 'recipes/recipe.html', data)


