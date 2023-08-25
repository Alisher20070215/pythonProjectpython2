from homework4 import People, People2, A, B

class C(People, People2, A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def a(self):
        print(self)

    def b(self):
        print(self)

        self.age = self._age

    @property
    def age(self):
        self._age
        return
    @age.setter
    def age(self):
        return
