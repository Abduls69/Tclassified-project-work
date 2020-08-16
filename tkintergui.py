# TKinter is a graphical user interface for python. It is a standard python interface

# How do you create an application using tkinter
'''
import the module-tkinter
Create any number of widgets to the main window
Apply the even Trigger on the widgets
'''

from tkinter import *

window = Tk()

# add widgets here
btn = Button(window, text = 'This is a button widget', fg = 'green',)
btn.place(x = 60, y = 100)
# Label widget
lbl = Label(window, text = 'This is a label widget', fg = 'red', font = ('Helvertical', 16))
lbl.place(x = 60, y = 50)

# Entry widget
txtfld = Entry (window, text = 'This is an entry widget', fg = 'red', bd = 5)
txtfld.place(x = 80, y = 150)

window.title('Welcome to Tclassified.com ICT center')
window.geometry('400x300+10+20')
window.mainloop()

