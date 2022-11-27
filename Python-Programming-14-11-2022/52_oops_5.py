# In this pyfile we learn about what is class method?

class Employee:
    no_of_leaves=7

    #calling constructor method
    def __init__(self,bname,bsalary,brole):
        self.name = bname
        self.salary = bsalary
        self.role = brole
    
    #creating the printing method
    def employee_detail(self):
        return f'Name is : {self.name} . Salary is : {self.salary} and Role is {self.role}'

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
#Creating the objects
vishnu=Employee('Vishnu Sharma',500000,'Instructor')
divya=Employee('Divya Nagpal',800000,'PR')

#Calling the objects information
print(vishnu.employee_detail())
print(divya.employee_detail())

#Now We Touch Our Main Topic Which Is Class Method. This topic start from line no 16


divya.change_leaves(45)
Employee.change_leaves(45)
print(divya.no_of_leaves) 
print(Employee.no_of_leaves) 

 



'''
So, what happen if you want to change the value of no_of_leaves through class Employee. But your wish is
not to change direct, so if you don't want to direct change the value of no_of_leaves , Here is 
the method in python which is @class method. Through this method you have to create a function and name
the function according to your convinience then use cls method which is nothing but class . 
'''
