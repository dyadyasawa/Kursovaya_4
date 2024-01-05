
import json
import requests
from pprint import pprint

head_hunter_url = 'http://api.hh.ru/vacancies?text=""'
#head_hunter_url = 'http://api.hh.ru/vacancies/7760476'

response = requests.get(url=head_hunter_url).json()

with open('data/hh_vacancies.json', 'w', encoding=('utf-8')) as file:
    json.dump(response, file, ensure_ascii=False, indent=4)


with open('data/hh_vacancies.json', 'r', encoding=('utf-8')) as file:
    dict_info = json.load(file)

pprint(dict_info)
#print(len(dict_info['items']))

def user_interaction():
    """ Функция для взаимодействия с пользователем """
    pass