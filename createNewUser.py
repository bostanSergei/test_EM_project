from baseLogic import LINE
from user import User
import json


def addNewUser():
    '''Функция для создания нового пользователя и добавления в справочник'''
    LINE()
    newUsersList, flag = [], True
    # newUsersList - пока пустой список пользователей, flag - запуск цикла
    massage = 'Поля, обязательные для заполнения будут отмечены звёздочкой. Остальные - можно оставить пустыми!'
    maxLen = len(sorted(User.dataDict.values(), key=len)[-1]) + 10

    print(massage, '', sep='\n')
    while flag:
        newUser = User(phone='None', first_name='None', second_name='None')
        userFunc = [newUser.set_first_name, newUser.set_second_name, newUser.set_phone]
        numOperation = 0
        # инициализируем новый объект класса User с пустыми полями и переменную numOperation(для вывода звездочек - обязательных полей)

        for key, value in User.dataDict.items():
            while True:
                string = value
                if numOperation < 3:
                    string += ' * '
                else:
                    string += '   '
                newValue = input(f'Введи поле {string.rjust(26)} | '.rjust(maxLen))

                if numOperation < 3:
                    try:
                        userFunc[numOperation](newValue)
                        break
                    except ValueError as v:
                        print(v)
                # условие выше будет прокидывать полученные от пользователя данные и прокидывать их в сеттер объекта
                # в сеттере есть некоторые ограничения на допустимые поля, вызывающие ошибку, которые я отрабатываю

                else:
                    newUser.__dict__[key] = None if newValue == '' else newValue
                    break
            numOperation += 1

        # добавляем только что созданного пользователя в список
        newUsersList.append(newUser)
        LINE()
        print('Новый пользователь добавлен в справочник!')
        answer = input('Добавить еще одного? (да / нет) | ')
        if answer == 'нет':
            flag = False

    # считываем данные с файла, добвляем новый словарь, записываем обратно в файл
    with open('usersFile.json', 'r', encoding='utf-8') as file:
        allUsersFromFile = json.load(file)
    for user in newUsersList:
        allUsersFromFile.append(user.userList())
    with open('usersFile.json', 'w', encoding='utf-8') as file:
        json.dump(allUsersFromFile, file, indent=3, ensure_ascii=False)

    print(f'Количество добавленных пользователей: {len(newUsersList)}')


