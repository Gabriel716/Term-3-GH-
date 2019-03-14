#Gabriel Harrison
#3/5/19
#GUI practice 2

from tkinter import *

class Application(Frame):
    def __init__(self,master):
        """Initialize the frame"""
        super(Application,self).__init__(master)
        self.grid()
        self.click_count=0
        self.create_widgets()
    def create_widgets(self):
        self.lbl = Label(text="Total count")
        self.lbl.grid()
        self.button1=Button(self)
        self.button1["text"]="Click here to add click count"
        self.button1["command"]=self.add_count
        self.button1.grid()
        self.button2=Button(self)
        self.button2["text"]=" Click here to subtract count"
        self.button2["command"]=self.subtract_count
        self.button2.grid()
        self.button3=Button(self)
        self.button3["text"]="Click here to multiply click count"
        self.button3["command"]=self.multiply_count
        self.button3.grid()
        self.button4=Button(self)
        self.button4["text"]="Click here to divide click count"
        self.button4["command"]=self.divide_count
        self.button4.grid()



    def add_count(self):
        """Increase click count"""
        self.click_count+=1
        self.button1["text"] = "Click here to add click count"
        self.lbl["text"] = "The total click count is" + str(self.click_count)
    def subtract_count(self):
        """Subtract from click count"""
        self.click_count-=1
        self.button2["text"]=" Click here to subtract count"
        self.lbl["text"] = "The total click count is" + str(self.click_count)
    def multiply_count(self):
        """Multiply the click count"""
        self.click_count=self.click_count*2
        self.button3["text"]="Click here to multiply click count"
        self.lbl["text"] = "The total click count is" + str(self.click_count)
    def divide_count(self):
        """Divide the click count by 2"""
        self.click_count=self.click_count/2
        self.button4["text"]="Click here to divide click count"
        self.lbl["text"] = "The total click count is" + str(self.click_count)
root=Tk()
root.title("GUI practice 2")
root.geometry("200x200")
app=Application(root)
root.mainloop()







root.mainloop()