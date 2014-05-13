#!/usr/bin/python3
from tkinter import *
from urllib.request import *
#from tkinter.ttk import *
class pegaBrowser:
    url=None
    topFrame=None
    contentFrame=None
    frame_padx="1m"
    frame_pady="1m"
    frame_ipadx="1m"
    frame_ipady="1m"
    def __init__(self, master=None):
        mainContainer=Frame(master)
        mainContainer.pack()
        self.topFrame=Frame(mainContainer, background="red")

        self.topFrame.pack(side=TOP,fill=X, expand=YES,anchor=W,
            padx=self.frame_padx,
            pady=self.frame_pady)

        self.contentFrame=Frame(mainContainer,background="blue")
        self.contentFrame.pack(side=TOP)       
        #self.initializeScreen()
        
    def initializeScreen(self):
        self.addressLabel=Label(self.topFrame, text="Address")
        self.addressLabel.pack(side=LEFT)
        self.addressBar=Entry(self.topFrame, width=50,)
        
        #For easy debug
        self.addressBar.insert(0,"http://google.com")
        self.addressBar.pack(side=LEFT)
        self.goButton=Button(self.topFrame,text="Go")
        self.goButton.configure(           
            padx="1m",
            pady="1m"
            )
        self.goButton.pack(side=LEFT)
        self.goButton.bind("<Button-1>",self.goButtonHandler)        
        
        self.contentArea=Label(self.contentFrame)
        self.contentArea.pack(side=BOTTOM,fill=BOTH, expand=YES)
    def goButtonHandler(self, event):
        self.url=self.addressBar.get()
        #self.contentArea["text"]="Fetching "+self.url
        htmlData=getHttpResource(self.url)    
        self.contentArea["text"]=htmlData

def getHttpResource(url):
        #Get resource from server
        response=urlopen(url)
        html=response.read()
        return html

       

root=Tk()
root.title("PegaBrowser - 0.1")

#root.minsize(600,400)
#Start the window maximized
#w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("800x600") 
pegabrowser=pegaBrowser(root)
root.mainloop()
