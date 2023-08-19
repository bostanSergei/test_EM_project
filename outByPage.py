# реализуем постраничный (что бы это не значило)) вывод словаря в консоль


from user import User
import json
from time import sleep


def printByPage():
    print('Вы можете выбрать ключевой элемент, по которому будет выполняться сортировка при постраничном выводе')
    header = [['Фамилия', 'Имя', 'Отчество', 'Сотовый телефон', 'Организация', 'Рабочий телефон'],
              ['Имя', 'Отчество', 'Фамилия', 'Сотовый телефон', 'Организация', 'Рабочий телефон']]
    sortList = [['По фамилии - 1', '_first_name'], ['По имени - 2', '_second_name']]
    flag = True

    while flag:
        answer = input(f"{'     |     '.join([i[0] for i in sortList])}    |   ")
        if answer not in ['1', '2']:
            print('Вы выбрали некорректную сортировку. Повторите!')
        else:
            sortKey = sortList[int(answer) - 1][1]
            flag = False

    with open('usersFile.json', 'r', encoding='utf-8') as file:
        allUsersFromFile = json.load(file)

    allUsersFromFile.sort(key=lambda user: user[sortKey])
    print()
    objectList = [User(*i.values()) for i in allUsersFromFile]
    mainKey = [user.__dict__[sortKey][0] for user in objectList]
    pageKey = sorted(set(mainKey), key=lambda x: mainKey.index(x))

    space = ' ' * 8 + '|' + ' ' * 8
    lenHeader = len(space) * (len(header[int(answer) - 1]) - 1) + sum([len(i) for i in header[int(answer) - 1]])

    print('_' * lenHeader)
    print((space.join(header[int(answer) - 1])))
    print('¯' * lenHeader)

    startIndex = 0
    for alpha in pageKey:
        print(alpha)
        for index in range(startIndex, len(objectList)):
            if objectList[index].__dict__[sortKey][0] == alpha:
                print(objectList[index].sortByName(sortKey))
                startIndex += 1
            else:
                break
        print(lenHeader * '-', '\n')

printByPage()

