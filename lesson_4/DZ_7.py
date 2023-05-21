"""
дисциплина: "Наука данных для юристов"
домашнее задание № 7 по теме № 2 "Алгоритмы, структуры данных и абстракции"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""

import datetime

class CourtCase:

    def __init__(self, delo):
        self.case_number = delo
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ''
        self.resolution = ''

    def set_a_listening_datetime(self):
        date_time_str = input("Введите дату и время судебного заседания в формате ГГГГ-ММ-ДД ЧЧ:ММ: ")
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        self.listening_datetimes.append(date_time_obj)

    def add_participant (self, INN):
        self.case_participants.append(INN)

    def remove_participant (self, INN):
        self.case_participants.remove(INN)

    def make_a_decision (self):
        print('''
        Выбере какое решение было вынесено по делу:
        1 - иск удовлетворён в полном объёме
        2 - иск удовлетворён частично
        3 - в иске отказано
        4 - иск оставлен без рассмотрения
        5 - производство прекращено
        ''')
        a = int(input('Вводите: '))
        if a == 1:
            self.verdict = 'иск удовлетворён в полном объёме'
            print('''
            Желаете внести резолютивную часть решения?
            1 - да
            2 - нет
            ''')
            b = int(input ('Вводите: '))
            if b == 1:
                self.resolution = input ('Вводите: ')
        elif a == 2:
            self.verdict = 'иск удовлетворён частично'
            print('''
            Желаете внести резолютивную часть решения?
            1 - да
            2 - нет
            ''')
            b = int(input('Вводите: '))
            if b == 1:
                self.resolution = input('Вводите: ')
        self.is_finished = True




    

