"""
дисциплина: "Наука данных для юристов"
домашнее задание № 5 по теме № 1 "Введение в Python"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""

import json
import re
import csv

def text_mail(stroka):
    email = re.compile(r'\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[0-9a-zA-Z]+\b')
    spisok = list(re.findall(email, stroka))
    return (spisok)


with open('1000_efrsb_messages.json', 'r') as f:
    slovar = {}
    data = json.load(f)
    for item in data:
        mail = text_mail(item['msg_text'])
        if item['publisher_inn'] not in slovar:
            slovar[item['publisher_inn']]=list(set(mail))
        else:
            slovar[item['publisher_inn']]=list(set(slovar[item['publisher_inn']]+mail))

print(slovar)

with open("email.json", "w") as f_1:
    json.dump(slovar, f_1, indent=3, sort_keys=True)
    print(json.dumps(slovar, indent=3, sort_keys=True))

