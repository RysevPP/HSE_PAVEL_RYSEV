"""
дисциплина: "Наука данных для юристов"
домашнее задание № 3 по теме № 1 "Введение в Python"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""

import lesson_2_data

"""
Функция shapka генерирует шапку для процессуальных документов с реквизитами сторон для отправки.
Функция принимает в качестве аргумента словарь с данными ответчика и номером дела, а возвращает 
готовую шапку в виде строки.
"""

def shapka(dict_sh):
    if "case_number" in dict_sh:
        sud_number = dict_sh["case_number"].split("-")[0]
        for item in lesson_2_data.courts:
            if sud_number == item['court_code']:
                sud = item['court_name']
                adress = item['court_address']
        print(f"""
        В {sud}
        Адрес: {adress}
        
        Истец: Рысев Павел Петрович
        ИНН: 123456789001
        Адрес: 121351, г. Москва, ул. Крамолы, д. 7, кв. 121
        
        Ответчик: {dict_sh['short_name']}
        ИНН: {dict_sh['inn']}, ОГРН: {dict_sh['ogrn']}
        Адрес: {dict_sh['address']}
        
        Дело № {dict_sh["case_number"]}
        """)

"""
Функция perebor принимает в себя список словарей с данными ответчика и генерирует все возможные варианты
этой шапки с вызовом функции shapka внутри тела и выводит данные в консоль.
"""

def perebor(dict_sh_1):
    for item in dict_sh_1:
        shapka(item)

perebor(lesson_2_data.repondents)
