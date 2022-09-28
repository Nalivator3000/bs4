import requests


link = 'https://browser-info.ru/'
response = requests.get(link).text

with open('site.html', 'w', encoding='utf-8') as file:
    file.write(response)