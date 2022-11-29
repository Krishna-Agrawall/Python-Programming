# In This Pyfile We Learn About What is Super() and Overriding in Classes

#creating A Class
class A:
    class_variable_a='I am a class variable in Class A'

    #Creating constructor method in class A
    def __init__(self):
        self.class_var_a='I am inside in class A constructor '
        # self.class_variable_a='Instance Variable in class A'   # This is instance variable

class B(A):
    class_var_a='I am a class variable in Class B'

     #Creating constructor method in class B 
    def __init__(self):         # And Now we are doing overriding. It is nothing but it will print this detail class b
        
        self.class_var_a='I am inside in class B constructor '
        self.class_variable_a='Instance Variable in class B' # If we comment it , then it will 

# Creating the instance variable or objcets
a=A()
b=B()

#Printing the detail
print(b.class_variable_a)

