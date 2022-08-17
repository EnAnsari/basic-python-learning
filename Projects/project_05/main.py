# part 90 to 92 from 97
# project 5
# Calculator Project

from tkinter import *
import tkinter.messagebox

# ------------------- SETTING ------------------------

root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.config(bg=color)

# ------------------- VARIABLES ------------------------

num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# ------------------- FRAMES ------------------------

top_first = Frame(root, width=400, height=50, bg='red')
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg='green')
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg='blue')
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg='yellow')
top_forth.pack(side=TOP)


# ------------------- FUNCTIONS ------------------------

def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong!')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'can not Divide By 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def div():
    try:
        if float(num2.get()) == 0:
            errorMsg('division zero error')
        else:
            value = float(num1.get()) / float(num2.get())
            res_value.set(value)
    except:
            errorMsg('error')


# ------------------- BUTTONS ------------------------

btn_plus = Button(top_third, text='+', width=10, highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text='-', width=10, highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text='*', width=10, highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text='/', width=10, highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

# ------------------- ENTRIES AND LABELS ------------------------

lable_first_num = Label(top_first, text='Input Number 1:', bg=color)
lable_first_num.pack(side=LEFT, pady=10, padx=10)

first_num = Entry(top_first, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)

lable_second_num = Label(top_second, text='Input Number 2:', bg=color)
lable_second_num.pack(side=LEFT, pady=10, padx=10)

second_num = Entry(top_second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)

res = Label(top_forth, text='Result', bg=color)
res.pack(side=LEFT, padx=10, pady=10)

res_num = Entry(top_forth, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT)

root.mainloop()
