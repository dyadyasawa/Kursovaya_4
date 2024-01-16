
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
    def __init__(self, prof: str, area: str):
        self.prof = prof
        self.area = area

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий hh.ru. """

        # url_hh = "http://api.hh.ru/vacancies"
        # params = {'text': f'name:{self.prof}',
        #           'area': 1,
        #           'page': 0}
        #
        # response = requests.get(url_hh, params).json()
        response = requests.get(f"http://api.hh.ru/vacancies?text=!{self.prof} AND !{self.area}").json()
        with open('data/hh_vacancies.json', 'w', encoding=('UTF-8')) as file:
            json.dump(response, file, ensure_ascii=False, indent=4)

        with open('data/hh_vacancies.json', 'r', encoding=('UTF-8')) as file:
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
        print(f"Страница: {dfc['page']} из {dfc['pages']}")


class SuperJobApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта superjob.ru. """

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий superjob.ru."""
        pass
