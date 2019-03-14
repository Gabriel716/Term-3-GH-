# class Critter(object):
#
#     total=0 #related to the class as a whole
#     def __init__(self,name):
#         print("A critter was born")
#         self.name=name
#         Critter.total+=1
#
#     def __str__(self):
#         rep="Critter object\n"
#         rep+="Name:",self.name,"\n"
#         return rep
#
#     def talk(self):
#         print("Hi, I am",self.name,"\n")
#
#     @staticmethod
#     def status():
#         """Static method"""
#         print("\nThe total number of critters is",Critter.total)
# print("Access the Critter.total:",end="")
# print(Critter.total)
# print("\nCreating critters")
# crit1=Critter("Joe")
# Critter.status()
# crit2=Critter("Bob")
# Critter.status()
# crit3=Critter("Nate")
# Critter.status()


# class Critter(object):
#     def __init__(self,name,mood):
#         print("A critter was born")
#         self.name=name #public attribute
#         self.__mood=mood #private attribute
#     def talk(self):
#         print("\n'm",self.name)
#         print("Right now I feel",self.__mood,"\n")
#     def __private_method(self):
#         print("This is a private method")
#         self.__private_method()
#         crit.name="Bob"
#     def public_method(self):
#         print("This is a public method")
#         crit.__mood="Bad mood"
# class Critter2(object):
#     def __init__(self,name,mood):
#         print("A critter was born")
#         self.name=name #public attribute
#         self.__mood=mood #private attribute
#     def talk(self):
#         print("\n'm",self.name)
#         print("Right now I feel",self.__mood,"\n")
#     def __private_method(self):
#         print("This is a private method")
#         self.__private_method()
#     def public_method(self):
#         print("This is a public method")
#         crit.__mood="Bad mood"
# crit=Critter(name="Bob",mood="happy")
# crit1=Critter2(name="Joe",mood="happy")
# crit.talk()
# crit1.talk()
# crit.public_method()
# crit1.public_method()
# crit.talk()


# class Critter(object):
#     def __int__(self,name):
#         print("A new critter was born")
#         self.__name=name
#     @property
#     def name(self):#public method
#         return self.__name
#     @name.setter
#     def name(self,new_name):
#         if new_name=="":
#             print("A critter's name can't be an empty string")
#         else:
#             self.__name=new_name
#             print("Name change successful")
#     def talk(self):
#         print("\nHello","I am",self.name)
#
# crit=Critter("Chicken")
# crit.talk()
# print("\My critter's name is:",end="")
# print(crit.name)
# print("\Attempting to change my critter's name to Duck")
# crit.name="Duck"
# print(crit.name)
# print("\nAttempting to change my critter's name to the empty string")
# crit.name=""
# print("My criter's name is:",end="")
# print(crit.name)

a = ""
import random
hunger=0
class Critter(object):
    def __init__(self,critter_name):
        self.critter_name = critter_name
        self.hunger=0
        self.boredom=0
    def __pass_time(self):
            self.hunger+=1
            self.boredom+=1
    def play(self,fun=0):
        print("The critter says 'yo'")
        self.fun=random.randrange(0,10)
        self.boredom-=fun
        if self.boredom<0:
            self.boredom=0
        else:
            self.__pass_time()
    def talk(self):
        c=self.mood
        print("Hi I am", a,"Who is", c)


    def eat(self,food=0):
        self.food=random.randrange(0,10)
        print("I eat food")
        self.hunger-=food
        if self.hunger<0:
            hunger=0
        else:
            self.__pass_time()



    @property
    def mood(self):
        unhappiness=self.hunger + self.boredom

        if unhappiness<5:
            mood="Happy"
        elif 5<=unhappiness<=10:
            mood="Okay"
        elif 11<=unhappiness<=15:
            mood="Frustrated"
        else:
            mood="MAD LAD"
        return mood

def main():
        global a
        a=input("What do you want your pet's name to be?")
        crit=Critter(a)
        choice=None
        #choice=input("Enter 1 to talk, enter 2 to eat, enter 3 to play, and 0 to leave")
        while choice!=0:
            #display menu
            choice=input("Enter 1 to talk, enter 2 to eat, enter 3 to play, and 0 to leave")
            if choice=="0":
             print("Good bye")
             break
            #break
            elif choice=="1":
                crit.talk()
            elif choice=="2":
                crit.eat()
            elif choice=="3":
                crit.play()
            else:
                print("That is not a good choice")
main()























