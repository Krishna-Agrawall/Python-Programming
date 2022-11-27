'''
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
'''


#Example:

# def myfunc(*kids):
#     print('The youngest kid is',kids[2])  #Run1
# myfunc('nihal','akansha','supriya','shav')



'''
Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
'''


#Example:

# def func5(kid3,kid1,kid2):
#     print('The eldest child is',kid2)  #Run2
#
# func5(kid3='Mehal',kid2='Raj',kid1='Manas')





#Another Example:

# def scientist(science1,science2,science3):
#     print('The Inventor of Theory of relativity is',science1)  #Run3
#
# scientist(science2='Galilio Galleli',science1='Alber Einstein',science3='Leonardo da vinci')


'''
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
'''
#Example:

# def func6 (**kid) :
#     print('His lname name is ',kid['lname'])   #Run4
#
# func6(fname='Jack',lname='Grealish')



'''
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
'''
#Example:

# def func7(country='india'):
#     print('I am from',country)   #Run5
# func7('Norway')
# func7()
# func7('Australia')
# func7()



#Another Example:

def func7(food='dal rice'):
     print('My favourite food item is',food)
func7('Pizza')
func7()
func7('Roti+Paneer')




