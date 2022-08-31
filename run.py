import sys
from pathlib import Path
from pydantic import ValidationError
from base import *


class Converter:
    def __init__(self, file):
        self.file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        if self._file_existing(value):
            self.__file = value

    @staticmethod
    def _file_existing(value):
        if type(value) is str:
            if not Path(value).is_file():
                raise FileNotFoundError(f'Файл {value} не найден')
            return True
        raise TypeError(f'Путь должен быть строкой')

    @staticmethod
    def _is_file_json_or_raise_type_error(file):
        '''проверка формата файла'''
        if Path(file).suffix == '.json':
            return True
        raise TypeError(f'Этот файл ({file}) невозможно обработать')

    @staticmethod
    def _file_dependencies_and_return_json(text):
        phone = {
            "city": str(text.contacts.phone[1:4]),
            "country": str(text.contacts.phone[:1]),
            "number": f'{text.contacts.phone[4:7]}-{text.contacts.phone[7:9]}-{text.contacts.phone[9:]}'
        }

        contacts = {
            "email": text.contacts.email,
            "name": text.contacts.fullName,
            "phone": phone
        }

        coordinates = {
            "latitude": text.address.lat,
            "longitude": text.address.lng
        }

        salary_range = {
            "from": text.salary.from_,
            "to": text.salary.to
        }

        schedule = {
            "id": text.employment
        }

        data = {
            "address": text.address.value,
            "contacts": contacts,
            "coordinates": coordinates,
            "description": text.description,
            "experience": '',
            "name": text.name,
            "salary": text.salary.to,
            "salary_range": salary_range,
            "schedule": schedule
        }
        result = ResultData.parse_obj(data)
        return result.json(ensure_ascii=False, sort_keys=True, by_alias=True)

    def launch(self):
        self._is_file_json_or_raise_type_error(self.file)

        try:
            text = IncomingData.parse_file(self.file)
        except ValidationError as e:
            print(e)
        else:
            result = self._file_dependencies_and_return_json(text)

            with open('Result.json', 'w', encoding='utf-8') as outfile:
                outfile.write(result)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = sys.argv[1]
        Converter(file).launch()
    else:
        raise AttributeError('Не передан аргумент при запуске программы')
