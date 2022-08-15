# day 16 = part 79 to 81 from 97

def sum(number, func):
    total = 0
    for num in range(1, number + 1):
        total += func(num)
    return total


square = lambda num: num ** 2

print(sum(5, square))

from random import choice


# def greet(person = 'ali'):
#     def get_mood():
#         msg = choice(('hello', 'go away', 'good bye'))
#         return msg
#     return get_mood() + " " + person
#
# print(greet('Rahmat'))
#
# res = greet()
# print(res)

def greet(person):
    def get_mood():
        msg = choice(('hello', 'go away', 'good bye'))
        return msg + " " + person

    return get_mood()


res = greet('mohammad')
print(res)

print('-----------------------')


# def my_decorartor(func):
#     def say_bye():
#         print('bye guys')
#         func()
#
#     return say_bye
#
# @my_decorartor
# def say_hello():
#     print('hello guys')
#
# # sayHelloByDecorator = my_decorartor(say_hello)
# # sayHelloByDecorator()
#
# say_hello()

def my_decorartor(func):
    # def say_bye(name):
    #     print(f'bye {name}')
    #     func(name)
    #
    # return say_bye

    def say_bye(*args, **kwargs):
        print('this is working for me')
        func(*args, **kwargs)

    return say_bye


# @my_decorartor
# def say_hello(name):
#     print(f'hello {name}')


# say_hello('Rahmat')


@my_decorartor
def say_my_name(name, family):
    print(f'{name} {family}')


say_my_name('Rahmat', 'Ansari')

print('----------------------------')
from functools import wraps


def my_decorartor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'function name is {func.__name__}')
        print(args)
        print(kwargs)
        return func(*args, **kwargs)

    return wrapper


@my_decorartor
def say_hello(name, family):
    print(f'hello {name} {family}')


say_hello('rahmat', 'ansari')


# help(say_hello)
# print(say_hello.__name__)

def show_decorator(is_show):
    def inner_decorator(func):
        @wraps(func)
        def wrapper():
            if is_show:
                func()
            else:
                print('you dont have permission')
        return wrapper
    return inner_decorator

@show_decorator(False)
def go_to_admin_page():
    print('this is Admin page!')


go_to_admin_page()

print('------------------------')

def check_string_length(characterCount):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(name):
            if len(name) > characterCount:
                print('an error occured')
            else:
                func(name)
            return func
        return wrapper
    return inner_decorator

@check_string_length(5)
def show_name(name):
    print(name)

show_name('rahmat')
show_name('ali')

# print(sum(num for num in range(200000)))
# print(sum([2, 4, 2]))

# continue of this file in ./temp/main.py
