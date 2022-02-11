
import pickle
import os


class Addrres:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # добавление
    def add(self):
        book = {}
        book['name'] = self.name
        book['age'] = self.age

        data = 'E:\\Python\\' + self.name + '.data'
        f = open(data, 'wb')
        pickle.dump(book, f)
        f.close()
        del book

    # чтение
    def reader(self):
        data = 'E:\\Python\\' + self.name + '.data'
        f = open(data, 'rb')
        stored = pickle.load(f)
        print(stored)

    # удаление
    def deleter(self):
        os.remove('E:\\Python\\' + self.name + '.data')

    # изменение
    def changer(self):
        os.remove('E:\\Python\\' + self.name + '.data')
        newname = input('New name: ')
        newage = input('New age: ')
        self.name = newname
        self.age = newage
        book = {}
        book['name'] = self.name
        book['age'] = self.age

        data = 'E:\\Python\\' + self.name + '.data'
        f = open(data, 'wb')
        pickle.dump(book, f)
        f.close()
        del book

running = True
while running:
    o = input('What do we do: ')

    '''
    добавление - "0"
    чтение - "1"
    изменение - "2"
    удаление - "3"
    '''

    if o == '0':
        a = input('Age: ')
        b = input('Name: ')
        address = Addrres(b, a)
        address.add()
    elif o == '1':
        a = input('Name: ')
        address = Addrres(a, age=1)
        address.reader()
    elif o == '3':
        a = input('Name: ')
        address = Addrres(a, age=1)
        address.deleter()
    elif o == '2':
        a = input('Name: ')
        address = Addrres(a, age=1)
        address.changer()
