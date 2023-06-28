from tkinter import *

window = Tk()
# window.title('Blockchain Bank')
# window.minsize(400, 300)
# window.maxsize(600, 450)
# window.geometry('400x300')
# window.resizable(width=False, height=False)

# Label(window, text='Hello World!').pack()
# Label(window, text='Hello World!', font=('Tahoma', 20)).pack()
# Label(window, text='Hello World!', background='aqua', foreground='blue').pack()
#
# Button(window, text='click me!', bg='yellow').pack()

# hello_label = Label(window, text='hello world')
# hello_label.pack()
#
# hello_label.config(fg='blue')

# def print_hello():
#     print('hello world!')
#
# btn = Button(window, text='click me!', command=print_hello)
# btn.pack()

# counter = 0
#
# def increse_counter():
#     global counter
#     counter += 1
#     # print(counter)
#     lbl.config(text=f'counter = {counter}')
#
# btn = Button(window, text='click me!', command=increse_counter)
# lbl = Label(window, text='counter = 0')
#
# lbl.pack()
# btn.pack()

# def change_status():
#     lbl.config(text='status: online', foreground='green')
#
# btn = Button(window, text='click me!', command=change_status, width=40, border=5)
# lbl = Label(window, text='status: offline', fg='red')
#
# lbl.pack()
# btn.pack()

# Label(window, text='First name:').pack()
# first_name = Entry(window)
# first_name.pack()
# Label(window, text='Last name:').pack()
# last_name = Entry(window)
# last_name.pack()
#
# male_var = IntVar()
# Checkbutton(window, text='male', variable=male_var).pack()
#
# def sign_in():
#     prename = ''
#     if male_var.get() == 1:
#         prename = 'mr'
#     else:
#         prename = 'mrs'
#     lbl.config(text=f'Welcome {prename} {first_name.get()} {last_name.get()}')
#
# sign_in_btn = Button(window, text='sign in', command=sign_in)
# sign_in_btn.pack()
#
# lbl = Label(window)
# lbl.pack()

# Modes = [('male', 'man'), ('female', 'woman'), ('unknown', 'none')]
# var = StringVar()
# var.set('man')
#
# for text, mode in Modes:
#     Radiobutton(window, text=text, variable=var, value=mode, indicatoron=0).pack(anchor=W)

# scale_dim = Scale(window, from_=0, to=100, orient=HORIZONTAL)
# scale_dim.pack()
#
# def push_btn():
#     lbl.config(text=f'value = {scale_dim.get()}')
#
# Button(window, text='get value', command=push_btn).pack()
# lbl = Label(window, fg='green')
# lbl.pack()

# Label(window, text='Welcome to translate of TOEFL\'s result', font=('consolas', 10)).pack()
#
# Label(window, text='\n\nReading score', font=('consolas', 8)).pack()
# reading_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
# reading_score.pack()
# Label(window, text='Listening score', font=('consolas', 8)).pack()
# listening_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
# listening_score.pack()
# Label(window, text='Speaking score', font=('consolas', 8)).pack()
# speaking_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
# speaking_score.pack()
# Label(window, text='Writing score', font=('consolas', 8)).pack()
# writing_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
# writing_score.pack()
#
# def result():
#     total_score = reading_score.get() + listening_score.get() + speaking_score.get() + writing_score.get()
#     if total_score >= 100:
#         lbl.config(text=f'\nWelcome to USA\nYour total score is {total_score}', fg='green')
#     else:
#         lbl.config(text=f'\nTry again!\nYour total score is {total_score}', fg='red')
#
# Button(window, text='show me Result', bg='yellow', command=result).pack()
# lbl = Label(window)
# lbl.pack()


window.title('simple gui')
window.geometry('400x500')

# text = Text(window)
# text.pack()
#
# def save_text():
#     with open('output.txt', 'w') as f:
#         f.write(text.get(1.0, END))
#
# def load_text():
#     with open('output.txt') as f:
#         data = f.read()
#     text.insert(INSERT, data)
#
# Button(window, text='save', command=save_text).pack()
# Button(window, text='load', command=load_text).pack()

# name = Entry(window)
# name.pack()
#
# def clear_list():
#     list_box.delete(0, END)
#
# def insert_list():
#     list_box.insert(END, name.get())
#
# Button(window, text='add', width=15, fg='green', command=insert_list).pack()
# Button(window, text='clear', width=15, fg='red', command=clear_list).pack()
#
# list_box = Listbox(window)
# list_box.pack()

