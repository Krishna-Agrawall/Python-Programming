#In this pyfile we learn about What is Inheritance

'''
credit:w3schools.com

Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''

# Now First We Are Creating The Parent Class
class Parent:
    no_of_leave=8

    #Now calling constructor method
    def __init__(self,aname,aage,aprofession):
        self.name = aname
        self.age = aage
        self.profession = aprofession

    # Now calling the printing method
    def parent_detaial(self):
        return f'Name is: {self.name}. Age is: {self.age} And Profession is: {self.profession} '

    # Now Calling the class method
    @classmethod
    def change_leave(cls,new_leave):
        cls.no_of_leave=new_leave

   #Now Calling the alternative method
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))

    # Now Calling the static method
    @staticmethod
    def static(string):
        print('Hello I Am Parent And You '+string)


#Let's create the instance of parent

ram=Parent.from_dash('Shri Ram-43-King')
sita=Parent.from_dash('Mata Sita-42-Queen')

#Let's chang the no_of_leaves

Parent.change_leave(16)

# Let's print the detail and no of leaves
print(ram.parent_detaial())
print(sita.parent_detaial())
print(ram.no_of_leave)
print(sita.no_of_leave)

#Let print the static method

print(ram.static('I Am Also Parent'))


#Now let's create the child class
class Children(Parent):
    no_of_day=23
    #Creating the constructor method
    def __init__(self,aname,aage,aprofession,alanguage):
        self.name=aname
        self.age=aage
        self.profession=aprofession
        self.language=alanguage

    # Calling the printing method
    def child_detail(self):
        return f'Name is: {self.name}. Age is: {self.age} And Profession is: {self.profession} .Languages are: {self.language}'

    # Now Calling the class method
    @classmethod
    def change_leave(cls,new_leave):
        cls.no_of_leave=new_leave

   #Now Calling the alternative method
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))

#Now Creating the instance
luv=Children.from_dash('Shri Luv-17-Programmer-[C,Pyton,Java]')
kush=Children.from_dash('Shri Kush-19-Programmer-[C++,R,Java Script]')

#printing detail of child and days
print(luv.child_detail())
print(kush.child_detail())

# print(luv.parent_detaial())

print(luv.no_of_day)