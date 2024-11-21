from django.contrib.sessions.models import Session
from django.db.transaction import atomic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from .models import Category, Ingredient, Recipe, Step
from .utils import get_test_dict
from .forms import RecipeForm


# def index(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             # Получаем очищенные данные из формы
#             cleaned_data = form.cleaned_data
#     form = RecipeForm()
#     return render(request, 'recipes/index.html', {'form': form})


class Index(CreateView):
    form_class = RecipeForm
    template_name = 'recipes/index.html'

    def form_valid(self, form):
        recipe_data = get_test_dict()
        try:
            with atomic():
                self.object = Recipe.objects.create(
                    tags=form.cleaned_data['tags'],
                    category=form.cleaned_data['category'],
                    user=Session.objects.get(
                        pk=self.request.session.session_key),
                    title=recipe_data['title'],
                    slug=recipe_data['slug'],
                    description=recipe_data['description'],
                    )
                Ingredient.objects.bulk_create([
                    Ingredient(
                        title=title, count=count, recipe=self.object
                        ) for title, count in zip(
                            recipe_data['ingredients_title'],
                            recipe_data['ingredients_count'])
                    ])
                Step.objects.bulk_create([
                    Step(
                        description=description, recipe=self.object
                        ) for description in recipe_data['step_description']
                    ])
        except Exception:
            return HttpResponse('Ошибка при сохранении рецепта в БД')
        return redirect(reverse('recipes:detail',
                                kwargs={'recipe_slug': self.object.slug}))


class Detail(DetailView):
    model = Recipe
    slug_url_kwarg = 'recipe_slug'
    template_name = 'recipes/detail.html'
    context_object_name = 'recipe'
