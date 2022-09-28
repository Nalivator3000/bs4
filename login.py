import requests
import fake_useragent


session = requests.Session()

user_agent = fake_useragent.UserAgent().random

header = {
    'user_agent': user_agent
}

link = 'https://zastavok.net/auth.php'

data = {
    'username': 'Hippi4',
    'password': "3wmVi",
    'remember_me': 'on',
    'act': 'login'
}

response = requests.post(link, data=data, headers=header).text

profile_info = 'https://rutracker.org/forum/profile.php?mode=viewprofile&u=22698968'

profile_response = session.get(profile_info).text

cookie_dict = [
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookie_dict:
    session2.cookies.set(**cookies)

resp = session2.get(profile_info, headers=header)

print(resp.text)
