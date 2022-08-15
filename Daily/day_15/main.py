# day 15 = part 71 to 78 from 97

# class Dog:
#     def makeSound(self):
#         return 'dog makes sound'
#
# class Cat:
#     def makeSound(self):
#         return 'cat makes sound'
#
# dog = Dog()
# cat = Cat()
#
# print(cat.makeSound())
# print(dog.makeSound())

class Animal:
    def makeSound(self):
        raise NotImplementedError


class Dog(Animal):
    # def makeSound(self):
    #     return 'dog makes sound'
    pass


class Cat(Animal):
    def makeSound(self):
        return 'cat makes sound'


dog = Dog()
cat = Cat()

print(cat.makeSound())


# print(dog.makeSound())

class IUserService:
    def getAllUsers(self): raise NotImplementedError

    def getUserById(self): raise NotImplementedError

    def createNewUser(self): raise NotImplementedError


class UserServiceBySql(IUserService):
    pass


class UserServiceByOracle(IUserService):
    pass


obj = UserServiceBySql()


class Person:
    def __init__(self, name, family, age, money):
        self.name = name
        self.family = family
        self.age = age
        self.money = money

    def __repr__(self):
        return f'{self.name} {self.family}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.money + other.money

    def __mul__(self, other):
        return self.money * other.money

    def __truediv__(self, other):
        return self.money / other.money


p1 = Person('ali', 'reza', 24, 1000)
p2 = Person('zahra', 'amiri', 19, 2000)

print(len(p1))
print(p1 + p2)
print(p1 * p2)
print(p1 / p2)

# start Advanced Part!

nums = [1, 2, 3, 4, 5]
iterNums = iter(nums)
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))

print('---------------')


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)


nums = [1, 2, 3, 4, 5]
my_for(nums, print)

square = lambda num: print(num * num)
my_for(nums, square)

print('-------------------')


class Counter:
    def __init__(self, start, end, step = 1):
        self.current = start
        self.step = step
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += self.step
            return num
        raise StopIteration

for num in Counter(4, 40, 4):
    print(num, end=" ")
print()

class User:
    index = 0
    ActiveUsers = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        userDict = {'name': name, 'age': age}
        User.ActiveUsers.append(userDict)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(User.ActiveUsers):
            person = User.ActiveUsers[self.index]
            self.index += 1
            return person
        raise StopIteration

p1 = User('mohammad', 23)
p2 = User('ali', 30)
p3 = User('sara', 40)

for p in p1:
    print(p)

print('-------------------')

def count_to_up(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_to_up(10)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

print(fib_list(10))


# print(fib_list(1000000))

def fib_generator(max):
    x, y, count = 0, 1, 0
    while count < max:
        x, y = y, x + y
        yield y
        count += 1

i = 0
for num in fib_generator(10):
    i += 1
    print(f'{i}th number is: {num}')

# for num in fib_generator(1000000):
#     print(num, end=' ')
# print()

print('-------------------------')

def nums():
    for num in range(20):
        yield num

myGenerator = (num for num in range(20))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
# ...

# print(sum(num for num in range(100000000)))
# print(sum([num for num in range(100000000)]))

# << The End >>
