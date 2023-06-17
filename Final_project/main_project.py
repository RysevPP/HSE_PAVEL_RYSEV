"""
дисциплина: "Наука данных для юристов"
"Итоговый проект"

студент: Павел Петрович Рысев
группа ВШЭ|Нетология МЛТ221
"""


import pprint

from parser import ParserCBRF
from name_sort import NameSort
from date_registration_sort import CurrentSort, EarlierSort, LaterSort, IntervalSort
from number_registration_sort import RegNumSort
from status_license_sort import StatusLicenseSort
from adress_sort import AdressSort

def menu():
    print(
            '''
            Вы хотите:
            1 - найти кредитную(ые) организацию(и) по наименованию
            2 - найти кредитную(ые) организацию(и) по дате регистрации
            3 - найти кредитную(ые) организации(и) по регистрационному номеру
            4 - найти кредитную(ые) организации(и) по адресу
            5 - отфильтровать кредитные организации по периодам регистрации
            6 - отфильтровать кредитные организации по статусу лицензии
            7 - выйти из программы
        ''')

    i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())

    if i_menu == 1:
        name = input('\n\t\t\tВведите комбинацию букв, цифр и символов, которая может быть\n'
                     '\t\t\tв наименовании кредитной организации: ').strip()
        b = NameSort(name)
        c = b.start()
        pprint.pprint(c, sort_dicts=False)
        print(
            '''
            Результаты поиска сохранены в файл по адресу "parsed_data/name_credit_organizations.json",
            а также выведенны выше в консоль
            ''')
        print(
            '''
            Вы хотите:
            1 - запустить программу заново
            2 - выйти из программы
            ''')
        i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())
        if i_menu == 1:
            menu()
        else:
            print('\n\t\t\tВсего доброго!')

    elif i_menu == 2:
        date = input('\n\t\t\tВведите дату регистрации кредитной организации в формате "ДД.ММ.ГГГГ": ').strip()
        b = CurrentSort(date)
        c = b.start()
        pprint.pprint(c, sort_dicts=False)
        print(
            '''
            Результаты поиска сохранены в файл по адресу "parsed_data/current_credit_organizations.json",
            а также выведенны выше в консоль
            ''')
        print(
            '''
            Вы хотите:
            1 - запустить программу заново
            2 - выйти из программы
            ''')
        i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())
        if i_menu == 1:
            menu()
        else:
            print('\n\t\t\tВсего доброго!')

    elif i_menu == 3:
        regnum = input('\n\t\t\tВведите точный регистрационный номер или комбинацию букв, цифр и символов,\n'
                       'которая может быть в регистрационном номере кредитной организации: ').strip()
        b = RegNumSort(regnum)
        c = b.start()
        pprint.pprint(c, sort_dicts=False)
        print(
            '''
            Результаты поиска сохранены в файл по адресу "parsed_data/regnum_credit_organizations.json",
            а также выведенны выше в консоль
            ''')
        print(
            '''
            Вы хотите:
            1 - запустить программу заново
            2 - выйти из программы
            ''')
        i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())
        if i_menu == 1:
            menu()
        else:
            print('\n\t\t\tВсего доброго!')

    elif i_menu == 4:
        adress = input('\nВведите номер дома, название улицы, города или субъекта,\n'
                       'которые могут содержаться в адресе быть кредитной организации\n'
                       '(например: Маршала Жукова, Москва, Краснодарский и т.д.): ').strip()
        b = AdressSort(adress)
        c = b.start()
        pprint.pprint(c, sort_dicts=False)
        print(
            '''
            Результаты поиска сохранены в файл по адресу "parsed_data/adress_credit_organizations.json",
            а также выведенны выше в консоль
            ''')
        print(
            '''
            Вы хотите:
            1 - запустить программу заново
            2 - выйти из программы
            ''')
        i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())
        if i_menu == 1:
            menu()
        else:
            print('\n\t\t\tВсего доброго!')

    elif i_menu == 5:
        print(
            '''
            Вы хотите:
            1 - произвести поиск кредитных организаций, зарегистрированных ранее определённой даты
            2 - произвести поиск кредитных организаций, зарегистрированных позже определённой даты
            3 - произвести поиск кредитных организаций, зарегистрированных в период между двумя датами
            ''')

        j_menu = int(input('Введите соответствующий номер: ').strip())

        if j_menu == 1:
            date = input('\n\t\t\tВведите дату в формате "ДД.ММ.ГГГГ" (будет произведён поиск кредитных организаций,\n'
                         'зарегистрированных ранее указанной даты): ').strip()
            b = EarlierSort(date)
            c = b.start()
            pprint.pprint(c, sort_dicts=False)
            print(
            '''
            Результаты поиска сохранены в файл по адресу "parsed_data/earlier_credit_organizations.json",
            а также выведенны выше в консоль
            ''')
            print(
            '''
            Вы хотите:
            1 - запустить программу заново
            2 - выйти из программы
            ''')
            i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())
            if i_menu == 1:
                menu()
            else:
                print('\n\t\t\tВсего доброго!')

        elif j_menu == 2:
            date = input('\n\t\t\tВведите дату в формате "ДД.ММ.ГГГГ" (будет произведён поиск кредитных организаций,\n'
                         'зарегистрированных позже указанной даты): ').strip()
            b = LaterSort(date)
            c = b.start()
            pprint.pprint(c, sort_dicts=False)
            print(
            '''
            Результаты поиска сохранены в файл по адресу "parsed_data/earlier_credit_organizations.json",
            а также выведенны выше в консоль
            ''')
            print(
            '''
            Вы хотите:
            1 - запустить программу заново
            2 - выйти из программы
            ''')
            i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())
            if i_menu == 1:
                menu()
            else:
                print('\n\t\t\tВсего доброго!')

        elif j_menu == 3:
            date_low = input('\n\t\t\tВведите дату начала периода поиска в формате "ДД.ММ.ГГГГ": ').strip()
            date_up = input('\n\t\t\tВведите дату окончания периода поиска в формате "ДД.ММ.ГГГГ": ').strip()
            b = IntervalSort(date_low, date_up)
            c = b.start()
            pprint.pprint(c, sort_dicts=False)
            print(
            '''
            Результаты поиска сохранены в файл по адресу "parsed_data/interval_credit_organizations.json",
            а также выведенны выше в консоль
            ''')
            print(
            '''
            Вы хотите:
            1 - запустить программу заново
            2 - выйти из программы
            ''')
            i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())
            if i_menu == 1:
                menu()
            else:
                print('\n\t\t\tВсего доброго!')

    elif i_menu == 6:
        print(
            '''
            Вы хотите:
            1 - произвести поиск кредитных организаций со статусом лицензии "Действует"
            2 - произвести поиск кредитных организаций со статусом лицензии "Отозвана"
            3 - произвести поиск кредитных организаций со статусом лицензии "Аннулирована"
            4 - произвести поиск кредитных организаций со статусом лицензии "Не получена"
            ''')

        j_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())

        if j_menu == 1:
            k = 'Действует'
        elif j_menu == 2:
            k = 'Отозвана'
        elif j_menu == 3:
            k = 'Аннулирована'
        elif j_menu == 4:
            k = 'Не получена'

        b = StatusLicenseSort(k)
        c = b.start()
        pprint.pprint(c, sort_dicts=False)
        print(
            '''
            Результаты поиска сохранены в файл по адресу "parsed_data/status_credit_organizations.json",
            а также выведенны выше в консоль
            ''')
        print(
            '''
            Вы хотите:
            1 - запустить программу заново
            2 - выйти из программы
            ''')
        i_menu = int(input('\t\t\tВведите соответствующий номер: ').strip())
        if i_menu == 1:
            menu()
        else:
            print('\n\t\t\tВсего доброго!')

    else:
        print('\nВсего доброго!')


if __name__ == '__main__':
    print(
            '''
            Добро пожаловать в программу "ParserCBRF, v.1.0"!
            Программа собирает с сайта Банка России сведения о всех
            кредитных организациях, зарегистрированных на территории России
            в период с 06.03.1990 по дату запуска программы.
        
            Программа позволяет искать кредитные организации по наименованию, дате регистрации, 
            регистрационному номеру и адресу, а также позволяет фильтровать кредитные организации
            по периоду регистрации и статусу лицензии.
        
            Сведения уже скачены и сохранены в файл по адресу "parsed_data/all_credit_organizations.json".
            Поехали...
        ''')
    a = ParserCBRF()
    a.start()
    menu()