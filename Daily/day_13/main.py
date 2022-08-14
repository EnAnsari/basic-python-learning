# day 13 = part 61 to 67 from 97

class User:
    def __init__(self, name):
        self.family = None
        self.name = name

    def _hi(self):
        return f'Hi {self.name}'

    def sayHi(self):
        print(self._hi())


ali = User('Ali')
ali.sayHi()


# print(dir(ali))

class Calculate:
    def sum(self, a, b):
        print(f'{a} + {b} : {a + b}')

    def subtract(self, a, b):
        print(f'{a} - {b} : {a - b}')

    def mulitply(self, a, b):
        print(f'{a} * {b} : {a * b}')

    def division(self, a, b):
        print(f'{a} / {b} : {a / b}')


# Calculate.sum(5, 2) => Error!
obj = Calculate()
obj.sum(5, 2)


class Users:
    allowList = list()


ali = Users()
print(Users.allowList)
ali.allowList.append('Ali')
print(Users.allowList)
Users.allowList.append('Rahmat')
print(ali.allowList)


class User:
    activeUsers = 0

    def __init__(self, name, family):
        self.name = name
        self.family = family
        User.activeUsers += 1
        print(f'{self.name} logged in')

    def logOut(self):
        User.activeUsers -= 1
        print(f'{self.name} has logged out')

    @classmethod
    def getActiveUsers(cls):
        print(f'there are currently {cls.activeUsers} active users')

    @classmethod
    def from_string(cls, string_data):
        data = string_data.split(',')
        return cls(data[0], data[1])


User.getActiveUsers()
me = User('mohammad', 'ardookhani')
you = User('sara', 'moradi')
User.getActiveUsers()

obj = User.from_string('Rahmat,Ansari')
print(obj.name, obj.family)
me.getActiveUsers()

print('--------------------------------------')


class User:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.family} is {self.age}'


me = User('robert', 'Mackenzie', 29)
print(me)


class Person:
    classAttribute = 'test value'

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def showFullname(self):
        return f'{self.name} {self.family}'

    @classmethod
    def showClassAttribute(cls):
        return Person.classAttribute


class User(Person):
    pass


sara = User('sara', 'moradi', 30)
print(sara.showFullname())
print(User.showClassAttribute())
print(Person.classAttribute)