
from src.classes import HeadHunterApi

if __name__ == '__main__':

    profession = input("Кем хош быть? >>>  ")
    area = input("А де? >>>  ")
    salary = int(input("Скока хош?(ну.., так, плюс-минус) >>>  "))

    p1 = HeadHunterApi(profession, area, salary)

    print(p1.choice_dict(p1.get_vacancies()))


    def user_interaction():
        """ Функция для взаимодействия с пользователем """
        pass
