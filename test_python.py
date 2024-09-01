'''
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше



'''

# Пример использования функции filter
friends = ['Alice', 'Bob', 'Charlie', 'Megan', 'Mark', 'Michael']
filtered_friends = list(filter(lambda x: x.startswith('M'), friends)) # Используем filter с лямбда-функцией для выбора имен, начинающихся с "M"
print(filtered_friends)
def test_filter():
    assert list(filter(lambda x: x.startswith('M'), friends)) == ['Megan', 'Mark', 'Michael']

# Пример использования функции map
strings = ['apple', 'banana', 'cherry'] # Создаем список строк
def capitalize_string(s): # Определяем функцию, которая преобразует строку, чтобы она начиналась с заглавной буквы
    return s.capitalize()
capitalized_strings = list(map(capitalize_string, strings)) # Применяем функцию capitalize_string к каждой строке в списке strings с помощью map
print(capitalized_strings)
def test_map():
    assert list(map(capitalize_string, strings)) == ['Apple', 'Banana', 'Cherry']

# Пример использования функции sorted
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
def test_sorted():
    assert sorted(numbers) == [1, 2, 3, 5, 8]

# Пример использования функции pi
from math import pi
print("Значение числа Pi:", pi)
def test_pi():
    assert pi == 3.141592653589793

# Пример использования функции sqrt
number = 16 # Вычисление квадратного корня числа 16
square_root = math.sqrt(number)
print("Квадратный корень числа", number, "равен", square_root)
def test_square():
    assert math.sqrt(16) == 4

# Пример использования функции pow
result = pow(2, 3) # Возводим число 2 в степень 3
print(result)  # Выведет: 8
def test_pow():
    assert pow(2, 3) == 8

# Пример использования функции hypot
katet1 = 3 # Задаем длины катетов
katet2 = 4
hypotenuse = math.hypot(katet1, katet2) # Вычисляем гипотенузу с помощью функции hypot
print(hypotenuse) # Выводим результат
def test_hypot():
    assert math.hypot(3, 4) == 5
