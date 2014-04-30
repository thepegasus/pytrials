#/usr/bin/python
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World")

B=Tkinter.Button(top, text="Click Me", command=helloCallBack)
B.pack()

top.mainloop()
