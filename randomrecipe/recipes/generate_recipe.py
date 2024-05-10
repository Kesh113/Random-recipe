import os
import requests
from bs4 import BeautifulSoup


def get_recipe():
    url = 'https://www.russianfood.com/recipes/recipe.php?rid=121338'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # soup = BeautifulSoup(response.text, 'html.parser')
        # steps = soup.find_all('div', {'class': 'step_n'})
        # recipe_name = soup.find('h1', class_='title').text
        # recipe_feature = soup.find('td', class_='padding_l padding_r').find('p').text
        # recipe_ingredients = soup.find_all('tr', {'class': ['ingr_tr_0', 'ingr_tr_1']})

        data = {
            'recipe_name': 'recipe_name',
            'recipe_feature': 'recipe_feature',
            'recipe_ingredients': [],
            'steps_content': [],
            'images_content': [],
            'is_active': True
        }
        # for ingr in recipe_ingredients:
        #     data['recipe_ingredients'].append(ingr.text.strip())
        #
        # for i, p in enumerate(steps, 1):
        #
        #     data['steps_content'].append(p.find('p').text.strip())
        #
        #     image = p.find('img')
        #     image_url = 'https:' + image['src'] if image else ''
        #     if image_url:
        #         response = requests.get(image_url)
        #
        #         if response.status_code == 200:
        #             if 'step_images' not in os.listdir('./media'):
        #                 os.makedirs(f'media/step_images/{recipe_name}')
        #             file_name = f'media/step_images/{recipe_name}/step{i}.jpg'
        #             with open(file_name, 'wb') as img_file:
        #                 img_file.write(response.content)
        #
        #     data['images_content'].append(file_name)

        return data



if __name__ == '__main__':
    print(get_recipe())