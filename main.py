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


print("1.Shorten link")
print("2.Find the number of clicks on the shortened link")

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
                           ╰─>{response.json()['link']}""",'green')

if user_choice == 2:
    print("Test getting number of clicks on shortened link")
if user_choice > 2:
    print('You have to choose 1 or 2')
    exit()

