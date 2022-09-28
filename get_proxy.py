from bs4 import BeautifulSoup
import requests
import fake_useragent


session = requests.Session()

user_agent = fake_useragent.UserAgent().random

header = {
    'user_agent': user_agent
}

link = 'https://hidemy.name/ru/proxy-list/'

cookie_dict = [
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookie_dict:
    session2.cookies.set(**cookies)

# for i in range(50):
response = session2.get(link, headers=header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', class_='table_block')

print(response)