import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random

header = {'user-agent': user}

link = 'https://browser-info.ru/'

response = requests.get(link, headers=header).text

soup = BeautifulSoup(response, 'lxml')

block = soup.find('div', id='tool_padding')

#check JS
check_js = block.find('div', id='javascript_check')
result_js = check_js.find_all('span')[1].text

#check Flash
check_flash = block.find('div', id='flash_version')
status_flash = check_flash.find_all('span')[1].text

#check UserAgent
check_user = block.find('div', id='user_agent').text
ua_list = check_user.split(' ')
a = ua_list.pop(0)
user_agent = ' '.join(ua_list)

print({'JavaScript': result_js})
print({'Flash': status_flash})
print({'UserAgent': user_agent})
