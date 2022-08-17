# part 83 from 97

textfile = open('text.txt')
# print(textfile.read())
# # print(textfile.read())
#
# textfile.seek(0)
# print(textfile.read())

# print(textfile.readline(), end='')
# print(textfile.readline(), end='')

print(textfile.readlines())

textfile.close()

with open('text.txt') as File:
    print(File.read())


# with open('./text.txt', mode='w') as File:
#     File.write('hello honey!')

with open('text.txt', mode='a') as File:
    File.write('\nhello honey!')
