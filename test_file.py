
import requests
import json


params = {'text': 'name:токарь',
          'area': 1,
          'page': 0}
response = requests.get('http://api.hh.ru/vacancies', params).json()


with open('data/hh_vacancies.json', 'w', encoding=('UTF-8')) as file:
    json.dump(response, file, ensure_ascii=False, indent=4)
#
with open('data/hh_vacancies.json', 'r', encoding=('UTF-8')) as file:
    dict_info = json.load(file)
#
print(dict_info)
