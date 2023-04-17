"""
дисциплина: "Наука данных для юристов"
домашнее задание № 4 по теме № 1 "Введение в Python"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""

def inn_ul(inn_ulc):
    vesa = [2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
    kontr_sum=0
    for i in range(0, 10):
        kontr_sum = kontr_sum + (int(inn_ulc[i])*vesa[i])
    kontr_chislo = kontr_sum % 11
    if kontr_chislo > 9:
        kontr_chislo = kontr_chislo % 10
    if kontr_chislo == int(inn_ulc[9]):
        print(f"Введённое ИНН: {inn_ulc} действвительно, то есть существует")
    else:
        print(f"Введённое ИНН: {inn_ulc} недействвительно, то есть не существует")

inn_ul("5408117935")

inn_ul("0300000000")