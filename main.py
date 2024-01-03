
import json
import requests

head_hunter_url = 'http://api.hh.ru/vacancies?text="python"'

response = requests.get(url=head_hunter_url).json()

with open('data/hh_vacancies.json', 'w', encoding=('utf-8')) as file:
    json.dump(response, file, ensure_ascii=False, indent=4)
