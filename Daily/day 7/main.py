


me = {
    'name' : 'Rahmat',
    'family' : 'Ansari',
    'age' : 20
}

print(f'dictionary: {me}')
print(f'pop: {me.pop("name")}')
print(f'dictionary: {me}')
me.popitem()
print(f'dictionary: {me}')

me['name'] = 'sara'

print(f'dictionary: {me}')

second = {
    'name' : 'Robert',
    'email' : 'EnAnsari@outlook.com'
}

me.update(second)
print(f'dictionary: {me}')

print('-----------------------')

course = {
    'title' : 'python course',
    'teacher' : 'Mohammad Ordookhani',
    'time' : 8.5,
    'video count' : 97,
    'tags' : ['python', 'online course', 'free course'],
    'sessions' : [
        {
            'title' : 'title_1',
            'time' : 5
        },
        {
            'title': 'title_2',
            'time': 7
        },
        {
            'title': 'title_3',
            'time': 9
        }
    ],
    'related course' : [
        {
            'title': 'java course',
            'teacher': 'Mohammad Ghari',
            'time': 20,
            'video count': 42,
            'tags': ['java', 'online course', 'free course']
        },
        {
            'title': 'csharp course',
            'teacher': 'Iman Mada\'eni',
            'time': 10,
            'video count': 22,
            'tags': ['csharp', 'online course', 'free course']
         }
    ]
}

for related in course['related course']:
    print(related['teacher'])

totalTime = 0
for related in course['related course']:
    totalTime += related['time']
print(f'total time is {totalTime}')

totalTime = 0
for session in course['sessions']:
    totalTime += session['time']
print(f'total time is {totalTime}')

print('-----------------------')

nums = dict(first = 1, second = 2, third = 3)
squaredNums = {key : value ** 2 for key, value in nums.items()}

print(nums)
print(squaredNums)

simpleNums = {num : ("even" if num % 2 == 0 else "odd") for num in range(1, 5 + 1)}
print(simpleNums)

tupleNums = (1, 2, 3, 4, 5)
print(tupleNums, 3 in tupleNums)

item = tuple(range(1, 5 + 1))
print(item)

location = {
    (35.67, 45.78) : 'tehran',
    (40.30, 69.92) : 'new york'
}

print(location[(40.30, 69.92)])
temp = location.keys()
print(temp)

print(tupleNums.count(3))
print(tupleNums[1:3])
print(tupleNums.index(1))

names = ('Ali', 'Mohammad')
print(names.index("Mohammad"))

print('-----------------------')

myset = {1, 4.3, 'Ali'}
print({1, 4.3, False, 'Ali', True}) # 1 == True
print([1, 4.3, False, 'Ali', True])

print(1 in {True, 0, 53.2})

myset.add(54)
print(myset)
myset.remove(True)
print(myset)
myset.discard(True)
myset.discard('Ali')
print(myset)

yourset = myset.copy()
myset.clear()
myset.add(100)
print(f'your set = {yourset}, my set = {myset}')

set1 = {1, 5, 3, 7}
set2 = {6, 3, 2, 1}
print(set1 | set2)
print(set1 & set2)

print("".join({char for char in "Rahmat Ansari"}))

