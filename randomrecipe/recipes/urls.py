from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('recipe/', views.generation_recipe, name='generation_recipe'),
    #path('recipe/<slug:recipe_slug>/', views.recipe, name='recipe'),
]