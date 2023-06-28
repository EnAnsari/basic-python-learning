from tkinter import *

window = Tk()

window.title('TOEFL result')
window.geometry('400x500')

Label(window, text='Welcome to translate of TOEFL\'s result', font=('consolas', 10)).pack()

Label(window, text='\n\nReading score', font=('consolas', 8)).pack()
reading_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
reading_score.pack()
Label(window, text='Listening score', font=('consolas', 8)).pack()
listening_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
listening_score.pack()
Label(window, text='Speaking score', font=('consolas', 8)).pack()
speaking_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
speaking_score.pack()
Label(window, text='Writing score', font=('consolas', 8)).pack()
writing_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
writing_score.pack()

def result():
    total_score = reading_score.get() + listening_score.get() + speaking_score.get() + writing_score.get()
    if total_score >= 100:
        lbl.config(text=f'\nWelcome to USA\nYour total score is {total_score}', fg='green')
    else:
        lbl.config(text=f'\nTry again!\nYour total score is {total_score}', fg='red')

Button(window, text='show me Result', bg='yellow', command=result).pack()
lbl = Label(window)
lbl.pack()

window.mainloop()