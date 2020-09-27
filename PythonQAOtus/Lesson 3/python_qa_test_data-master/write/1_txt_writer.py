some_file = open("example_write.txt", "w")

text = """О сколько нам открытий чудных
Готовят просвещенья дух
И Гений парадоксов друг
И Опыт сын ошибок трудных
"""

some_file.write(text)

some_file.close()
