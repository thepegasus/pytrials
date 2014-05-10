#!/usr/bin/python
from Tkinter import *

class MyApp():
    def __init__(self, parent):
        button_width=6
        button_padx="2m"
        button_pady="1m"
        
        buttons_frame_padx="3m"
        buttons_frame_pady="2m"
        buttons_frame_ipadx="3m"
        buttons_frame_ipady="1m"
        
        self.myParent=parent
        self.myContainer1=Frame(parent)
        self.myContainer1.pack()

        self.buttons_frame=Frame(parent)
        
        self.buttons_frame.pack(
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            padx=buttons_frame_padx,
            pady=buttons_frame_pady
            )
        self.top_frame=Frame(self.myContainer1)
        self.top_frame.pack(side=TOP,
                            fill=BOTH,
                            expand=YES
                            )
        
        self.bottom_frame=Frame(self.myContainer1,
                                borderwidth=5, relief=RIDGE,
                                height=50,
                                background="white")

        self.bottom_frame.pack(side=TOP,
                               fill=BOTH,
                               expand=YES
                               )

        self.left_frame=Frame(self.top_frame, background="red",
                              borderwidth=5, relief=RIDGE,
                              height=250, 
                              width=50
                              )
        
        self.left_frame.pack(side=LEFT,
                              fill=BOTH,
                              expand=YES
                              )
        self.right_frame=Frame(self.top_frame, background="tan",
                              borderwidth=5, relief=RIDGE,
                              width=250
                              )
        
        self.right_frame.pack(side=RIGHT,
                              fill=BOTH,
                              expand=YES
                              )
        

        self.button1=Button(self.buttons_frame, command=self.button1Click)
        self.button1.configure(text="OK", background="green")
        self.button1.focus_force()
        self.button1.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
            )
        self.button1.pack(side=LEFT)
        self.button1.bind("<Return>", self.button1Click_a)
        
        self.button2=Button(self.buttons_frame, command=self.button2Click)
        self.button2.configure(text="Cancel", background="red")
        self.button2.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
            )
        self.button2.pack(side=RIGHT)
        self.button2.bind("<Return>", self.button2Click_a)
        
    def button1Click(self):
            if self.button1["background"]=="green":
                self.button1["background"]="yellow"
            else:
                self.button1["background"]="green"

    def button2Click(self):
            self.myParent.destroy()

    def button1Click_a(self, event):
            self.button1Click()

    def button2Click_a(self, event):
            self.button2Click()

root=Tk()
myapp=MyApp(root)
root.mainloop()
