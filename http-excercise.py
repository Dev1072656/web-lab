import requests
import time
from datetime import datetime

def show_html(response):
    text = response.text
    count = 0 
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (N,y)?')
            if (reply == 'n' or reply == 'N'):
                break

def putURL():
    print("\nProvide a URL:  ")
    URL = input()
    with requests.get(URL) as response:
        return response

def show_headers(response):
    for k,v in response.headers.items():
        print(f"name: {k} value: {v}")

def show_cookies(response) :
    cookies = response.cookies
    expires = None
    print("####Cookie List####")
    for cookie in cookies:
        try:
            expires = cookie.expires
            expires = datetime.fromtimestamp(expires)
            print(f"Name: {cookie.name}  expires  {expires}")
        except:
            print(f"Name: {cookie.name}")


def show_test(response):
    print(response.headers["Server"])

def choose():
    print("""
    Options avalailable:
        1: Show HTML
        2: Show Headers of HTTP response
        3: Show Cookies if available
        4: Show Server type
    """)
    print("Choose one number 1-4.")
    
    while True:
        n = input() 
        try:
            n = int(n)
        except ValueError:
            print("Your input should be an integer between 1-4.")
            continue   
        if n > 4 or n < 1:
            print("Choose a valid number.")
            continue
        else:
            break
    return n

        

response = putURL()

option = choose()

match option:
    case 1:
        show_html(response)
    case 2:
        show_headers(response)
    case 3:
        show_cookies(response)
    case 4:
        show_test(response)


