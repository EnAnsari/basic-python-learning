# day 5 = part 21 to 26 from 97

items = ['hi', 'hello', 54.4, True, 'hola']
print(items[-1])
print('bonjour' in items)

for item in items:
    if type(item) == str:
        print(f'{item} is a string')
    else:
        print(f'{item} is not a string')

print('-----------------------')

index = 0
while index < len(items):
    item = items[index]
    if type(item) == str:
        print(f'{item} is a string')
    else:
        print(f'{item} is not a string')
    index += 1

print('-----------------------')

print(f'items: {items}')
items.append("bonjour")
print(f'items: {items}')
items.extend(['slm', 'salam'])
print(f'items: {items}')
items.insert(2, 'assalam')
print(f'items: {items}')

print('-----------------------')

items_2 = list(items)
print(f'items_2: {items_2}')
items_2.clear()
print(f'items: {items}')
print(f'items_2: {items_2}')
poped = items.pop(-1)
print(f'poped: {poped}')
print(f'items: {items}')

if 'salam' in items:
    items.remove('salam')

if 'bonjour' in items:
    items.remove('bonjour')

print(f'items: {items}')

print('-----------------------')

print(items.index('assalam', 1, 4))
items.insert(0, 'hello')
items.append('hello')

print(f'items: {items}')
print(items.count('hello'))

obj = 'hello'
if items.count(obj) != 0:
    print(f'index of {obj} is {items.index(obj, 1)}')

print('-----------------------')

from random import randint
mylist = []
for i in range(11):
    mylist.append(randint(1, 10))

print(mylist)
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)

list_2 = []
for item in items:
    if type(item) == str:
        list_2.append(item)

print(' + '.join(list_2))

print('-----------------------')

name = 'Rahmat Ansari'
print(name[::-1])
print(name[:8])
print(name[-6:])
