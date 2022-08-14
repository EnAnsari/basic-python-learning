# day 12 = part 55 to 60 from 97

# class User:
#     pass
#
# mohammad = User()
# print(type(mohammad))

class User:
    userName = 'Mohammad'
    userFamily = 'Ansari'
    userAge = 20

    def showFullName(self):
        return self.userName + " " + self.userFamily

    def __init__(self, userName, userFamily):
        self.userName = userName
        self.userFamily = userFamily


obj1 = User('ali', 'bagheri')
obj2 = User('rahmat', 'ansari')
print(obj1.showFullName())
print(obj2.showFullName())

print(obj1.userName + ' ' + obj1.userFamily)


class car:
    def __init__(self, name, numOfDoors, color):
        self.name = name
        self.numOfDoors = numOfDoors
        self.color = color

    def showFullInfo(self):
        return f'car name is {self.name} and car color is {self.color}'

bmw = car('bmw 8', 4, 'blue')
print(bmw.showFullInfo())
print(bmw.numOfDoors)