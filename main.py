from user import User
import json


u1 = User('+7 960 915 48 08', 'Bostan', 'Sergey')
u2 = User('+79509201223', 'Иванов', 'Иван', 'Иванович', 'Good Company', '+74953654235')
u3 = User('+79609206523', 'Иванов', 'Григорий', 'Петрович', 'Bad Company', '+74953654565')
u4 = User('+79504325678', 'Герасимов', 'Николай', 'Тимофеевич', 'Рога и копыта', '+74863654200')
u5 = User('+7 999-354-67-89', 'Николаев', 'Герман', 'Григорьевич', 'ООО Питон и компания')

usersList = []

for user in [u1, u2, u3, u4, u5]:
    usersList.append(user.userList())

with open('usersFile.json', 'w', encoding='utf-8') as file:
    json.dump(usersList, file, indent=3, ensure_ascii=False)


















