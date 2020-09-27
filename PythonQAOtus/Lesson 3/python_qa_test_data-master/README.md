# Работа с тестовыми данными

- txt
- csv
- json
- xml
- sqlite

### Чтение из файла

```python
f = open("file_name", "r")
f.read()
f.close()
```

### Использование with
```python
with open("file_name", "r") as f:
    f.read()
```

Python содержит встроенные библиотеки для работы json, csv, sqlite, html данными. А так же может быть использован для чтения любого файла в бинарном формате.

### Генераторы и итераторы

Генераторы создаются путем добавления ключевого слова yield в любую функцию. После этого каждое новое обращение к ней вызывает следующую итерацию цикла или выдачу следующего значения.

```python
def squares(start, stop):
    for i in range(start, stop):
        yield i * i

generator = squares(1, 10)
```

```python
def letters():
    yield 'a'
    yield 'b'
```

Итераторы это более общее понятние и в общем случае означает объект который явялется наследником класса у которого реализованы методы __next__ и __iter__

```python
class Squares(object):

    def __init__(self, start, stop):
       self.start = start
       self.stop = stop

    def __iter__(self): 
        return self

    def __next__(self):
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current

iterator = Squares(1, 10)
```