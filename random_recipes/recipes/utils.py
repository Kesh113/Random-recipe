from random import randrange

import requests
# from transliterate import slugify
from bs4 import BeautifulSoup


# def get_recipe(category, tags):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
#         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 \
#         Safari/537.36"
#     }
#     url = f'https://www.russianfood.com/search/simple/index.php?ssgrtype=bytype&sskw_title=&tag_tree%5B1%5D%5B%5D={category}&tag_tree%5B2%5D%5B%5D=0&sskw_iplus=&sskw_iminus=&submit=#beforesearchform'
#     + str(randrange(120000, 170000))

#     response = requests.get(url, headers)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         recipe_name = soup.find('h1', class_='title').text
#         slug = slugify(recipe_name)
#         recipe_feature = soup.find('td',
#                                    class_='padding_l padding_r').find('p').text
#         ingredients = soup.find_all('tr',
#                                     {'class': ['ingr_tr_0', 'ingr_tr_1']})
#         steps = soup.find_all('div', {'class': 'step_n'})
#         + soup.find_all('div', {'id': 'how'})

#         data = {
#             'recipe_name': recipe_name,
#             'slug': slug,
#             'recipe_feature': recipe_feature,
#             'ingredient': [],
#             'step_image': [],
#         }

#         for ingr in ingredients:
#             data['ingredient'].append(ingr.text.strip())

#         for p in steps:

#             step = p.find('p').text.strip()

#             image = p.find('img')
#             image_url = 'https:' + image['src'] if image else ''
#             if image_url:
#                 response = requests.get(image_url)

#                 if response.status_code == 200:
#                     data['step_image'].append((image_url, step))

#     print(url, data, steps)
#     return render_template('page.html', data=data)


# app.run(host='127.0.0.1', port=8000, debug=True)

def get_test_dict():
    return {
        'title': 'рецепт',
        'slug': 'slug3',
        'description': 'Описание',
        'ingredients_title': ['Ингредиент1', 'Ингредиент1'],
        'ingredients_count': ['15 гр', '500 мл'],
        'step_description': ['Шаг1', 'Шаг2']
    }