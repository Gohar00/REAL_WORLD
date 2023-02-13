class Person:
    def __init__(self, name="", age=0, address=""):
        self.name = name
        if type(age) == int and age > 0:
            self.age = age
        else:
            self.age = 0
        self.address = address

    def set_info(self, name, age, address):
        self.name = name
        if type(age) == int and age > 0:
            self.age = age
        if type(address) == str:
            self.address = address

    def get_info(self):
        return f'name:{self.name} age:{self.age} address: {self.address}'

    def work(self):
        return f'{self.name} working'

    def sleep(self):
        return f'{self.name} sleeping'
