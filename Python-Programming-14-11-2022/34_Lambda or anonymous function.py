'''
credit:w3school

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:
'''


#This is normal function to print sum of a and b

# def add(a,b):
#     return(a+b)
# c=add(2,2)
# print('The sum of a + b is = ',c)

#This is lambda function to print sum of a and b

add=lambda a,b:a+b
print('The sum of a+b is = ',add(1022,4594))
print(type(add))


sub=lambda a,b:a-b
print('The sub of a-b is = ',sub(78,44))
print(type(sub))


#Sorting Example


#This is normal function using sorting
def a_first(a):
    return a[0]




# a=[[4,56],[9,23],[1,2]]
# a.sort(key=a_first)
# print(a)


#This is lambda or anonymous function using sorting

a=[[8,32],[2,67],[6,14]]
a.sort(key=lambda a:a[0])
print(a)
