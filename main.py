import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

token = os.getenv("TOKEN")

headers = {
    
    'Authorization': f'Bearer {token}'

}

url = 'https://api-ssl.bitly.com/v4/user'

response = requests.get(url, headers=headers)
response.raise_for_status()


pprint(response.json())
#ответ в виде словарей или списков