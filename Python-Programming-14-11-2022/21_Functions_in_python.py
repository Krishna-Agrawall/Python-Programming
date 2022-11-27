'''credit:w3school.com
Python Functions:
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
'''

# a=2
# b=4
# c=sum((a,b))  #This is known as built-in function
# print(c)  #Run1



def func1():
    print('Hello from func1') #Run2           # This is known as user-defined functions
func1()


def func2(a,b):
    print('The sum of a+b is ',a+b) #Run3
func2(5,6)



'''
Arguments:

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
'''

def func3(a,b):
    '''This is a function which will calculate the average of 2 numbers'''     #<-- Whatever We write in ''' '''' in inside the function it is known as docstring.
    #docstring means given the information to the user or you in the future that what the function exactly means.

    average=(a+b)/2
    # print('The average of a and b is ', (a+b)/2) #Run4
    return average

a=func3(7,5)
print('The average of a and b is ', a)
print(func3.__doc__)



'''
So, let's see what exactly happened in func3. First of all your function ignores what you write in def . it directly
come in a=func3 (7,5) it comes to func3 . now it comes in func3 . after coming in fuc3 it takes average of a+b/2
means it get enter with 7 and 5.now then it find average which is 6 and then return the average which is 6.now your function
again come in a=func3(7,5) and replace func3(7,5) to 6 then line 22 is equal to a=6, next it print it.
'''





'''



Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
'''








