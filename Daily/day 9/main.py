# day 9 = part 41 to 44 from 97

def sequre(num): return num * num


print(sequre(3))

sums = lambda a, b: a + b

print(sums(5, 3))
print(sequre.__name__)
print(sums.__name__)

print('-----------------------')

numbers = [1, 2, 3, 4, 5, 6]


def func(num): return num * 2


doubles1 = map(lambda num: num * 2, numbers)
doubles2 = list(map(func, numbers))

print(doubles1)
print(list(doubles1))
print(list(doubles1))
print(doubles2)

names = ['ali', 'mohammad', 'rahmat', 'reza']
names2 = list(map(lambda name: name.upper(), names))
print(names2)

people = [
    {'name': 'rahmat', 'family': 'ansari', 'age': 20},
    {'name': 'naser', 'family': 'naseri', 'age': 31},
    {'name': 'jalal', 'family': 'jalali', 'age': 43}
]

families = list(map(lambda person: person['family'], people))
print(families)

print(list(map(lambda person: person['family'], people)))

evens = list(filter(lambda num: num % 2 == 0, list(range(1, 10 + 1))))
print(evens)

users = [
    {'name': 'rahmat', 'shopCard': []},
    {'name': 'reza', 'shopCard': ['kotlin']},
    {'name': 'jalal', 'shopCard': []}
]

print(list(filter(lambda user: len(user['shopCard']) == 0, users)))
print(list(filter(lambda user: not user['shopCard'], users)))

print(" and ".join(list(map(lambda user: user['name'], filter(lambda user: not user['shopCard'], users)))))
print(" and ".join(map(lambda user: user['name'], filter(lambda user: not user['shopCard'], users))))

print(' and '.join([user['name'] for user in users if not user['shopCard']]))

numbers = [0, 4, 2, 6, 10, 12]
print(f'all of numbers is even: {"YES" if all([num % 2 == 0 for num in numbers]) else "NO"}')
print(all([]))

numbers = [3, 5, 1, 43, 95, 112]
print(f'numbers have an even number: {"YES" if any([num % 2 == 0 for num in numbers]) else "NO"}')
print(any([]))

print('-----------------------')

numbers = [5, 3, 2, 5, 6, 1, 7, 10, 0]
print(sorted(numbers, reverse=True))
print(sorted(numbers))
print(numbers)

# we has this dictionary:
# people = [
#     {'name': 'rahmat', 'family': 'ansari', 'age': 20},
#     {'name': 'naser', 'family': 'naseri', 'age': 31},
#     {'name': 'jalal', 'family': 'jalali', 'age': 43}
# ]

print(sorted(people, key=lambda user: user['name'], reverse=True))

print(f'max of {numbers} : {max(numbers)}')
print(f'min of {numbers} : {min(numbers)}')

print(max(people, key=lambda p: len(p['name'])).get('name'))

print(numbers)
print(reversed(numbers))
print(list(reversed(numbers)))

print('hello'[::-1])
print(''.join(reversed('hello')))

for i in reversed(range(0, 10)):
    print(i, end=" ")
print('\n--- THE END ---')