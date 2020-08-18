# Description : This is a GUI for a Chatbot

#importing libraries
from tkinter import *


# Creating Tkiner instance with preferred size and a title
root = Tk()
root.title('Chat Bot')
root.geometry('400x500')


# Creating a Menu Bar 
main_menu = Menu(root)

# Adding File menus
file_menu = Menu(root)
file_menu.add_command(label='New File')
file_menu.add_command(label='Save')

#Adding some Menus
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Exit')
root.config(menu = main_menu)


# Creating our Chat Window,, where messeage will be displayed
chatwin = Text(root, bd=1, bg='grey', width = 60, height = 8)
chatwin.place(x=6, y=6, height=385, width =370)

# Creating the message input box
messagebox = Text(root, bg='grey', width=30, height=4)
messagebox.place(x=6, y=400, height=88, width=260)	

# Creating a send button
send = Button(root, text='Send', bg='grey', activebackground='light grey', width=12, height=4)
send.place(x = 270, y=400, height=88, width=100)

#Adding a scrollbar
scrollbar = Scrollbar(root, command=chatwin.yview())
scrollbar.place(x=375, y=6, height=385)

# Running the tkinter app
root.mainloop()
