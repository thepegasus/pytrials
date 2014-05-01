#/usr/bin/python
from Tkinter import *
import tkMessageBox
top=Tk()

def helloCallBack():
   tkMessageBox. showinfo("Hello Python", "Hello World")

var=StringVar()
label=Label(top, textvariable=var, relief=RAISED)
var.set("Hey! How are you doing?")
B=Button(top, text="Click Me", command=helloCallBack)
B.pack()
label.pack()

top.mainloop()
