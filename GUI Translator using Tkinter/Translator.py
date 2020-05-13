from tkinter import *
from googletrans import Translator
from tkinter.messagebox import showinfo

window = Tk()
window.title('Translator')
window.geometry('200x100')

translator = Translator()


def dotranslation():
    word = entry.get()
    result = translator.translate(word).text
    showinfo('Translation', result)


label1 = Label(window, text="Enter your string: ")
label1.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=1, column=0)

button = Button(window, text='Translate', command=dotranslation)
button.grid(row=2, column=0)

window.mainloop()