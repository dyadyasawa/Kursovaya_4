
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
    def __init__(self, prof: str, area: int):
        self.prof = prof
        self.area = area

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий hh.ru. """

        response = requests.get(f"http://api.hh.ru/vacancies?text=name:!{self.prof} AND !{self.area}").json()

        with open('data/hh_vacancies.json', 'w', encoding=('UTF-8')) as file:
            json.dump(response, file, ensure_ascii=False, indent=4)

        with open('data/hh_vacancies.json', 'r', encoding=('UTF-8')) as file:
            dict_info = json.load(file)

        pages = int(dict_info['pages'])

        for page in range(pages +1):
            response = requests.get(f"http://api.hh.ru/vacancies?text=name:!{self.prof} AND !{self.area}&page={page}").json()

            with open('data/hh_vacancies.json', 'w', encoding=('UTF-8')) as file:
                json.dump(response, file, ensure_ascii=False, indent=4)

            with open('data/hh_vacancies.json', 'r', encoding=('UTF-8')) as file:
                dict_info = json.load(file)

            for item in range(len(dict_info['items'])):
                if dict_info['items'][item]['name'] == None:
                    print(f"Профессия: Значение не указано")
                else:
                    print(f"Профессия: {dict_info['items'][item]['name']}")

                if dict_info['items'][item]['salary'] == None:
                    print(f"Зарплата: Значение не указано")
                elif dict_info['items'][item]['salary']['from'] == None:
                    print(f"Зарплата: Значение не указано")
                else:
                    print(f"Зарплата: {dict_info['items'][item]['salary']['from']}")

                if dict_info['items'][item]['salary'] == None:
                    print(f"Валюта: Значение не указано")
                elif dict_info['items'][item]['salary']['currency'] == None:
                    print(f"Валюта: Значение не указано")
                else:
                    print(f"Валюта: {dict_info['items'][item]['salary']['currency']}")
                print()





    # @staticmethod
    # def choice_dict(dict_for_choice):
    #
    #     dfc = dict_for_choice
    #
    #     print(f"Профессия: {dfc['items'][0]['name']}")
    #     print(f"Зарплата: {dfc['items'][0]['salary']['from']}")
    #     print(f"Валюта: {dfc['items'][0]['salary']['currency']}")
    #     print(f"Место: {dfc['items'][0]['area']['name']}")
    #     print(f"Занятость: {dfc['items'][0]['schedule']['name']}")
    #     print(f"Условия: {dfc['items'][0]['snippet']['responsibility']}")
    #     print(f"Страница: {dfc['page']} из {dfc['pages']}")


class SuperJobApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта superjob.ru. """

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий superjob.ru."""
        pass


# p1 = HeadHunterApi('токарь', 1)
#
# print(p1.get_vacancies())
