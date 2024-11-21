# Generated by Django 5.1.3 on 2024-11-21 02:29

import django.db.models.deletion
import recipes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('description', models.TextField(verbose_name='Описание')),
                ('title_image', models.ImageField(blank=True, default=None, null=True, upload_to=recipes.models.Recipe.recipe_title_image_upload_to, verbose_name='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'default_related_name': 'recipes',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('count', models.CharField(max_length=120, verbose_name='Количество')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=recipes.models.Step.step_image_upload_to, verbose_name='Фото')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipes.recipe')),
            ],
        ),
    ]