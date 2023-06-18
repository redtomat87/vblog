"""
Домашнее задание №1
Функции и структуры данных
"""

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def power_numbers(*numbers):
    return [number ** 2 for number in numbers]

print(f'список квадратов {power_numbers(*numbers)}')

"""
функция, которая принимает N целых чисел,
и возвращает список квадратов этих чисел
>>> power_numbers(1, 2, 5, 7)
<<< [1, 4, 25, 49]
"""


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

"""
функция, которая на вход принимает список из целых чисел,
и возвращает только чётные/нечётные/простые числа
(выбор производится передачей дополнительного аргумента)

>>> filter_numbers([1, 2, 3], ODD)
<<< [1, 3]
>>> filter_numbers([2, 3, 4, 5], EVEN)
<<< [2, 4]
"""


def odd(num):
    if(num % 2) == 0:
        return True
    else:
        return False

filtered_numbers = filter(odd, numbers)
print(list(filtered_numbers))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

filtered_numbers = filter(is_prime, numbers)
print(list(filtered_numbers))
def even(num):
    if(num % 2) != 0:
        return True
    else:
        return False


filtered_numbers = filter(even, numbers)
print(list(filtered_numbers))


def filter_numbers(numbers, filter_type):
    if filter_type == ODD:  # нечётные
        return [number for number in numbers if number == 1 or number % 2 != 0]
    if filter_type == EVEN:  # четные
        return [number for number in numbers if number % 2 == 0]
    if filter_type == PRIME:
        return [number for number in numbers if is_prime(number)]

print(ODD, filter_numbers(numbers, ODD))
print(EVEN, filter_numbers(numbers, EVEN))
print(PRIME, filter_numbers(numbers, PRIME))