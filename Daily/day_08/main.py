# day 8 = part 36 to 40 from 97

def hello():
    print("hello world")

hello()

def add_num():
    a, b = 5, 2
    return a + b

print(add_num())

def sum(a, b):
    return a + b

print(sum(1, 6))


def fullname(str1, str2):
    return f'{str1} {str2}'

print(fullname('Rahmat', 'Ansari'))


def isPrime(num):
    for i in range(2, num // 2):
        if(num % i == 0):
            return False
    return True

print(isPrime(5), isPrime(28), isPrime(51), isPrime(101))


print(fullname(str2='Ansari', str1='Rahmat'))

def sums(*num):
    total = 0
    for temp in num:
        total += temp
    return total

print(sums(2, 3, 2, 4, 5))

def fnames(**ss):
    for name, family in ss.items():
        print(f'Hello {name}. Are you {family}?')

fnames(Rahmat = 'Ansari', Ali = "Alavi")

def power(num1, num2 = 2):
    return num1 ** num2

print(power(2, 4))
print(power(6))


def ppr(*args):
    print(args)

ppr(3, 4, 3, 2)

def sumnumbyList(*n):
    s = 0
    for i in n:
        s += i
    return s

nums = [4, 3, 5, 2, 5]
print(sumnumbyList(*nums))

def display_name(name, family):
    print(f'name: {name}, family: {family}')

# me = {
#     'first name' : 'Rahmat',
#     'last name' : 'Ansari'
# }
#
# display_name(**me)

# result by error!!!

me = {
    'name' : 'Rahmat',
    'family' : 'Ansari'
}

display_name(**me)