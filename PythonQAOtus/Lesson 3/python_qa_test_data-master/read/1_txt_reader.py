some_file = open("../files/example.txt", "r")

# Читаем кол-во байт
print(some_file.read(7))

# Читаем строку
print(some_file.readline())

# Построчно массив
print(some_file.readlines(), "\n")

# Всё что осталось
print(some_file.read())

some_file.close()
