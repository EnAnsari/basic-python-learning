# day 3 = part 12 to 16 from 97

grade = -6

if grade < 0 or grade > 20:
    print("wrong!")
elif grade < 10:
    print("bad")
elif grade < 15:
    print("good")
else:
    print("great!")

print("true grade") if grade <= 20 and grade >= 0 else print("wrong grade")

print("-----------------------")

list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)

print(f'list 1 = {list_1}')
print(f'list 2 = {list_2}')
print(f'list 3 = {list_3}')

print(list_1 == list_2)
print(list_1 == list_3)
print(list_1 is list_2)
print(list_1 is list_3)

print("-----------------------")

# car = input('Enter car name : ')
# if car:
#     print(f'your car is {car}')

num1, num2 = 93, 93
print(f'{num1} == {num2} : {num1 == num2}')

gender = "male"
age = 19
helth = False

if (gender == 'male') and not age < 18 and helth is True:
    print('you should go to soldiery bro!')

