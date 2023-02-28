import requests
session = requests.Session()
print(session.cookies.get_dict())
response = session.get('https://www.youtube.com')
print(session.cookies.get_dict())