#!/usr/bin/python
from Tkinter import *

class MyApp:
    def __init__(self, parent):
        self.lastButton=None
        self.myParent=parent
        self.myContainer1=Frame(parent)
        self.myContainer1.pack()
        self.button1=Button(self.myContainer1, command=self.button1Click)
        self.button1["text"]="Button One - E"
        self.button1["background"]="green"
        self.button1.pack(side=LEFT)
        self.button1.bind("<Button-1>", self.button1Click_a)
        self.button1.focus_force()
        
        self.button2=Button(self.myContainer1, command=self.button2Click)
        self.button2.configure(text="Button Two - 2E")
        self.button2.configure(background="tan")
        self.button2.pack(side=LEFT)
        self.button2.bind("<Button-1>", self.button2Click_a)
        self.button2.bind("<Return>", self.button2Click_a)
        
        self.button3=Button(self.myContainer1, command=self.button3Click)
        self.button3.configure(text="Button Three - C", background="cyan")
        self.button3.pack(side=BOTTOM)
        
        self.button4=Button(self.myContainer1, text="Button Four - C", background="red", command=self.button4Click)
        self.button4.pack(side=LEFT)

    def button1Click(self):
        if self.button1["background"]=="green":
            self.button1["background"]="red"
        else:
            self.button1["background"]="blue"
        self.showLast()
        self.lastButton="One - Command Bind"
    def button1Click_a(self, event):
        print "Button Click "+str(event.type)
        self.button1Click()
        self.showLast()
        self.lastButton="One - Event Bind"

    def button2Click_a(self, event):
        print "Event binded"
        report_event(event)
        self.button2Click()
        self.showLast()
        self.lastButton="Two - Event Bind"

    def button2Click(self):
        print "Command Binded"
        self.showLast()
        self.lastButton="Two - Command Bind"
    #self.myParent.destroy()
    def button3Click(self):
        print "Button3Click event handler"
        self.showLast()
        self.lastButton="Three - Event Bind"
    def button4Click(self):
        print "Button4Click event handler"
        self.showLast()
        self.lastButton="Four - Event Bind"
    def showLast(self):
        print self.lastButton
def report_event(event):
    """Print a description of an event based on its attributes.
    """
    event_name={"2":"Keypress", "4":"ButtonPress"}
    print "Time:", str(event.time)
    print "EventType:" + str(event.type), \
        event_name[str(event.type)], \
        "EventWidgetID="+ str(event.widget), \
        "EventKeySymbol=" + str(event.keysym)

print "\n"*100
print "Starting"
root=Tk()
#root.title="Test"
myapp=MyApp(root)
root.mainloop()
print "...Done"
