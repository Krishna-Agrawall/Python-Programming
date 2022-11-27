
#Run1

#Normal function to print the name
# def func(a,b,c):
#     print(a,b,c)
#
# func('Nehal','Mehal','Keyur')


'''
Now Suppose I have many name to write in the program , and i don't want to write arguments again and again like a,b,c
. So the solution is arguments . You can use *arguments function to write unlimited names or arguments. Let me show you
with an example
'''

#Run2
#
# def funarg(*args):
#     for item in args:
#         print(type(item))
#         print(item)
#
# tup=('Akshay','Bob','Christ')
# funarg(*tup)      #Tup means tuple


#Run3

# def arg(normal,*args):
#
#     for i in  args:
#         print(i)
#
# lst=['Danny','Elish','Franc']
# n=('This is the honarary special mention names:')
# print(n)
# arg(n,*lst)




#Run4

def keyarg(normal,*args,**kwargs):
    for i in (args):
        print(i,'\n')

    print('\nAfter Introducing The Students, Now I Would Like To Introduce ,Some Names With Their Current Profession :\n')
    for key,value in kwargs.items():
        print(f'{key} is a {value}')


list=['Harry','Isha','Jack']   #This is *args

k=('I am a normal argument and the student names are : ')   #This is for normal argument
print(k)

kw={'krishna':'Learning Python','Lemano':'Software engineer','Melody':'Scientist'}  # This is for keyword arguments


keyarg(k,*list,**kw)


# This is the order you have to follow normal argument, argument, keyword argument. You can give any to your arguments