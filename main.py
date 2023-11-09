import os
from pprint import pprint
from time import sleep
#_________________________
from urllib.parse import urlparse
import requests
from termcolor import cprint
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

headers = {
    
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'

}

url = 'https://api-ssl.bitly.com/v4/user'

response = requests.get(url, headers=headers)
response.raise_for_status()

while True:
    print("1.Shorten link")
    print("2.Find the number of clicks on the shortened link")
    print("3.Exit")

    try:
        user_choice = int(input("Select the function: "))
    except ValueError:
        cprint("You have to choose 1/2/3\n", 'red')  
        continue

    if user_choice == 1:
        user_url = input("enter your link-> ")
        shorten_link = {
            "long_url" : user_url,
        }

        try:
            response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=shorten_link)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            cprint(f"Incorrect link -> {user_url}\n", 'red')
            continue
        
        cprint(f"""
Your shorten link ×
                      │
                      ╰─> {response.json()['link']}\n""", 'green')

    elif user_choice == 2:
        user_shorten_url = input("write your shorten link -> ")
        splited_shorten_user_url = urlparse(user_shorten_url)
        nohttps_user_shorten_url = splited_shorten_user_url.netloc + splited_shorten_user_url.path
        params = {
            "unit" : "month",
            "units"  : "-1"
        }

        try:
            response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{nohttps_user_shorten_url}/clicks/summary', headers=headers, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            cprint(f"Incorrect shortened link -> {nohttps_user_shorten_url}\n", 'red')
            continue

        cprint(f"""
click-through rate  ×
                    ╰─> {response.json()['total_clicks']}\n""",'green')

    elif user_choice == 3:
        cprint("You closed the proggram\n", 'magenta')
        exit()
            

    else:
        cprint("You have to choose 1/2/3\n", 'red')
        sleep(1)


