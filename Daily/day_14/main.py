# day 14 = part 68 to 70 from 97

class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def set_age(self, value):
    #     if value >= 0:
    #         self._age = value
    #     else:
    #         raise ValueError('age can not be negative number!')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError('age can not be negative!')

    @property
    def fullName(self):
        return f'{self.name} {self.family}'

    def showFullName(self):
        return f'{self.name} {self.family}'


me = Person('ali', 'mohammadi', 9)
me.age = 19
print(me.age)
print(me.showFullName())
print(me.fullName)

print('----------------------')


class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    @property
    def fullName(self):
        return f'{self.name} {self.family}'


class User(Person):
    def __init__(self, name, family, email):
        super().__init__(name, family)
        self.email = email

me = User('rahmat', 'ansari', 'rahamt2022a@gamil.com')
print(me.fullName)
print(me.email)

print('------------------------')

# class Person:
#     def __init__(self, name):
#         print("init in Person")
#         self.name = name
#     def sayHello(self):
#         return f'Hello {self.name} in Person Class'
#
# class User:
#     def __init__(self, name):
#         print("init in User")
#         self.name = name
#     def sayHello(self):
#         return f'Hello {self.name} in User Class'
#     def sayBye(self):
#         return f'Bye Bye {self.name}'
#
# class Admin(Person, User):
#     def __init__(self, name):
#         print("init in Admin")
#         super().__init__(name)
#
# person1 = Admin('Ali')
# print(person1.name)
# print(person1.sayHello())
#
# print(isinstance(person1, Admin))
# print(isinstance(person1, Person))
# print(isinstance(person1, User))
#
# print(person1.sayBye())

class Person:
    def __init__(self, name):
        print("init in Person")
        self.__name = name
    def sayHello(self):
        return f'Hello {self.__name} in Person Class'

class User:
    def __init__(self, name):
        print("init in User")
        self.__name = name
    def sayHello(self):
        return f'Hello {self.__name} in User Class'
    def sayBye(self):
        return f'Bye Bye {self.__name}'

class Admin(Person, User):
    def __init__(self):
        print("init in Admin")
        User.__init__(self, 'user name')
        Person.__init__(self, 'person name')


person1 = Admin()
print(person1._Person__name)
print(person1._User__name)

print(Admin.__mro__)
print(Admin.mro())
# help(Admin)

print('----------------------')

class A:
    def sayHi(self):
        print('hello in A')

class B(A):
    pass
    # def sayHi(self):
    #     print('hello in B')

class C(A):
    pass
    # def sayHi(self):
    #     print('hello in C')

class D(B, C):
    pass
    # def sayHi(self):
    #     print('hello in D')

item = D()
item.sayHi()
help(D)