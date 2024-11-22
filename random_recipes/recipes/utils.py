from random import choice
from django.http import HttpResponseServerError
import requests
import urllib.parse

from bs4 import BeautifulSoup as bs


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'
}

BASE_URL = 'https://www.russianfood.com'
SEARCH_URL = '/search/simple/index.php?'


# class RandomRecipe:

def get_encoded_text(text):
    return urllib.parse.quote(text, encoding="windows-1251")


def get_url_response(url):
    return requests.get(BASE_URL + url, headers=HEADERS)


def get_random_recipe_url(response):
    if response.status_code == 200:
        data = bs(response.text, "html.parser")
        recipe = choice(data.find_all('div', class_='in_seen'))
        tag_a = recipe.find('a')
        if tag_a:
            url_recipe = tag_a.get('href')
        else:
            raise KeyError('Ccылки на рецепт не найдено')
    else:
        return HttpResponseServerError
    return url_recipe


def get_recipe_data(category, tags):
    url_list_recipes = f'sskw_title={get_encoded_text(tags)}&tag_tree[1][]={category}'
    url_recipe = get_random_recipe_url(get_url_response(SEARCH_URL + url_list_recipes))
    response = bs(get_url_response(url_recipe).text, "html.parser")
    recipe_html = response.find('table', class_='recipe_new')
    title = recipe_html.find('h1').text
    image = 'https:' + recipe_html.find('a', class_='tozoom')['href']
    description = recipe_html.find('p').text
    ingredients = [ingredient.get_text(strip=True) for ingredient in recipe_html.find_all('tr', {'class': ['ingr_tr_0', 'ingr_tr_1']})]
    
    steps = soup.find_all('div', {'class': 'step_n'}) + soup.find_all('div', {'id': 'how'})
    
    return {
        'title': title,
        'image': image,
        'description': description,
        'ingredients': ingredients,
        'steps': steps
    }

    #     steps = soup.find_all('div', {'class': 'step_n'})
    #     + soup.find_all('div', {'id': 'how'})


    #     for p in steps:

    #         step = p.find('p').text.strip()

    #         image = p.find('img')
    #         image_url = 'https:' + image['src'] if image else ''
    #         if image_url:
    #             response = requests.get(image_url)

    #             if response.status_code == 200:
    #                 data['step_image'].append((image_url, step))

    # return


# def get_test_dict():
#     return {
#         'title': 'реце1',
#         'description': 'Описание',
#         'ingredients_title': ['Ингредиент1', 'Ингредиент1'],
#         'ingredients_count': ['15 гр', '500 мл'],
#         'step_description': ['Шаг1', 'Шаг2']
#     }


print(get_recipe_data(2, "курица"))
