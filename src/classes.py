
import json
import requests
from abc import ABC, abstractmethod
from pprint import pprint


class WorkApi(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями. """

    @abstractmethod
    def get_vacancies(self):
        """ Абстрактный метод для подключения к API и получения вакансий. Реализуется в дочерних классах. """
        pass


class HeadHunterApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта hh.ru. """
    def __init__(self, prof):
        self.prof = prof

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий hh.ru. """

        response = requests.get(url=f'http://api.hh.ru/vacancies?text="{self.prof}"').json()

        with open('../data/hh_vacancies.json', 'w', encoding=('UTF-8')) as file:
            json.dump(response, file, ensure_ascii=False, indent=4)

        with open('../data/hh_vacancies.json', 'r', encoding=('UTF-8')) as file:
            dict_info = json.load(file)

        return dict_info

    @staticmethod
    def choice_dict(dict_for_choice):

        dfc = dict_for_choice

        print(f"Профессия: {dfc['items'][0]['name']}")
        print(f"Зарплата: {dfc['items'][0]['salary']['from']}")
        print(f"Валюта: {dfc['items'][0]['salary']['currency']}")
        print(f"Место: {dfc['items'][0]['area']['name']}")
        print(f"Занятость: {dfc['items'][0]['schedule']['name']}")
        print(f"Условия: {dfc['items'][0]['snippet']['responsibility']}")


class SuperJobApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта superjob.ru. """

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий superjob.ru."""
        pass

profession = input("По какой профессии вывести вакансии? >>>  ")
p1 = HeadHunterApi(profession)
print(p1.choice_dict(p1.get_vacancies()))
