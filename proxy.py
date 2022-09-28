import requests

with open('proxy') as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')

for proxy in proxy_base:
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    link = 'http://icanhazip.com/'
    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f"IP: '{response}'")
    except:
        print('The proxy isn`t work')
