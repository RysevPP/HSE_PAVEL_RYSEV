import json
import datetime
from pathlib import Path


class EarlierSort:

    def __init__(self, date):
        self.d = datetime.datetime.strptime(date, '%d.%m.%Y')
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')
        self.file_earlier_base = Path(Path.cwd(), 'parsed_data', 'earlier_credit_organizations.json')
        self.base_earlier = {}

    def __loading(self):
        with open(self.file_base, "r") as f:
            self.load = json.load(f)

    def __earlier_sort(self):
        for key, value in self.load.items():
            self.d1 = datetime.datetime.strptime(value['Дата регистрации Банком России'], '%d.%m.%Y')
            if self.d1 < self.d:
                self.base_earlier[key] = value

    def __save(self):
        with open(self.file_earlier_base, 'w') as f:
            json.dump(self.base_earlier, f)

    def start(self):
        self.__loading()
        self.__earlier_sort()
        self.__save()
        return self.base_earlier


class LaterSort:

    def __init__(self, date):
        self.d = datetime.datetime.strptime(date, '%d.%m.%Y')
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')
        self.file_later_base = Path(Path.cwd(), 'parsed_data', 'later_credit_organizations.json')
        self.base_later = {}

    def __loading(self):
        with open(self.file_base, "r") as f:
            self.load = json.load(f)

    def __later_sort(self):
        for key, value in self.load.items():
            self.d1 = datetime.datetime.strptime(value['Дата регистрации Банком России'], '%d.%m.%Y')
            if self.d1 > self.d:
                self.base_later[key] = value

    def __save(self):
        with open(self.file_later_base, 'w') as f:
            json.dump(self.base_later, f)

    def start(self):
        self.__loading()
        self.__later_sort()
        self.__save()
        return self.base_later


class IntervalSort:

    def __init__(self, date_lower, date_upper):
        self.d_l = datetime.datetime.strptime(date_lower, '%d.%m.%Y')
        self.d_u = datetime.datetime.strptime(date_upper, '%d.%m.%Y')
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')
        # self.file_base = 'all_credit_organizations.json'
        self.file_interval_base = Path(Path.cwd(), 'parsed_data', 'interval_credit_organizations.json')
        # self.file_interval_base = 'interval_credit_organizations.json'
        self.base_interval = {}

    def __loading(self):
        with open(self.file_base, "r") as f:
            self.load = json.load(f)

    def __interval_sort(self):
        for key, value in self.load.items():
            self.d = datetime.datetime.strptime(value['Дата регистрации Банком России'], '%d.%m.%Y')
            if (self.d > self.d_l) and (self.d < self.d_u):
                self.base_interval[key] = value

    def __save(self):
        with open(self.file_interval_base, 'w') as f:
            json.dump(self.base_interval, f)

    def start(self):
        self.__loading()
        self.__interval_sort()
        self.__save()
        return self.base_interval


class CurrentSort:

    def __init__(self, date):
        self.d = datetime.datetime.strptime(date, '%d.%m.%Y')
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')
        self.file_current_base = Path(Path.cwd(), 'parsed_data', 'current_credit_organizations.json')
        self.base_current = {}

    def __loading(self):
        with open(self.file_base, "r") as f:
            self.load = json.load(f)

    def __current_sort(self):
        for key, value in self.load.items():
            self.d1 = datetime.datetime.strptime(value['Дата регистрации Банком России'], '%d.%m.%Y')
            if self.d1 == self.d:
                self.base_current[key] = value

    def __save(self):
        with open(self.file_current_base, 'w') as f:
            json.dump(self.base_current, f)

    def start(self):
        self.__loading()
        self.__current_sort()
        self.__save()
        return self.base_current