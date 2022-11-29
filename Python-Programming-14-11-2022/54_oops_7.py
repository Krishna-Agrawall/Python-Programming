#In this pyfile we learn about What is static method 

class Employee:
    no_of_leaves=14
    # Creating the constructor
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    # Creating the printing method
    def employee_detail(self):
        return f'Name is : {self.name} . Salary: {self.salary} and Role: {self.role}'

    # Creating the class method
    @classmethod
    def change(cls,newleave):
        cls.no_of_leaves=newleave

    # Creating the alternative method
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split('-'))
   
   # Creating the static method
    @staticmethod
    def static(string):
         print('Hello Your Name is '+string)

#Creating the instance
pulkit=Employee.from_dash('Pulkit Verma-25000-Begineer')
neha=Employee.from_dash('Neha Sharma-25000-Begineer')

#Changing the value of no_of _leaves
Employee.change(34)

#Now printing the detail of employee and no of leaves
print(pulkit.employee_detail())
print(pulkit.no_of_leaves)

#using the static method
print(pulkit.static('Leo Messi'))
