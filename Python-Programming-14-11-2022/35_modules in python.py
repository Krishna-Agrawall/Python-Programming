'''
credit:w3school.com
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py:

Note: When using a function from a module, use the syntax: module_name.function_name.


'''
#Run1

# import mymodule   #importing this file from mymodule.py
#
# m=mymodule.human
# print(m)

'''
Re-naming a Module
You can create an alias when you import a module, by using the as keyword:

'''
#Run2
import mymodule as my
m=my.human['age']
print(m)

import random  #This is a module

#Run3
# def random_n():
#    w= random.randint(0,5)
#    return w
#
# print(random_n())

#Run4
# random_n=random.random()   *100
# print(random_n)



#Run5
# choice=['mars','venus','earth','jupiter','saturn','pluto']
# ran=random.choice(choice)
# print(ran)