import tkinter as tk
from tkinter import filedialog
from tkinter import *
from cartoonify import cartoonify
from PIL import ImageTk, Image
import cv2

top = tk.Tk()
top.geometry('1000x600')
top.title('Cartoonifier')
# top.iconbitmap('/home/sanket/PycharmProjects/Cartoonifier/test.jpeg')
top.configure(background='white')


def save_cartoon(file_path, cartoon):
    fp = filedialog.asksaveasfilename(filetypes=(('JPEG files', '*.jpg'),
                                                 ('PNG Files', '*.png'),
                                                 ('All Files', '*.*')),
                                      defaultextension=file_path)
    cartoon.save(fp)


def show_save_button(file_path, cartoon):
    save_b = Button(top, text='Save', command=lambda: save_cartoon(file_path, cartoon), padx=10, pady=5)
    save_b.place(relx=0.40, rely=0.86)


def convert(file_path):
    cartoon = cartoonify(file_path)
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    cartoon = Image.fromarray(cartoon)
    cartoon.thumbnail(((top.winfo_width()/1.8),(top.winfo_height()/1.8)))
    im = ImageTk.PhotoImage(cartoon)
    label = Label(top, image=im)
    label.image = im
    label.pack(side='right', expand='yes')
    show_save_button(file_path, cartoon)


def show_convert_button(file_path):
    convert_b = Button(top, text='Cartoonify', command=lambda: convert(file_path), padx=10, pady=5)
    convert_b.place(relx=0.60, rely=0.86)


def upload_image():
    file_path = filedialog.askopenfilename()
    inp = Image.open(file_path)
    inp.thumbnail(((top.winfo_width() / 2.22),
                   (top.winfo_height() / 2.22)))
    im = ImageTk.PhotoImage(inp)
    label = Label(top, image=im)
    label.image = im
    label.pack(side='right', expand='yes')
    show_convert_button(file_path)


upload = Button(top, text='Upload an image', command=upload_image, padx=10, pady=5)
upload.configure(background='#adadee', foreground='white', font=('arial', 10, 'bold'))
upload.place(relx=0.20, rely=0.86)

top.mainloop()