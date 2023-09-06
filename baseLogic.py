from outByPage import lineLen
from time import sleep


def LINE():
    print(lineLen * '-')


def startProgram():
    '''Функция отвечает за старт программы. Приветствие. Вопросы для авторизации. login, password: admin/admin'''
    LINE()
    print('Привет! Это телефонный справочник. Перед началом работы давай узнаем, какой функционал тебе доступен')
    sleep(1)
    login = input('Введи свой логин | ')
    password = input('Введи свой пароль | ')
    print()
    return login, password


def authorisation(login: str, password: str):
    '''Хоть такой задачи и не стояло, но очень простая авторизация. НЕавторизированный пользователь НЕ может
    изменять уже существующие записи, НО ему доступен весь остальной функционал. login: admin, password: admin'''
    return True if login + password == 'adminadmin' else False


def chooseAction(flag: bool):
    '''flag: True или False - авторизирован пользователь или нет. По этому значению мы либо показываем часть функционала, либо нет
    actionList и whatYouCanDo - список действий, доступных пользователю и список доступных ответов, которые могут выбрать юзеры
    Сама функция отвечает только за выбор действия и вернет целое число (условный ключ) по которому мы отправим пользователя дальше'''
    actionList = ['1 - Добавить новую запись', '2 - Найти существующую', '3 - Вывести всех пользователей', '4 - Внести изменения']
    whatYouCanDo = ['1', '2', '3', '4'][:[3, 4][flag]]
    string = f'{"   |   ".join(actionList[:[3, 4][flag]])}'

    LINE()
    print(string)
    sleep(0.5)

    flagAction = True
    while flagAction:
        action = input('Выбери действие, которое хочешь выполнить | ')
        if action in whatYouCanDo:
            flagAction = False
        else:
            print('Этот функционал для тебя недоступен или ты ошибся при вводе!')
    return int(action)
