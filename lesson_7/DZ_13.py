"""
дисциплина: "Наука данных для юристов"
домашнее задание № 13 по теме № 3 "Сетевое взаимодействие"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221

Программа забирает c сайта Банка России, из таблицы по адресу:https://cbr.ru/banking_sector/credit/FullCoList/,
список кредитных организаций, зарегистрированных на территории России по состоянию на дату сбора
"""

import requests
from bs4 import BeautifulSoup
import json

class ParserCBRF:

    def __init__(self):
        self.URL = 'https://cbr.ru/banking_sector/credit/FullCoList/'
        self.baza={}

    def __parser(self):
        r = requests.get(self.URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', class_='data levels')
        headers=[]
        for i in table.find_all('th'):
            title = i.text
            headers.append(title)
        for j in table.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text.replace('\xa0', ' ') for i in row_data]
            self.baza[row[3]] = {headers[4]:row[4], headers[5]:row[5], headers[8]:row[8], headers[6]:row[6], headers[2]:row[2],
                                 headers[7]:row[7].replace('\n', 'Действует').replace('ОТЗ', 'Отозвана').replace('АНН', 'Аннулирована')}
        return (self.baza)

    def __file(self):
        with open("credit_organizations.json", "w") as f:
            json.dump(self.baza, f)

    def start(self):
        self.__parser()
        self.__file()

if __name__ == '__main__':
    a = ParserCBRF()
    a.start()