# list_box = Listbox(window)
# Scrollbar(window, command=list_box.yview).pack(side=RIGHT, fill=BOTH)
# list_box.pack(expand=True, fill=BOTH)
#
# for line in range(200):
#     list_box.insert(END, 'this is line number: {}'.format(line + 1))

# spin = Spinbox(window, from_=0, to=100)
# spin.pack()
#
# def print_number():
#     print(spin.get())
#
# Button(window, text='get', command=print_number).pack()

# cw = Canvas(window, width=1000, height=1000)
# cw.pack()
#
# cw.create_line(10, 10, 10, 100)
# cw.create_line(50, 10, 50, 100, fill='red', dash=(3, 3))
# cw.create_rectangle(70, 10, 150, 150, fill='blue', outline='red')
# cw.create_oval(190, 10, 260, 300, fill='yellow')
# cw.create_arc(10, 200, 150, 300, fill='aqua')
# cw.create_polygon([300, 10, 400, 350, 500, 200, 700, 300], fill='pink', outline='blue')
# cw.create_text(100, 400, fill='darkblue', font='Times 20 italic bold', text='EnAnsari')
# image_file = PhotoImage(file='C:\\Users\\Mateo\\Pictures\\Screenshots\\Screenshot-1.png')
# cw.create_image(400, 500, image=image_file)

# top = Toplevel()
# top.title('hint')
# top.geometry('200x100')
# top.resizable(width=False, height=False)
# Label(top, text='this is top window').pack()

# frame1 = LabelFrame(window, text='registration')
# frame1.pack(fill=BOTH, expand=True)
#
# frame2 = Frame(window, bg='yellow')
# frame2.pack(expand=True, fill=BOTH)
#
# Label(frame1, text='label in frame 1').pack()
# Label(frame2, text='label in frame 2').pack()

# panel_1 = PanedWindow(window, bg='red', bd=4)
# panel_1.pack(fill='both', expand=True)
#
# label_pn1 = Label(panel_1, text='panel 1')
# panel_1.add(label_pn1)
#
# panel_2 = PanedWindow(window, bg='blue', bd=4, orient='vertical')
# panel_1.add(panel_2)
#
# label_pn2 = Label(panel_2, text='panel 2')
# panel_2.add(label_pn2)
#
# panel_2.add(Label(panel_2, text='test'))

# menubar = Menu(window)
#
# def save_file():
#     with open('output.txt', 'w') as f:
#         f.write(text.get(1.0, END))
#
# def open_file():
#     with open('output.txt') as f:
#         data = f.read()
#     text.insert('insert', data)
#
# filemenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='Save', command=save_file)
# filemenu.add_command(label='Open', command=open_file)
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=window.quit)
#
# editmenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=editmenu)
# editmenu.add_command(label='Copy')
# editmenu.add_command(label='Cut')
# editmenu.add_command(label='Paste')
#
# helpmenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')
#
# window.config(menu=menubar)
#
# text = Text(window)
# text.pack()

# from tkinter import messagebox
#
# def show_info():
#     messagebox.showinfo('Author', 'created by Rahmat')
#
# def show_exit():
#     value = messagebox.askquestion('exit', 'do you want exit?')
#     if value == 1:
#         window.quit()
#
# def show_error():
#     messagebox.showerror('error', 'something not ok!')
#
# def show_warn():
#     messagebox.showwarning('warn', 'hey - you are warning!')
#
# menubar = Menu(window)
# menubar.add_command(label='info', command=show_info)
# menubar.add_command(label='exit', command=show_exit)
#
# Button(window, text='error', command=show_error).pack()
# Button(window, text='warning', command=show_warn).pack()
#
# window.config(menu=menubar)

f0 = Frame(window, bg='yellow')
f0.pack(expand=True, fill='both')
lables = ['First Name', 'Last Name', 'Site', 'Social Media']

i = 0
for item in lables:
    Label(f0, text=item).grid(row=i, column=0)
    Entry(f0).grid(row=i, column=1)
    i += 1


f1 = Frame(window, bg='aqua')
f1.pack(expand=True, fill='both')

f2 = LabelFrame(window, bg='pink')
f2.pack(expand=True, fill='both')

Label(f1, text='test 1', bg='red').grid(row=0, column=0)
Label(f1, text='test 2', bg='purple').grid(row=0, column=1)
Label(f1, text='test 3', bg='gray').grid(row=1, column=0)
Label(f1, text='test 4', bg='yellow').grid(row=4, column=4)

Label(f2, text='name: ', bg='white').grid(row=0, column=0)
Entry(f2).grid(row=0, column=1)

Label(window, text='test 5').pack()





window.mainloop()
