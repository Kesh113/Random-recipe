from django.urls import path
from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('recipe/<slug:recipe_slug>', views.Detail.as_view(), name='detail'),
]