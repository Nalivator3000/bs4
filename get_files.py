import requests
from .login import *
from bs4 import BeautifulSoup




image_number = 0
storage_number = 1
link = f'https://zastavok.net'

for storage in range(1):
    response = requests.get(f'{link}/{storage_number}').text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', class_='block-photo')
    all_images = block.find_all('div', class_='short_full')

    for image in all_images:
        image_link = image.find('a').get('href')
        download_storage = requests.get(f'{link}/{image_link}').text
        download_soup = BeautifulSoup(download_storage, 'lxml')
        download_block = download_soup.find('div', class_='image_data').find('div', class_='block_down')
        result_link = download_block.find('a').get('href')

        h1_name = download_soup.find('div', class_='wall_page-speedbar').find('h1')
        image_name = h1_name.string
        image_name = image_name[1:-1]

        image_bytes = requests.get(f'{link}{result_link}').content

        with open(f'images/{image_name}.jpg', 'wb') as file:
            file.write(image_bytes)

        print(f'{image_name}.jpg Image successfully downloaded')

    storage_number += 1

#print(all_images[0])

