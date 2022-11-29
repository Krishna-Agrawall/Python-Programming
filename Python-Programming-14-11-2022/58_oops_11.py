#In this pyfile we learn about What is public,private and protected

#public -> Anyone can access the variable or anything you have created

#private -> Only I have right to access it or not anyone else.

#protected -> You want the variables are come in my child class but other environment can't access it. 
# only sub sub classes access it..


#Let's create the class
class Employee:


    no_of_leave = 4  # This no_of_leaves is public variable
    var = 5          # This is also public variable



    #If you wanted to protect the variable, So before giving any variable name put underscore(_) first.ex- _christ
    _protect=2       # This is protect method , and you can easily print this.



    #Now, If you want to private any variable , So you can put double-underscore(__) before giving any variable name.
    __private=9   #This is private variable , and you cannot access it outside the class.



    # creating the constructor method
    def __init__(self,name,salary,profession):
        self.name=name
        self.salary=salary
        self.profession=profession

    # creating the printing method
    def employee_detail(self):
        return f'Name is:{self.name}. Salary is:{self.salary} And Profession is: {self.profession}'

    #creating the class method to change the leave
    @classmethod
    def change_leave(cls,new_leave):
        cls.no_of_leave=new_leave

    #creating the alternative method
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))

    #creating the static method
    @staticmethod
    def static(string):
        print('Whoops! There is an error do you have error in your program - '+string)


#creating the instance
alex=Employee.from_dash('Alex Roy-50000-Full Stack Developer')
jack=Employee.from_dash('Jack Rowling-500000-Data Scientist')
ross=Employee.from_dash('Ross Kane-25000-Programmer')
peter=Employee.from_dash('Peter Maguire-600000-Android Developer')

#printing the detail of employee
print(alex.employee_detail())
print(jack.employee_detail())
print(ross.employee_detail())
print(peter.employee_detail())

# Changing the no of leave and use of public private and protected
Employee.change_leave(34)

print(alex.no_of_leave) # This is public variable

print(jack.var) # This is also public variable

print(ross._protect)  #This is protected variable

# print(peter.__private)  # This is private variable . 
''' 
If you run line 77 it will give you the error. Now the variable is not beccme the private now, Here
Python Done the 'Name-Mangling'. What is Name - Mangling? Name - Mangling means you cannot access __private
variable directly. If you want to access the private variable you have to write -> 
print(peter._Employee__private). So whole this method known as Name-Mangling

'''

print(peter._Employee__private) # type: ignore #This is private variable

#using the staticmethod
print(jack.static('No'))

