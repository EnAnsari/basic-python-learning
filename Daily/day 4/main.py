# day 4 = part 17 to 19 from 97

listofnumbers = [51, 81, 79, 100]
for num in listofnumbers:
    print(num, end=" ")
print('')

rangeofnumbers = range(0, 100, 15)
for num in rangeofnumbers:
    print(num, end=" ")
print('')

print(range(10))
print(list(range(10)))

for num in range(1, 10):
    print('*' * num)

print('-----------------------')

# for num in range(1, 10):
#     if num % 2 == 1:
#         for star in range(1, 6):
#             print('*' * star)
#     else:
#         for star in range(5, 0, -1):
#             print('*' * star)


# mypassword = 'AliAli'
# while True:
#     yourpassword = input('Enter password : ')
#     if mypassword == yourpassword:
#         print('\U0001f600' * 5)
#         break
#     else:
#         print('wrong, try again!')

