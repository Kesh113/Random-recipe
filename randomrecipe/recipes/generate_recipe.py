import os


import requests
from bs4 import BeautifulSoup
from transliterate import slugify


def random_num():
    pass

def get_recipe():
    url = 'https://www.russianfood.com/recipes/recipe.php?rid=120338'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        recipe_name = soup.find('h1', class_='title').text
        slug = slugify(recipe_name)
        recipe_feature = soup.find('td', class_='padding_l padding_r').find('p').text
        ingredients = soup.find_all('tr', {'class': ['ingr_tr_0', 'ingr_tr_1']})
        steps = soup.find_all('div', {'class': 'step_n'})

        data = [{
            'recipe_name': recipe_name,
            'slug': slug,
            'recipe_feature': recipe_feature,
            'is_active': True
        },
            {'ingredient': []},
            {'step': []},
            {'image': []},
        ]
        for ingr in ingredients:
            data[1]['ingredient'].append(ingr.text.strip())

        for i, p in enumerate(steps, 1):

            data[2]['step'].append(p.find('p').text.strip())

            image = p.find('img')
            image_url = 'https:' + image['src'] if image else ''
            if image_url:
                response = requests.get(image_url)

                if response.status_code == 200:
                    if slug not in os.listdir('media/step_images'):
                        os.makedirs(f'media/step_images/{slug}')
                    file_name = f'media/step_images/{slug}/step{i}.jpg'
                    with open(file_name, 'wb') as img_file:
                        img_file.write(response.content)

            data[3]['image'].append(file_name)

        return data


if __name__ == '__main__':
    print(get_recipe())
