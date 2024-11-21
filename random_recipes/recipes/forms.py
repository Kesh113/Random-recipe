from django import forms

from .models import Recipe, Category


class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(
           queryset=Category.objects.all(),
           label=('Типы блюд'),
           empty_label=('Все')
       )

    class Meta:
        model = Recipe
        fields = 'tags',
        labels = {
            'tags': 'Слова в названии рецепта',
        }
