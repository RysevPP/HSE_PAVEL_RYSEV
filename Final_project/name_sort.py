import json
from pathlib import Path


class NameSort:

    def __init__(self, name):
        self.name = name
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')
        self.file_name_base = Path(Path.cwd(), 'parsed_data', 'name_credit_organizations.json')
        self.base_name = {}

    def __loading(self):
        with open(self.file_base, "r") as f:
            self.load = json.load(f)

    def __name_sort(self):
        for key, value in self.load.items():
            if self.name.lower() in value['Наименование'].lower():
                self.base_name[key] = value

    def __save(self):
        with open(self.file_name_base, 'w') as f:
            json.dump(self.base_name, f)

    def start(self):
        self.__loading()
        self.__name_sort()
        self.__save()
        return self.base_name