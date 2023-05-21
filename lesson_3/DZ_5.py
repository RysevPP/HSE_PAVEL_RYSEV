"""
дисциплина: "Наука данных для юристов"
домашнее задание № 5 по теме № 1 "Введение в Python"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""

import json
import csv

with open('traders.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    #print(lines)

with open('traders.json', 'r') as f1:
    data = json.load(f1)
    #print(data)

spisok = []
for inn in lines:
    for item in data:
        if inn == item['inn']:
            spisok.append({'inn':item['inn'], 'ogrn':item['ogrn'], 'address':item['address']})

fields = ['inn', 'ogrn', 'address']

with open ('traders.csv', 'w') as f2:
    writer = csv.DictWriter(f2, fieldnames=fields, delimiter = "|")
    writer.writeheader()
    writer.writerows(spisok)

