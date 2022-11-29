#In this pyfile we learn about What is  Multiple Inheritance
'''
credit:geeksforgeeks.org
What is a multiple inheritance in Python?
Image result for multiple inheritance in python
When a class is derived from more than one base class it is called multiple Inheritance.
'''

#Creating the first class
class Parent:
    no_of_day=7

    #calling the constructor method
    def __init__(self,name,age,profession):
        self.name=name
        self.age=age
        self.profession=profession

    # Now calling the printing method
    def parent_detail(self):
        return f'Name is: {self.name} . Age is: {self.age} and Profession is: {self.profession}'

# Creating the instance or objects
vijay=Parent('Vijay Rai',55,'Army Officer')
supriya=Parent('Supriya Rai',53,'Charted Accountant')

#printing the details of parent class
print(vijay.parent_detail())
print(supriya.parent_detail())

#Creating the second class
class Children:
    no_of_day=9

    #calling the constructor method
    def __init__(self,name,age,profession,language):
        self.name=name
        self.age=age
        self.profession=profession
        self.language=language

    # Now calling the printing method
    def child_detail(self):
        return f'Name is: {self.name} . Age is: {self.age} and Profession is: {self.profession} . Languages are {self.language}'

# Creating the instance or objects
neel=Children('Nell Rai',35,'Software Developer',['C and Python'])
akansha=Children('Akansha Rai',33,'Electrical Engineer',['Java'])

#printing the details of child class
print(neel.child_detail())
print(akansha.child_detail())


# Now Let's create the third class which is gonna be multiple inheritance
class cool_human(Parent,Children):
    sport='football'
    def human(self):
        print(self.sport)

astras=cool_human('Astras','3.5 billion','Ruler')
print(astras.parent_detail())
print(astras.human())


print(astras.no_of_day)