import json
from pathlib import Path


class StatusLicenseSort:

    def __init__(self, status):
        self.status = status
        self.file_base = Path(Path.cwd(), 'parsed_data', 'all_credit_organizations.json')
        self.file_status_base = Path(Path.cwd(), 'parsed_data', 'status_credit_organizations.json')
        self.base_status = {}

    def __loading(self):
        with open(self.file_base, "r") as f:
            self.load = json.load(f)

    def __status_sort(self):
        for key, value in self.load.items():
            if self.status.lower() == value['Статус лицензии'].lower():
                self.base_status[key] = value

    def __save(self):
        with open(self.file_status_base, 'w') as f:
            json.dump(self.base_status, f)

    def start(self):
        self.__loading()
        self.__status_sort()
        self.__save()
        return self.base_status