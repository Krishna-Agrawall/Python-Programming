'''
credit:w3school.com
Python Conditions and If statements:
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
 Other programming languages often use curly-brackets for this purpose.
'''



a=34
b=45
# c=int(input('Enter any number : '))

# if b>c:
#     print(' b is greater then c')
# elif b==c:
#     print('Both are equal')
# else:
#     print(' c is greater then b')


#First Run line 3 to 10 then run next part of lines

a=[23,45,78,90,65,35,61]
# print(22 in a)
# if 22 in a:
#     print('yes')
# else:
#     print('no')


#After running line 3 to 10 run 16 to 19 then comment the lines and run the next part of lines

# print(22 not in a)
# if 22 not in a:
#     print('yes')
# else:
#     print('no')



'''
Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
'''
c=23
d=89

# print('The value of c is greater then d') if c>d else print('The value of d is greatern then c')  #Run1
# This technique is known as Ternary Operators, or Conditional Expressions.

'''
And:
The and keyword is a logical operator, and is used to combine conditional statements:
'''
e=65
f=12
g=90

# if e>f and g>f:
#     print('Both condtions are true')
# else:
#     print('Conditions are fail')
#
#
''' 
Or:
The or keyword is a logical operator, and is used to combine conditional statements:
'''

h=43
i=21
j=98

# if h>i or h>j:
#     print('Atleast one condition is true')
#
# else:
#     print('Both conditions are false')


'''
Nested If:
You can have if statements inside if statements, this is called nested if statements.
'''
k=78
# if k>10:
#     print('Above 10')
#     if k>20:
#       print('Above 20')
# else:
#     print('Below 10')



'''
The pass Statement:
if statements cannot be empty, but if you for some reason have an if statement with no content,
 put in the pass statement to avoid getting an error.
'''

# l=20
# m=10
# if l>m:
#     pass


#Quiz

'''The quiz is that you have to ask user to input his/her ageif your age is above 18 you have to print 
you can drive and if your age is not above 18you have to print your age is not 18 so you cannot drive 
and if your age is 18 you have to print we cannot decide to give you the permission to drive or not 
so wait some time.'''


age=int(input('Enter your age : '))
if age>18:
    print('Congratulationis! Your are able to drive the car')
elif age == 18:
    print('Decision Pending Please Wait Some Time')
else:
    print('You Cannot Drive')





