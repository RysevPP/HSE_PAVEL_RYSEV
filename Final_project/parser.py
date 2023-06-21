import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path


class ParserCBRF:

    def __init__(self):
        self.URL = 'https://cbr.ru/banking_sector/credit/FullCoList/'
        self.base={}
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')


    def __parser(self):
        r = requests.get(self.URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', class_='data levels')
        name_column=[]

        for i in table.find_all('th'):
            title = i.text
            name_column.append(title)

        for j in table.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text.replace('\xa0', ' ') for i in row_data]
            self.base[row[3]] = {name_column[4]:row[4], name_column[5]:row[5], name_column[8]:row[8],
                                 name_column[6]:row[6], name_column[2]:row[2],
                                 name_column[7]:row[7].replace('\n', 'Действует').replace('ОТЗ', 'Отозвана').replace('АНН', 'Аннулирована').replace('РЕГ', 'Не получена')}

    def __file(self):
        with open(self.file_base, 'w') as f:
            json.dump(self.base, f)

    def start(self):
        self.__parser()
        self.__file()
        return (self.base)