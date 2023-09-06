from outByPage import SPACE, HEADER
from baseLogic import LINE
from time import sleep
from user import User
import json

def findElement(findToChange=False):
    '''findToChange - ключ по которому мы решаем как и для чего мы будем выполнять поиск по нашему справочнику. Если
    мы хотим в последствии что-то изменить, то в функцию передаем True и поиск будет осуществляться по одному паттерну.
    Если это "стандартный поиск" - можем выбрать ДО трех паттернов для поиска с дальнейшим выводом результатов на экран.
    Список findList - использую для вывода вспомагательной информации на экран и выбора ключей для поиска'''
    findList = [['По имени', '_second_name', 'Имя'], ['По фамилии', '_first_name', 'Фамилию'], ['По организации', '_organisation', 'Организацию']]
    massage1 = 'Тебе доступен поиск по имени, фамилии и организации. Ты можешь комбинировать эти паттерны по своему усмотрению.'
    massage2 = 'То есть искать или только по имени, или по имени и фамилии или, к примеру, по фамилии и огранизации. Давай начнем!'
    flag, numPattern = True, 1

    if not findToChange:
        LINE()
        print(massage1, massage2, sep='\n')
        LINE()

        while flag:
            answer = input('Сколько паттернов будем использовать? (1, 2 или 3): | ')
            if answer not in ['1', '2', '3']:
                print('Выбрать можно только еденицу, двойку или тройку!')
            else:
                numPattern, flag = int(answer), False

        LINE()

    if findToChange:
        LINE()
        print('Перед тем как что-то менять, давай найдем это ЧТО-ТО. Поиск возможен по одному из паттеров:')
        sleep(1.1)

    patternList = []
    if numPattern != 3:
        # в этом IF-е я выбираю ключи по которым будет выполняться дальнейший поиск. Ключи собираются в список patternList
        exampleList = [f'{num} - {pattern[0]}' for num, pattern in enumerate(findList, 1)]
        while len(patternList) != numPattern:
            print(f'{" | ".join(exampleList)}')
            newPattern = input('Выбери паттерн, который хочешь добавить в критерии поиска | ')
            if newPattern.isdigit() and newPattern in [i[0] for i in exampleList]:
                index = [i[0] for i in exampleList].index(newPattern)
                currientPattern = exampleList.pop(index)[4:]
                patternList.extend([element[1] for element in findList if currientPattern in element])
            else:
                print('Нет такого паттерна. Попробуй еще раз!')
        LINE()

    # если на этапе выбора количества паттернов выбрали тройку, то просто добавим все ключи в patternList.
    elif numPattern == 3:
        patternList = [element[1] for element in findList]

    sleep(1)

    # словарь find_User хранит в себе пары свойство объекта: значение по которму будет происходить поиск
    # по факту количество пар в словаре - количество паттернов, которое было выбрано шагом ранее
    find_User = {}
    for i in patternList:
        currientRequest = [j[2] for j in findList if i in j]
        currientAnswer = input((f'Введи {currientRequest[0].upper()} для поиска | ').rjust(35))
        find_User[i] = currientAnswer

    LINE()

    # если мы собираемся менять значения нашего справочника - на этом этапе поиск закончен и пора вернуть словарь в след.функцию
    if findToChange:
        return find_User

    with open('usersFile.json', 'r', encoding='utf-8') as file:
        allUsersFromFile = json.load(file)

    # resultList - список пока что обычных словарей, которые подходт по условиям поиска. Сначала пустой. После цикла - с совпадениями
    resultList = []
    for dct in allUsersFromFile:
        if len([True for key, val in find_User.items() if dct[key] is not None and val.lower() == dct[key].lower()]) == len(find_User):
            resultList.append(dct)

    lenHeader = len(SPACE) * (len(HEADER[0]) - 1) + sum([len(i) for i in HEADER[0]])
    resultUsers = [User(*k.values()) for k in resultList]
    # resultUsers - это уже список объектов, которые в следующих строчках будут выведены на экран. Либо нет, если список пустой
    # зачем нужен HEADER[0]? В разделе постраничного вывода я расширил функционал. Добавил возможность предварительно
    # отсортировать справочник или по имени или по фамилии. Здесь решил не усложнять и просто вывел список найденных пользователей

    print('\n', f'Количество пользователей которых мы нашли по текущему запросу: {len(resultUsers)}', sep='')
    if len(resultUsers) == 0:
        print('К сожалению, ты ошибся в паттернах или таких пользователей нет в базе')
    else:
        print('Вот они:')
        sleep(1)
        print('_' * lenHeader)
        print((SPACE.join(HEADER[0])))
        print('¯' * lenHeader)

        for el in range(len(resultUsers)):
            print(resultUsers[el].sortByName('_first_name'))
