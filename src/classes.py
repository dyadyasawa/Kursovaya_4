
from abc import ABC, abstractmethod


class WorkApi(ABC):
    """  """

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterApi(WorkApi):
    """  """

    def get_vacancies(self):
        pass


class SuperJobApi(WorkApi):
    """  """

    def get_vacancies(self):
        pass
