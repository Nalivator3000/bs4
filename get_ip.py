import requests


link = 'https://icanhazip.com/'
response = requests.get(link).text
print(response)