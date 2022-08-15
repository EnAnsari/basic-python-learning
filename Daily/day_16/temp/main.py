# day 16 = part 82 97

from time import time

# startTime = time()
# print(sum(num for num in range(200000000)))
# endTime = time()
# print(f'by generator: {endTime - startTime}')
#
# startTime = time()
# print(sum([num for num in range(200000000)]))
# endTime = time()
# print(f'normal: {endTime - startTime}')

def speed_test_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'time elapsed: {end_time - start_time}')
        return result
    return wrapper

@speed_test_decorator
def sum_nums_list():
    return sum([x for x in range(6000000)])

@speed_test_decorator
def sum_nums_gen():
    return sum(x for x in range(6000000))

sum_nums_list()
sum_nums_gen()

# The End
