# In this pyfile we will leaarn about what is dunder method and overlaading
''' 
The Method which start from double underscore __ and ends with double underscore __ , this type
of method is also called dunder __init__. And dunder __init__ is a special method. Why this is special
method , because it is constructor. Whatever arguments you give it will run, when the object was made. 

'''

'''
Now, let we talk about what is operator overloading? Belive that you create two objects which is:
emp1=Employee('Krishna Agrawal',5000,'Beginner')
emp2=Employee('Astris',400000,'Scientist')

Now,if you print(emp1+emp2) before calling dunder or you comment the dunder function, it will give you
the error, because the console asks what you want to do wheter you want to match the salary or weight,or 
what , so console does'nt understand what you want to say.  So what happens now, there is if you want
to joint the two objects , then it run the dunder add method in behind the scene. And Now When it join
so  the dunder is helping us from operating overloading.

'''

# Now let's move to another two dunder methods.

'''
If you print , print(emp1)  , Then your output is gonna show your object store location. Now, If you 
want to see the output beautiful , means you don't want to see the object store number , then what we
did we make one method which is repr method. then after creating it when you return self.employee_detail
. Now what self.employee_detail do it return the f string, which is :
 f'Name is: {self.name}. Salary is: {self.salary} and Profession is: {self.profession}'.

 The actual syntax of repr method is :
 return f"Employee('{self.name}','{self.salary}','{self.profession}')". So, we are using repr
 this way. 
 
 And For defining the objects means what is object to summarize this we are using str method.






'''

# Create one class
class Employee:
    no_of_leave=23
    # calling the constructor method
    def __init__(self,name,salary,profession):
        self.name=name
        self.salary=salary
        self.profession=profession

    # calling the printing method
    def employee_detail(self):
        return f'Name is: {self.name}. Salary is: {self.salary} and Profession is: {self.profession}'

    # calling the class method
    @classmethod
    def change_leave(cls,new_leave):
        cls.no_of_leave=new_leave

    # creating the dunder method for add the salary of 2 employees
    def __add__(self,other):        # This is dunder method
        return self.salary+other.salary

    # creating the dunder method for divide the salary of 2 employess
    def __truediv__(self,other):
        return self.salary/other.salary
 
    # creating the dunder method for multiple the salary of 2 employess
    def __mul__(self,other):
        return self.salary*other.salary

    # creating the dunder method for checking the differnce of 2 employess
    def __ne__(self,other):
        return self.salary!=other.salary

    # creating the dunder method for checking  the Equality of 2 employess
    def __eq__(self,other):
        return self.salary==other.salary
 
   # creating the repr method
    def __repr__(self):
        # return  f'Name is: {self.name}. Salary is: {self.salary} and Profession is: {self.profession}'
        return f"Employee('{self.name}','{self.salary}','{self.profession}')"

    # creating the str method
    # def __str__(self):
    #     return  f'Name is: {self.name}. Salary is: {self.salary} and Profession is: {self.profession}'


    # creating the objects or instance
emp1=Employee('Krishna Agrawal',5000,'Beginner')
emp2=Employee('Astris',400000,'Scientist')

# printing the dunder method + detail of employee
# print(emp1+emp2)       #Run1
# print(emp2/emp1)       #Run2
# print(emp1*emp2)       #Run3
# print(emp1!=emp2)      #Run4
# print(emp1==emp2)      #Run4

print(emp1)  #Run5
'''Run5 This will run str only not repr method , for run the repr method you have to write
  print(repr(emp1)). And if you commentd str method it will  print : repr syntax.
  not str because unavailabile of str, when you call str method then it gonna print str. 
'''