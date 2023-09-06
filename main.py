# в этом файле находится основная логика программы. Этот файл мы запускаем в работу. main.py - связующий файл этого ТЗ
# ----->>>>    https://youtu.be/1_3wwyzgMLc    <<<<----- ВИДЕО С ДЕМОНСТРАЦИЕЙ РАБОТЫ И ОБЪЯСНЕНИЕМ ЧТО И КАК РАБОТАЕТ


from baseLogic import startProgram, authorisation, chooseAction, LINE
from createNewUser import addNewUser
from changeUser import changeData
from outByPage import printByPage
from findLogic import findElement


def run():
    flag, mainCycle = authorisation(*startProgram()), True
    while mainCycle:
        action = chooseAction(flag=flag)
        # функция chooseAction вернет нам целое число от 1 до 4 - ключ по которму мы запустим следующую функцию
        if action == 1:
            addNewUser()
            # ключ 1 отвечает за добавление нового пользователя

        elif action == 2:
            secondFlag = True
            while secondFlag:
                findElement()
                print()
                answer = input('Повторить поиск? (да / нет) | ')
                if answer == 'нет':
                    secondFlag = False
                # ключ 2 - за поиск, который мы запускаем в цикле и можем повторять до тех пор, пока не устанем

        elif action == 3:
            printByPage()
            # ключ 3 - за постраничный вывод

        elif action == 4:
            findUser = findElement(findToChange=True)
            changeData(find_User=findUser)
            # ключ 4 - за внесение изменений
            # если в findElement() передать flag=True, то она вернет словарь, в котором мы получим паттерны в виде ключей
            # и данные в виде значений, которые в дальнейшем будем применять для поиска конкретного пользователя.

        else:
            print('Ты выбрал несуществующий или недоступный функционал')

        LINE()
        nextCycle = input('Продолжим работу? (да / нет) | ')

        if nextCycle == 'нет':
            mainCycle = False

    print('Спасибо за использование! Буду ждать тебя снова!')


run()