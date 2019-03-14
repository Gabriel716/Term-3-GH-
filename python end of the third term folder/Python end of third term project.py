# Colton Miller
# Gabe Harrison
# 3/7/19

from tkinter import *
import pickle, shelve


class Application(Frame):
    """Gui Application that adds characters to a file"""

    def __init__(self, master):
        """Initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.lbl1 = Label(self, text="Enter your Character name")
        self.lbl1.configure(fg="Black")
        self.lbl1.grid(row=0, column=0, columnspan=3)

        # Entry box that takes the input and makes a file for the character
        self.nametxt = Entry(self)
        self.nametxt.configure(width=35)
        self.nametxt.grid(row=0, column=4,columnspan=3,sticky=NSEW)

        self.lbl2 = Label(self, text="Character Stats")
        self.lbl2.configure(fg="Black")
        self.lbl2.grid(row=1, column=0, columnspan=8,sticky =NSEW)

      

       
        

        # Button that allows start creating characters
        self.buttn1 = Button(self, text="Click me to create Your Characters!")
        self.buttn1["command"] = self.w_char
        self.buttn1.configure(fg="Black")
        self.buttn1.grid(row=5, column=0, columnspan=3)

        Label(self, text="Load Character",width=15).grid(row=9, column=0,columnspan=8,sticky=NSEW)
        Label(self, text="Enter character name:",width=15).grid(row=10, column=0,columnspan=3,sticky=NSEW)
        
        # button that allows you see previously made characters
        self.buttn2 = Button(self, text="Load previous character")
        self.buttn2["command"] = self.view
        self.buttn2.configure(fg="Black")
        self.buttn2.grid(row=12, column=0, columnspan=4)

        # These are stat entries
        self.lab1 = Label(self, text="Shooting",width=15)
        self.lab1.grid(row=2, column=0,sticky=E)

        Label(self, text="",width=15).grid(row=6, column=0,columnspan=8)
        Label(self, text="",width=15).grid(row=7, column=0,columnspan=8)
        Label(self, text="",width=15).grid(row=8, column=0,columnspan=8)

        self.ent1 = Spinbox(self, from_=0, to=99)
        self.ent1.configure(width=5)
        self.ent1.grid(row=2, column=1)

        self.lab2 = Label(self, text="Melee",width=15)
        self.lab2.grid(row=3, column=0,sticky=E)

        self.ent2 =  Spinbox(self, from_=0, to=99)
        self.ent2.configure(width=5)
        self.ent2.grid(row=3, column=1)

        self.lab3 = Label(self, text="Construction",width=15)
        self.lab3.grid(row=4, column=0,sticky=E)

        self.ent3 =  Spinbox(self, from_=0, to=99)
        self.ent3.configure(width=5)
        self.ent3.grid(row=4, column=1)

        self.lab4 = Label(self, text="Mining",width=15)
        self.lab4.grid(row=2, column=2, sticky=E)

        self.ent4 =  Spinbox(self, from_=0, to=99)
        self.ent4.configure(width=5)
        self.ent4.grid(row=2, column=3,sticky=W)

        self.lab5 = Label(self, text="Cooking",width=15)
        self.lab5.grid(row=3, column=2,sticky=E)

        self.ent5 =  Spinbox(self, from_=0, to=99)
        self.ent5.configure(width=5)
        self.ent5.grid(row=3, column=3, sticky=W)

        self.lab6 = Label(self, text="Plants",width=15)
        self.lab6.grid(row=4, column=2, sticky=E)

        self.ent6 =  Spinbox(self, from_=0, to=99)
        self.ent6.configure(width=5)
        self.ent6.grid(row=4, column=3, sticky=W)

        self.lab7 = Label(self, text="Animals",width=15)
        self.lab7.grid(row=2, column=4, sticky=E)

        self.ent7 =  Spinbox(self, from_=0, to=99)
        self.ent7.configure(width=5)
        self.ent7.grid(row=2, column=5, sticky=W)

        self.lab8 = Label(self, text="Crafting",width=15)
        self.lab8.grid(row=3, column=4, sticky=E)

        self.ent8 =  Spinbox(self, from_=0, to=99)
        self.ent8.configure(width=5)
        self.ent8.grid(row=3, column=5, sticky=W)

        self.lab9 = Label(self, text="Artistic",width=15)
        self.lab9.grid(row=4, column=4, sticky=E)

        self.ent9 =  Spinbox(self, from_=0, to=99)
        self.ent9.configure(width=5)
        self.ent9.grid(row=4, column=5,sticky=W)

        self.lab10 = Label(self, text="Medical",width=15)
        self.lab10.grid(row=2, column=6, sticky=E)

        self.ent10 =  Spinbox(self, from_=0, to=99)
        self.ent10.configure(width=5)
        self.ent10.grid(row=2, column=7, sticky=W)

        self.lab11 = Label(self, text="Social",width=15)
        self.lab11.grid(row=3, column=6, sticky=E)

        self.ent11 =  Spinbox(self, from_=0, to=99)
        self.ent11.configure(width=5)
        self.ent11.grid(row=3, column=7, sticky=W)

        self.lab12 = Label(self, text="Intellectual",width=15)
        self.lab12.grid(row=4, column=6, sticky=E)

        self.ent12 =  Spinbox(self, from_=0, to=99)
        self.ent12.configure(width=5)
        self.ent12.grid(row=4, column=7, sticky=W)
         #Label for the second name
        
         #Name to get character
        self.namefile=Entry(self, text=".txt.",width=35)
        self.namefile.configure(fg="Black")
        self.namefile.grid(row=10,column=4,columnspan=4)
        self.displaybox=Text(self, height=5,width=80)
        self.displaybox.grid(row=11,column=0,columnspan=8)
    def w_char(self):
        char = self.nametxt.get()
        shooting = self.ent1.get()
        melee = self.ent2.get()
        construction = self.ent3.get()
        mining = self.ent4.get()
        cooking = self.ent5.get()
        plants = self.ent6.get()
        animals = self.ent7.get()
        crafting = self.ent8.get()
        artistic = self.ent9.get()
        medical = self.ent10.get()
        social = self.ent11.get()
        intellectual = self.ent12.get()
        self.char = open(char, "w")
        self.char.write(shooting + "shooting"+"\n")
        self.char.write(melee + "melee"+"\n")
        self.char.write(construction + "construction"+"\n")
        self.char.write(mining + "mining"+"\n")
        self.char.write(cooking + "cooking"+"\n")
        self.char.write(plants + "cooking"+"\n")
        self.char.write(animals + "cooking"+"\n")
        self.char.write(crafting + "crafting"+"\n")
        self.char.write(artistic + "artistic"+"\n")
        self.char.write(medical + "medical"+"\n")
        self.char.write(social + "social"+"\n")
        self.char.write(intellectual + "intellectual"+"\n")
        self.char.close()
                            

    def view(self):
        char = self.namefile.get()
        if char == "":
            self.lbl2 = Label(self, text="You MUST enter a name")
            self.lbl2.grid(row=1, column=6, sticky=W)
            self.create_widget
        else:
            char=self.namefile.get()
            char=open(char,"r")
            look=pickle.load(char)
            print(look)
            self.char.close()
        

        #self.name2 = Entry(self)
        #self.name2.grid(row = 2, column = 3)
        #char = self.name.get()
        #if self.name2 == "":
            #self.lbl3 = Label(self, text = "You MUST enter a name")
            #self.lbl3.grid(row = 2, column = 4, sticky = W)
            #view(self)
        #elif self.name2 != char:
            #self.lbl4=Label(self, text = "You MUST enter a VALID name")
            #self.lbl4.grid(row = 2, column =5, sticky = W)
        #else:
            #self.char=open(name2, "r")
            #self.char.close
            
            


root = Tk()

root.title("Rimworld Character Sheet")
root.geometry("600x600")
app = Application(root)
root.mainloop()
