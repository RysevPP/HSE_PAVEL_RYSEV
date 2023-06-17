import json
from pathlib import Path


class RegNumSort:

    def __init__(self, registration_number):
        self.regnum = registration_number
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')
        self.file_regnum_base = Path(Path.cwd(), 'parsed_data', 'regnum_credit_organizations.json')
        self.base_regnum = {}

    def __loading(self):
        with open(self.file_base, "r") as f:
            self.load = json.load(f)

    def __regnum_sort(self):
        for key, value in self.load.items():
            if self.regnum.lower() in value['Регистрационный номер'].lower():
                self.base_regnum[key] = value

    def __save(self):
        with open(self.file_regnum_base, 'w') as f:
            json.dump(self.base_regnum, f)

    def start(self):
        self.__loading()
        self.__regnum_sort()
        self.__save()
        return self.base_regnum