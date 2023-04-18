"""
дисциплина: "Наука данных для юристов"
домашнее задание № 4 по теме № 1 "Введение в Python"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""
#функция проверки ИНН юридического лица
def inn_ul(inn_ulc):
    vesa = [2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
    kontr_sum=0
    for i in range(0, 10):
        kontr_sum = kontr_sum + (int(inn_ulc[i])*vesa[i])
    kontr_chislo = kontr_sum % 11
    if kontr_chislo > 9:
        kontr_chislo = kontr_chislo % 10
    if kontr_chislo == int(inn_ulc[9]):
        print(f"Введённый ИНН: {inn_ulc} действителен!")
    else:
        print(f"Введённый ИНН: {inn_ulc} недействителен!")

#функция проверки ИНН физического лица
def inn_fl(inn_flc):
    vesa_1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    vesa_2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    kontr_sum_1 = 0
    kontr_sum_2 = 0

    for i in range(0, 10):
        kontr_sum_1 = kontr_sum_1 + (int(inn_flc[i])*vesa_1[i])
    kontr_chislo_1 = kontr_sum_1 % 11
    if kontr_chislo_1 > 9:
        kontr_chislo_1 = kontr_chislo_1 % 10

    for i in range(0, 11):
        kontr_sum_2 = kontr_sum_2 + (int(inn_flc[i]) * vesa_2[i])
    kontr_chislo_2 = kontr_sum_2 % 11
    if kontr_chislo_2 > 9:
        kontr_chislo_2 = kontr_chislo_2 % 10

    if (kontr_chislo_1 == int(inn_flc[10])) and (kontr_chislo_2 == int(inn_flc[11])):
        print(f"Введённый ИНН: {inn_flc} действителен!")
    else:
        print(f"Введённый ИНН: {inn_flc} недействителен!")

a = input('Введите ИНН юридического или физического лица для проверки (10 и 12 цифр соответственно): ')
if len(a) == 10:
    inn_ul(a)
else:
    inn_fl(a)
# проверка работы
#inn_ul("5408117935")
#inn_ul("0300000000")
#inn_fl("301505176790")
#inn_fl("301505176713")


