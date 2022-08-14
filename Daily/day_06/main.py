# day 6 = part 27 to 30 from 97

items_1 = [4, 4, 6, 1, 5, 3]
items_2 = [num * 2 for num in items_1]
print(items_2)

namelist = [char for char in 'mohammad']
print(namelist)
print([char.upper() for char in 'mohammad'])

print(f'even num in item_1: {[num for num in items_1 if num % 2 == 0]}')

print([num if num % 2 == 0 else num * (-1) for num in items_1])

nums = [[1, 2, 3], [4, 5, 6]]
[[print(l) for l in li] for li in nums]

generatedNestedList = [[newNum for newNum in range(1, 4)] for num in range(1, 4)]
print(generatedNestedList)

print('------------------------------')

myShoppingCard = [
    {
        "name" : "python",
        'price' : 0,
        'age' : 4
    },
    {
        'name' : 'c++',
        'price' : 1800,
        'age' : 6
    }
]
print(myShoppingCard)

mydict = dict(name = 'alexa', price = 3200, age = 23)
print(mydict['name'])

myShoppingCard.append(mydict)

print(myShoppingCard[2].values())
print(myShoppingCard[2].keys())
print(myShoppingCard[2].items())


print('------------------------------')

for i in range(3):
    for key, name in myShoppingCard[i].items():
        print(f'{key} => {name}')
    print('---------------------')

print('alexa' in mydict.values())
mydict2 = mydict.copy()
mydict.clear()
print(mydict)

mydict3 = {}.fromkeys(['name', 'family'], 'unknow')
print(mydict3)

print(mydict3.get('phone') is not None)