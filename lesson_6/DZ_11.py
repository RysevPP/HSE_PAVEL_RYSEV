"""
дисциплина: "Наука данных для юристов"
домашнее задание № 11 по теме № 3 "Сетевое взаимодействие"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""

import requests
import json

class SirotinskyAPI:
    URL = 'https://api.sirotinsky.com'

    def __init__(self, log, pasw):
        self.URL = 'https://api.sirotinsky.com'
        self.__login = log
        self.__password = pasw
        self.__token = self.__post_token()

    def __post_token(self):
        response = requests.post(self.URL + '/token', data={'username': self.__login, 'password': self.__password})
        translation = json.loads(response.text)
        self.token = translation['access_token']

    def get_dostup(self):
        response=requests.get(self.URL)
        translation = json.loads(response.text)
        self.dostup = translation['message']
        print(self.dostup)

    def get_name(self, name):
        response=requests.get(self.URL+'/hello/'+name)
        translation = json.loads(response.text)
        self.name = translation['message']
        print(self.name)

    def get_INN_manager(self, INN):
        response = requests.get(self.URL+'/'+self.token+'/efrsb/manager/'+INN, data={'inn':INN, 'token':self.token})
        print(response.text)

    def get_INN_trader(self, INN):
        response = requests.get(self.URL+'/'+self.token+'/efrsb/trader/'+INN, data={'inn':INN, 'token':self.token})
        print(response.text)

    def get_INN_person(self, INN):
        response = requests.get(self.URL+'/'+self.token+'/efrsb/person/'+INN, data={'inn':INN, 'token':self.token})
        print(response.text)

    def get_INN_organisation(self, INN):
        response = requests.get(self.URL+'/'+self.token+'/efrsb/organisation/'+INN, data={'inn':INN, 'token':self.token})
        print(response.text)

    def get_INN_party(self, INN):
        response = requests.get(self.URL+'/'+self.token+'/dadata/party/'+INN, data={'inn':INN, 'token':self.token})
        translation = json.loads(response.text)
        self.party = translation['message']
        print(self.party)

#проверка - создание экземпляра класса и запуск всех методов
if __name__ == '__main__':
    a = SirotinskyAPI('HSE_student', '123123123')
    a.get_dostup()
    a.get_name('Павел')
    a.get_INN_manager('7723727274')
    a.get_INN_trader('7723727274')
    a.get_INN_person('7723727274')
    a.get_INN_organisation('7723727274')
    a.get_INN_party('7723727274')