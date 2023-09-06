from user import User
import json


SPACE = ' ' * 8 + '|' + ' ' * 8
HEADER = [['Фамилия', 'Имя', 'Отчество', 'Сотовый телефон', 'Организация', 'Рабочий телефон'],
          ['Имя', 'Отчество', 'Фамилия', 'Сотовый телефон', 'Организация', 'Рабочий телефон']]
lineLen = len(SPACE) * (len(HEADER[0]) - 1) + sum([len(i) for i in HEADER[0]])
# в этом файле у меня были сформированы заголовки и появилось понимание "границ" моего вывода, которые я вывел в
# скажем так, константы и решил использовать в других частях своей программы

def printByPage():
    '''Функция для постраничного вывода. Пользователь может выбрать как он будет сортировать вывод - по имени или по фамилии'''
    print('-' * lineLen)
    sortList = [['1 - По фамилии', '_first_name'], ['2 - По имени', '_second_name']]
    print('Ты можешь выбрать по какому ключу сортировать данные для вывода на экран', f"{'   |   '.join([i[0] for i in sortList])}", sep='\n')
    flag = True

    # выбираем ключ для сортировки
    while flag:
        answer = input('Выбери ключ для сортировки | ')
        if answer not in ['1', '2']:
            print('Не корректный выбор!')
        else:
            sortKey = sortList[int(answer) - 1][1]
            flag = False

    # открываем файл
    with open('usersFile.json', 'r', encoding='utf-8') as file:
        allUsersFromFile = json.load(file)

    # сортируем)
    allUsersFromFile.sort(key=lambda user: user[sortKey])
    print()
    objectList = [User(*i.values()) for i in allUsersFromFile]
    mainKey = [user.__dict__[sortKey][0] for user in objectList]
    pageKey = sorted(set(mainKey), key=lambda x: mainKey.index(x))

    lenHeader = len(SPACE) * (len(HEADER[int(answer) - 1]) - 1) + sum([len(i) for i in HEADER[int(answer) - 1]])
    # формируем шапку в зависимости от предыдущего выбора ключа
    print('_' * lenHeader)
    print((SPACE.join(HEADER[int(answer) - 1])))
    print('¯' * lenHeader)

    # начинаем выводить наших пользователей в алфавитном порядке, каждая строка вывода - результат работы метода объекта
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

