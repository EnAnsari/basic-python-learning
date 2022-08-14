# day 10 = part 45 to 49 from 97

data = [4, 2, 45, 2, 5]
print(len(data))
print(data.__len__())

number = -34
print(abs(number))
print(number.__abs__())

print(sum(data, 10))

print(round(42.1))
print(round(42.8))
print(round(42.5))

number = 43.25254542
print(round(number, 3))

print('----------------------------')

nums1 = [3, 5, 2, 14, 4]
nums2 = [4, 2, 42, 6, 0]
print(list(zip(nums1, nums2)))

myList = [(3, 4), (5, 2), (2, 42), (14, 6), (4, 0)]
print(list(zip(*myList)))

students = ['mohammad', 'iman', 'sara']
midterm = [78, 80, 94]
final = [90, 88, 92]

print(list(zip(students, midterm, final)))
print({t[0]: max(t[1], t[2]) for t in zip(students, midterm, final)})

print(dict(zip(students, map(lambda x: max(x), zip(midterm, final)))))

# average
print({t[0]: (t[1] + t[2]) / 2 for t in zip(students, midterm, final)})
print(
    dict(
        zip(
            students,
            map(
                lambda x: (x[0] + x[1]) / 2,
                zip(midterm, final)
            )
        )
    )
)

print('----------------------------')


def colorsize(text, color):
    colors = ('red', 'green', 'blue')
    if type(text) is not str:
        raise TypeError("text must be a string!")
    elif color not in colors:
        raise ValueError(f'{color} is not find!')
    else:
        print(f'printed {text in color}')


myName = 'Rahmat'

try:
    print(myName)
except:
    print("an Error!")

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return 'no key found!'
    except IndexError:
        return 'no index found!'

nums1 = [3, 5, 2, 5, 6, 3]
nums2 = {
    'ali': 3,
    'jack': 4,
    'leo': 30
}

print(get(nums1, 4))
print(get(nums1, 10))

print(get(nums2, 'leo'))
print(get(nums2, 'sina'))

# while True:
#     try:
#         num = int(input("please enter a number: "))
#     except:
#         print("Error - please another one!")
#     else:
#         print('you have entered a number!')
#         break
#     finally:
#         print('this is finally section!')

def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return 'don\'t divide by 0 please!'
    except TypeError as err:
        return f'we have an error: {err}'

print(divide(4, 6))
print(divide(4, 0))
print(divide(4, '212'))