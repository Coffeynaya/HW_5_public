"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
'''
year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкина: ')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')
'''

def burn_date(q_1 = 1799, q_2 = 6):

    answer_1 = int(input('Ввведите год рождения А.С.Пушкина:'))
    while answer_1 != q_1:
        print('Не верно')
        answer_1 = int(input('Ввведите год рождения А.С.Пушкина:'))

    answer_2 = int(input('В какой день июня родился Пушкин?'))
    while answer_2 != q_2:
        print('Не верно')
        answer_2 = int(input('В какой день июня родился Пушкин?'))

    return 'Верно! Спасибо за игру!'



burn_date()