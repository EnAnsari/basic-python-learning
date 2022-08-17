# part 93 to 97(end)
# project 5
# Book store Project

from tkinter import *
import tkinter.messagebox
import backend

window = Tk()
window.title('Book store')

# --------------------- Labels ---------------------------

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

# --------------------- Entries ---------------------------

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
sb1 = Scrollbar(window)
sb1.grid(row=0, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


def get_select_row(event):
    # print(event)
    # index = list1.curselection()[0]
    # print(index)
    # selected_book = list1.get(index)
    # print(selected_book)
    global selected_book
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_book = list1.get(index)

        e1.delete(0, END)
        e1.insert(END, selected_book[1])
        e2.delete(0, END)
        e2.insert(END, selected_book[2])
        e3.delete(0, END)
        e3.insert(END, selected_book[3])
        e4.delete(0, END)
        e4.insert(END, selected_book[4])


list1.bind("<<ListboxSelect>>", get_select_row)


def clear_list():
    list1.delete(0, END)


def fill_list(books):
    for book in books:
        # list1.insert(END, book)
        list1.insert(END, book)

# def view_command():
#     list1.delete(0, END)
#     books = backend.view()
#     for book in books:
#         list1.insert(END, book)

def view_command():
    clear_list()
    books = backend.view()
    fill_list(books)


def search_command():
    clear_list()
    books = backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)


def add_command():
    if title_text.get() and author_text.get() and year_text.get() and isbn_text.get():
        backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        view_command()


def delete_command():
    try:
        print(selected_book[0])
        backend.delete(selected_book[0])
        view_command()
    except:
        tkinter.messagebox.showerror('Error', 'You dont select any thing!')


def update_command():
    try:
        backend.update(selected_book[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        view_command()
    except:
        tkinter.messagebox.showerror('Error', 'You dont select any thing!')


b1 = Button(window, text='view All', width=12, command=lambda: view_command())
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width=12, command=lambda: search_command())
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=lambda: add_command())
b3.grid(row=4, column=3)

b4 = Button(window, text='Update Entry', width=12, command=lambda: update_command())
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete Selected', width=12, command=lambda: delete_command())
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
