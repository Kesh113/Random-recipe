from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView

from . import generate_recipe


def main(request):
    data = {'name': 'recipe',
            'name_url': 'Йеах, получить рандомный рец!',
            'head_title': 'Главная страница',
            'page_title': 'Страница получения ресайпа!!',
            }
    return render(request, 'recipes/main.html', data)

def recipe(request):
    return render(request, 'recipes/recipe.html', {'data': generate_recipe.get_recipe()})