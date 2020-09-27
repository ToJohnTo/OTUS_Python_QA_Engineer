
class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        # Чтобы остановить итератор
        # if self.a > 1000:
        #     raise StopIteration
        return x

myclass = MyNumbers()

for el in myclass:
    print(el)
