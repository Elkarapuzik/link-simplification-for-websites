import requests
import os
from termcolor import cprint
from dotenv import load_dotenv
from pprint import pprint
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

    user_choice = int(input("Select the function: "))


    if user_choice == 1:
        user_url = input("enter your link-> ")
        abbreviated_reference = {
            "long_url" : user_url,
        }

        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=abbreviated_reference)
        response.raise_for_status()

        
        
        cprint(f"""
Your abbreviated reference ×
                           │
                           ╰─> {response.json()['link']}\n""",'green')

    if user_choice == 2:
        user_abbreviated_url = input("write your abbreviated reference -> ")
        abbreviated_params = {
            "unit" : "month",
            "units"  : "-1"
        }

        response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{user_abbreviated_url}/clicks/summary', headers=headers, params=abbreviated_params)
        response.raise_for_status()

        cprint(f"""
click-through rate  ×
                    ╰─> {response.json()['total_clicks']}\n""",'green')

    if user_choice == 3:
        print("\n")
        exit()
            

    if user_choice > 3:
        print("""You have to choose 1/2/3/\n""")


