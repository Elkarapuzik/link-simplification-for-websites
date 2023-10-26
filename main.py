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

print("1.Сократить ссылку")
print("2.Узнать количество кликов по сокращенной ссылке")

user_choice = int(input("Выбирите функцию: "))

if user_choice == 1:
    print("Тест сокращение ссылки")
if user_choice == 2:
    print("Тест получение количества кликов по сокращенной ссылке")