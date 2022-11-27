# In this pyfile we learn about what is instance and class variable?

class Employee:
    no_of_leaves=10
    def employee_details(self):

        return f'Name is {self.name}. Salary is {self.salary} and Role is {self.role}'  # type: ignore

anus=Employee()
victoria=Employee()

#Class instance of anus
anus.name=('Anus Saxphire')  # type: ignore
anus.salary=(10000)  # type: ignore
anus.role=('Data-Scientist')  # type: ignore

#Class instance of victoria
victoria.name=('Victoria Pelzen')  # type: ignore
victoria.salary=(70000)  # type: ignore
victoria.role=('Data-Analyst')  # type: ignore


#Printing the employee details
print(victoria.employee_details())
print(anus.employee_details())

# Now Let's Use Class Variable 
print(anus.no_of_leaves) 

'''This is the work of self program if we don't execute self instance you have to write
 print(victoria.name) then print(victoria.salary)+ print(victoria.role) and you have to write same
 for anus also . Suppose you have record of 50 students , so can you write this print(victoria.name)
 or anything of student details 50 or more time. Well Now No, You cannot write 50 or more time 
 print statement , You just have to call self method then see how you work gonna easy. '''



