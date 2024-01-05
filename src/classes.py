
from abc import ABC, abstractmethod


class WorkApi(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями. """

    @abstractmethod
    def get_vacancies(self):
        """ Абстрактный метод для подключения к API и получения вакансий. Реализуется в дочерних классах. """
        pass


class HeadHunterApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта hh.ru. """

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий hh.ru. """
        pass


class SuperJobApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта superjob.ru. """

    def get_vacancies(self):
        """ Метод для подключения к API и получения вакансий superjob.ru."""
        pass
