#credit-w3school.com

'''

Variables
Variables are containers for storing data values.


Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
'''

# Example

# a=4
# b=a
# print(a)
# print(b)

# Casting
'''If you want to specify the data type of a variable, this can be done with casting.'''

# Example

# q = str('Rohit')  # q will be 'Rohit' This is string data type
# x = str(3)    # x will be '3'  and this is string data type
# y = int(3)    # y will be 3 This is integer data type
# z = float(3)  # z will be 3.0  This is float data type
#
# print(type(q))
# print(type(x))
# print(type(y))
# print(type(z))


#

var1 = 'Amit '
var2 = 'Pawar'
var3 = '45'
var4 = '2'
# print(var1+var2)

#print(var1+var3) # This will give you the error but if you put quotes '45' the error would gone because you made it str

# print(int(var3)+int(var4))

'''Now , if you put quotes in var3 and var4 it will concatenate . It will not give you the addition of 45+2 . 
   Concatenate means The two values combine ex-  we write '45' in var3 and '2' in var 4 and now if you put plus sign in 
   between var3+var4 the output will be 452. So. This is known as concatenation. If you want to remove string datatype
     and want to insert integer data type you have to write    print(int(var3)+int(var4)). So next time your output 
     will be 47. And This Method Known as type casting'''





'''Now you want to print  hello world ten times here is the code'''

# print(10*'Hello World\n')

# print(100* int(var3) + int(var4))
print(100*str(int(var3) + int(var4)))