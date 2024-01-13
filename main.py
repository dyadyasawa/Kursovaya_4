
from src.classes import HeadHunterApi

if __name__ == '__main__':

    profession = input("По какой профессии вывести вакансии? >>>  ")
    area = int(input("В каком регионе? >>>  "))
    p1 = HeadHunterApi(profession, area)

    #print(p1.get_vacancies())
    print(p1.choice_dict(p1.get_vacancies()))


    def user_interaction():
        """ Функция для взаимодействия с пользователем """
        pass