# In this pyfile we learn about what is constructor?

class Employee:
    def __init__(self,aname,asalary,arole):            # This method is known as constructor method
        self.name=aname
        self.salary=asalary
        self.role=arole
        
    def employee_details(self):
        return f'Name is {self.name} . Salary is {self.salary} And Role is {self.role}' # type: ignore

magnus = Employee('Magnus Carlson',30000,'Student')
lionel = Employee('Lionel Messi',500000,'CEO')




# magnus.name='Magnus Carlson'
# magnus.salary='300000'
# magnus.role='Student'

# magnus.name='Lionel Messi'
# magnus.salary=5000000
# magnus.role='CEO'

'''
This is also very boring to write same thing again and again , so if you dont wanna write this type of 
line again and again you can implement constructor method . Which you can define by __init__()
function.  
'''

print(lionel.employee_details())
print(magnus.employee_details())