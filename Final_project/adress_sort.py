import json
from pathlib import Path


class AdressSort:

    def __init__(self, adress):
        self.adress = adress
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')
        self.file_adress_base = Path(Path.cwd(), 'parsed_data', 'adress_credit_organizations.json')
        self.base_adress = {}

    def __loading(self):
        with open(self.file_base, "r") as f:
            self.load = json.load(f)

    def __adress_sort(self):
        for key, value in self.load.items():
            if self.adress.lower() in value['Местонахождение'].lower():
                self.base_adress[key] = value

    def __save(self):
        with open(self.file_adress_base, 'w') as f:
            json.dump(self.base_adress, f)

    def start(self):
        self.__loading()
        self.__adress_sort()
        self.__save()
        return self.base_adress