from json import loads, dumps
from csv import DictReader

# Считали данные из json файла
with open("./users.json", "r") as file1:
    users = loads(file1.read())

# Считали данные из csv файла
with open("./books.csv", "r") as file2:
    reader = DictReader(file2)

    library = []

    # Формируем словарь
    for user in users:
        user_of_library = {'name':    user["name"],
                           'gender':  user["gender"],
                           'address': user["address"],
                           }
        book = next(reader)
        book_of_library = {"books": [{"title":  book["Title"],
                                      "author": book["Author"],
                                      "height": book["Height"],
                                      }]
                           }
        
        user_of_library.update(book_of_library)
        library.append(user_of_library)
    print(library)

# Добавляем в новый json файл
with open("./dictionary.json", "w") as fw:
    s = dumps(library, indent=4)
    fw.write(s)


##################### End of file #########################

            # # для прохождения по всем юзерам
            # for user in users:
            #     print(user["friends"][0]["name"])
            #
            # # для прохождения в первом узере
            # userA = users[0]
            # for user in userA['friends']:
            #     print(user)
            # # для образения к конкретному полю
            # userA = users[0]["friends"][1]["name"]
            # print(userA)