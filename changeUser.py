from baseLogic import LINE
from time import sleep
from user import User
import json

def changeData(find_User: dict):
    '''В этой функции мы принимает словарь в виде ключ (фамилия, имя, организация) и значения, которые будем использовать
    для уже внутри этой функции. Это необходимо для того, чтобы во первых, была возможность собрать всех пользователей
    в список и изменять конкретного пользователя без изменения его порядкого номера в итоговом файле.'''
    maxLen = len(sorted(User.dataDict.values(), key=len)[-1]) + 10
    with open('usersFile.json', 'r', encoding='utf-8') as file:
        allUsersFromFile = json.load(file)

    # resultList - это список индексов тех юзеров, которые подходят под наш поиск. Эти индексы потребуются нам для доступа
    # к этим (пока еще) словарям
    resultList = []
    for dct in range(len(allUsersFromFile)):
        if '_organisation' in find_User and allUsersFromFile[dct]['_organisation'] == None:
            continue
        elif '_organisation' in find_User and allUsersFromFile[dct]['_organisation'].lower() == find_User['_organisation'].lower():
            resultList.append(dct)
        elif '_first_name' in find_User and allUsersFromFile[dct]['_first_name'].lower() == find_User['_first_name'].lower():
            resultList.append(dct)
        elif '_second_name' in find_User and allUsersFromFile[dct]['_second_name'].lower() == find_User['_second_name'].lower():
            resultList.append(dct)

    objectList = [User(*i.values()) for i in allUsersFromFile]
    # в objectList - уже объекты класса user

    print(f'Количество пользователей, которых мы нашли: {len(resultList)}')

    # в блок изменений проваливаемся, если мы нашли хоть кого-то по нашим параметрам
    if len(resultList) > 0:
        for num, ind in enumerate(resultList, 1):
            print(f'№ - {num} - {objectList[ind].first_name}, {objectList[ind].second_name}')
        print()
        sleep(1)
        flag = True
        while flag:
            changeNumber = input('Введи порядковый номер пользователя, данные которого ты хочешь изменить ---->>> ')
            if changeNumber.isdigit() and 1 <= int(changeNumber) <= len(resultList):
                currientUser = int(changeNumber) - 1
                flag = False
            else:
                print('Номер введен не корректно!')

        print('Ниже будет предложено ввести НОВЫЕ данные для каждого поля. Если НЕ нужно вносить изменения в это поле - оставь его пустым!')
        LINE()
        sleep(1)
        for key, value in User.dataDict.items():
            newValue = input(f'Введите поле {value.rjust(26)} | '.rjust(maxLen))
            if len(newValue.replace(' ', '')) > 0:
                objectList[resultList[currientUser]].__dict__[key] = newValue

        allUsersFromFile = [user.userList() for user in objectList]

        with open('usersFile.json', 'w', encoding='utf-8') as file:
            json.dump(allUsersFromFile, file, indent=3, ensure_ascii=False)

        print('\nИзменения сохранены!')

    else:
        print('\n', 'К сожалению, найти никого не удалось. Попробуй еще раз!', sep='')




