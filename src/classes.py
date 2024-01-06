
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

    head_hunter_url = 'http://api.hh.ru/vacancies?text="Профессия"'



    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий hh.ru. """

        response = requests.get(url=HeadHunterApi.head_hunter_url).json()

        with open('data/hh_vacancies.json', 'w', encoding=('utf-8')) as file:
            json.dump(response, file, ensure_ascii=False, indent=4)

        # with open('data/hh_vacancies.json', 'r', encoding=('utf-8')) as file:
        #     dict_info = json.load(file)
        #
        # pprint(dict_info)
        # print(len(dict_info['items']))


class SuperJobApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта superjob.ru. """

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий superjob.ru."""
        pass
