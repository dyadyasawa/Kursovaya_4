
from src.classes import HeadHunterApi

if __name__ == '__main__':

    profession = input("По какой профессии вывести вакансии? >>>  ")
    p1 = HeadHunterApi(profession)
    print(p1.choice_dict(p1.get_vacancies()))
    def user_interaction():
        """ Функция для взаимодействия с пользователем """
        pass