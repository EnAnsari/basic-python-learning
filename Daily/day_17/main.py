# day 16 = part 83 to end(97)
# 83 in folder ./83/main.py
# 84 in folder ./84/main.py
# 85 and 86 in folder ./85_86
# 87 in folder ./87/main.py
# other in project 5, 6

from tkinter import *

root = Tk()
# root.title('button')
root.title('Entry')
root.geometry('400x300')
root.resizable(width=False, height=False)

# my_name = StringVar()

# def print_my_name():
#     my_name.set('my name is Rahmat')
#     # print('my name is Rahmat')
#
#
# btn = Button(root, text='show my name', command=lambda: print_my_name())
# btn.place(x=10, y=10)
#
# lable = Label(root, textvariable=my_name)
# lable.place(x=10, y=50)

nameLable = Label(root, text='Please Enter your name:')
nameLable.place(x=8, y=10)
nameInput = Entry(root)
nameInput.place(x=10, y=30)

# def get_name():
#     print(nameInput.get())

get_name = lambda: print(nameInput.get())

btn = Button(root, text='get name', command=lambda: get_name())
btn.place(x=10, y=60)

root.mainloop()
