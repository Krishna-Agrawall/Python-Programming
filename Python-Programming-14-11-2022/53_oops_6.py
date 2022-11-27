#In this pyfile we learn about What is alternative method as class method

class Employee:

    no_of_leaves=12

    #Calling a constructor method
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    #creating the printing method
    def employee_details(self):
        return f'Name is: {self.name} . Salary is: {self.salary} and Role is {self.role}'

    
    #creating the class method
    @classmethod
    def change_leave(cls,newleave):
        cls.no_of_leaves=newleave

    #creating the alterative method using class method
    @classmethod
    def from_dash(cls,string):
        params=string.split('-')
        return cls(params[0],params[1],params[2])
   
# Now Let's Create The Objects
sudhansu=Employee('Sudhansu Verma',15000,'Beginner')
payal=Employee('Payal Rai',20000,'Senior Employee')

# Using the alternative method
shasan=Employee.from_dash('Shasan Yagnik-300000-Head of Department')

# Printing the employee details
print(sudhansu.employee_details())
print(payal.employee_details())
print(shasan.employee_details())

#Let use the leave function one by one
# print(Employee.no_of_leaves)  #Run1
# print(sudhansu.no_of_leaves)  #Run2
# print(payal.no_of_leaves)     #Run3
# print(shasan.no_of_leaves)    #Run4

#Let's change the no of leaves
Employee.change_leave(14)

print(Employee.no_of_leaves)   #Run5
print(sudhansu.no_of_leaves)   #Run6
print(payal.no_of_leaves)      #Run7
print(shasan.no_of_leaves)     #Run8