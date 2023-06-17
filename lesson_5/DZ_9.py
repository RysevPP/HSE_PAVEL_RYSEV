"""
дисциплина: "Наука данных для юристов"
домашнее задание № 9 по теме № 2 "Алгоритмы, структуры данных и абстракции"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""

import random
import time

# функция линейного поиска
def lines_find(one, two):
    result = []
    start = time.time()
    for i in one:
        for k in two:
            if i == k:
                result.append(i)
    end = time.time()
    print(f'Линейный поиск выполнен за {start-end}')
    print(f'В списке размером {len(two)} найдены следующие значения:'
          f'{result}')

# функция бинарного поиска
def binary_find(one, two):
    result = []
    start = time.time()
    for i in one:
        min_b = 0
        max_b = (len(two)-1)
        while min_b <= max_b:
            mid = (min_b + max_b) // 2
            if i < two[mid]:
                max_b = mid-1
            elif i > two[mid]:
                min_b = mid+1
            elif i == two[mid]:
                result.append(i)
                break
    end = time.time()
    print(f'Бинарный поиск выполнен за {start-end}')
    print(f'В списке размером {len(two)} найдены следующие значения:'
          f'{result}')

if __name__ == '__main__':
    one = [i * random.randint(1, 25000000) for i in range(1, 11)]  # массив из 10 случайных чисел int
    one = sorted(one)
    two = [i for i in range(10, 250000001, random.randint(3, 5))]  # массив, содержащий отсортированные числа
    # от 10 до 250 млн., со случайным шагом от 3 до 5

    lines_find(one, two)
    binary_find(one, two)





# a = lines_find(one, two)
# print(one)
# print(a)
# #
# b = binary_find(one, two)
# print(one)
# print(b)







