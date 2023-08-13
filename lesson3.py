# инкапсуляция
# 1 капсула
# 2 уровни защиты
# 3 публичный,приватный,скрытый

class Bank:
    def __init__(self, name, age, money, password):
        self._name = name
        self._age = age
        self._money = money
        self.__passw = password

    @property
    def pname(self):
        return
        print(self._name, self._money)
    @pname.setter
    def pname(self):
        return

    @property
    def __ppas(self):
        return
        print(self.__passw)
    @__ppas.setter
    def __ppas(self):
        return

    @property
    def pasww(self):
        self.__ppas
        return
    @pasww.setter
    def pasww(self):
        return


beka = Bank('бека', 20, 0, '12345678987543')
beka._money = 123456789

print(beka._money)
beka.pname

beka.__passw = '0'
print(beka.__passw)
beka.pasww
print(dir(Bank))
