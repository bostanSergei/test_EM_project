# создадим базовый класс User - это наша запись в телефонной книге
# в момент инициализации будем передавать данные в порядке: телефон / фамилия / имя. Вся остальная информация - не обязательна
# header - потребуется в дальнейшем для выдачи запросов к телефонной книге


class User:
    dataDict = {'_first_name': 'Фамилия', '_second_name': 'Имя', '_phone': 'Сотовый телефон',
                '_father_name': 'Отчество', '_organisation': 'Организация', '_work_phone': 'Рабочий телефон'}


    def __init__(self, phone, first_name, second_name, father_name=None, organisation=None, work_phone=None):
        self._phone = phone
        self._first_name = first_name
        self._second_name = second_name
        self._father_name = father_name
        self._organisation = organisation
        self._work_phone = work_phone


    def userList(self):
        return {key: val for key, val in self.__dict__.items()}


    def get_first_name(self):
        return self._first_name.title()

    def set_first_name(self, newName):
        if isinstance(newName, str) and newName.isalpha() and len(newName) >= 2:
            self._first_name = newName
        else:
            raise ValueError('Некорректная фамилия!')

    first_name = property(get_first_name, set_first_name)


    def get_second_name(self):
        return self._second_name.title()

    def set_second_name(self, newName):
        if isinstance(newName, str) and newName.isalpha() and len(newName) >= 2:
            self._second_name = newName
        else:
            raise ValueError('Некорректное имя!')

    second_name = property(get_second_name, set_second_name)


    def get_phone(self):
        return self._phone

    def set_phone(self, newPhone: str):
        newPhone = newPhone.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
        if isinstance(newPhone, str) and newPhone.isdigit() and len(newPhone) >= 6:
            self._phone = newPhone
        else:
            raise ValueError('Некорректный номер телефона!')

    phone = property(get_phone, set_phone)


    def sortByName(self, sortKey):
        if sortKey == '_first_name':
            startString = f'{self._first_name.ljust(17)}' \
               f'{self._second_name.ljust(23)}' \
               f'{(self._father_name if self._father_name is not None else "нет данных").ljust(25)}'
        else:
            startString = f'{self._second_name.ljust(15)}' \
               f'{(self._father_name if self._father_name is not None else "нет данных").ljust(25)}' \
               f'{self._first_name.ljust(25)}'

        return f'{startString}' \
               f'{self._phone.ljust(30)}' \
               f'{(self._organisation if self._organisation is not None else "нет данных").ljust(30)}' \
               f'{(self._work_phone if self._work_phone is not None else "нет данных").ljust(25)}'

