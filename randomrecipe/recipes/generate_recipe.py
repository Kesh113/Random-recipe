import os
from time import sleep

import requests
from bs4 import BeautifulSoup


def get_recipe():
    url = 'https://www.russianfood.com/recipes/recipe.php?rid=121338'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        steps = soup.find_all('div', {'class': 'step_n'})
        steps_content = []
        images_content = []
        recipe_name = 'Курица на бутылке'
        for i, p in enumerate(steps, 1):

            steps_content.append(p.find('p').text.strip())

            image = p.find('img')
            image_url = image['src'] if image else ''

            if image_url:
                response = requests.get(f'https:{image_url}')

                if response.status_code == 200:
                    image_filename = os.path.join('dog_images', f'step{i}.jpg')

                    with open(image_filename, 'wb') as img_file:
                        img_file.write(response.content)

            images_content.append(image_filename)
        #'recipe_feature': soup.find('td', {'class': 'padding_l padding_r'}),
        #'ingridients': soup.find('table', {'class': 'ingr_block'}),
        #'steps': soup.find('div', {'class': 'step_images_n'}),
       # }
        return images_content



if __name__ == '__main__':
    print(get_recipe())