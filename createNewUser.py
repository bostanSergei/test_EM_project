# в этом файле реализуем добавление новых записей в справочник
from user import User
import json


def addNewUser():
    newUsersList, flag = [], True
    massage = 'Давай добавим в нашу телефонную книгу новых пользователей.\n'
    massage += 'Поля, обязательные для заполнения будут отмечены звёздочкой'
    massage2 = 'Остальные ты можешь оставить пустыми. Им мы присвоим None'
    maxLen = len(sorted(User.dataDict.values(), key=len)[-1]) + 10

    print(massage, massage2, '', sep='\n')
    while flag:
        newUser = User(phone='None', first_name='None', second_name='None')
        userFunc = [newUser.set_first_name, newUser.set_second_name, newUser.set_phone]
        numOperation = 0

        for key, value in User.dataDict.items():
            while True:
                string = value
                if numOperation < 3:
                    string += ' * '
                else:
                    string += '   '
                newValue = input(f'Введите поле {string.rjust(26)} | '.rjust(maxLen))

                if numOperation < 3:
                    try:
                        userFunc[numOperation](newValue)
                        break
                    except:
                        print('problem')

                else:
                    newUser.__dict__[key] = None if newValue == '' else newValue
                    break
            numOperation += 1

        newUsersList.append(newUser)
        print('-' * 41, '\nНовый пользователь добавлен в справочник!')
        answer = input('Добавить еще одного? (да / нет) ')
        if answer == 'нет':
            flag = False

    with open('usersFile.json', 'r', encoding='utf-8') as file:
        allUsersFromFile = json.load(file)
    for user in newUsersList:
        allUsersFromFile.append(user.userList())
    with open('usersFile.json', 'w', encoding='utf-8') as file:
        json.dump(allUsersFromFile, file, indent=3, ensure_ascii=False)

    print(f'Количество добавленных пользователей: {len(newUsersList)}')

addNewUser()
