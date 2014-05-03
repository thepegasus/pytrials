#!/usr/bin/python
from Tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myParent=parent
        self.myContainer1=Frame(parent)
        self.myContainer1.pack()
        self.button1=Button(self.myContainer1)
        self.button1["text"]="Colour Change!"
        self.button1["background"]="green"
        self.button1.pack(side=LEFT)
        self.button1.bind("<Button-1>", self.button1Click)
        
        self.button2=Button(self.myContainer1)
        self.button2.configure(text="Off to join the circus")
        self.button2.configure(background="tan")
        self.button2.pack(side=LEFT)
        self.button2.bind("<Button-1>", self.button2Click)
        
        self.button3=Button(self.myContainer1)
        self.button3.configure(text="Join me?", background="cyan")
        self.button3.pack(side=BOTTOM)
        
        self.button4=Button(self.myContainer1, text="Good bye!", background="red")
        self.button4.pack(side=LEFT)

    def button1Click(self, event):
        if self.button1["background"]=="green":
           self.button1["background"]="red"
        else:
                self.button1["background"]="blue"
    def button2Click(self, event):
        self.myParent.destroy()


root=Tk()
#root.title="Test"
myapp=MyApp(root)
root.mainloop()