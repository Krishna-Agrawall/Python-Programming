'''
What is a Python decorator?


Decorators provide a simple syntax for calling higher-order functions. By definition, a decorator 
is a function that takes another function and extends the behavior of the latter function without 
explicitly modifying it.
'''

# Run1 Line 12 to 16
 
# def fun1():
#     print('Hello Universe')
# fun2=fun1
# del(fun1)
# fun2()


# Run2 Line 21 to 27

# def funret(a):
#     if a==0:
#         return print
#     if a==1:
#         return int #or you can return sum also 
# f=funret(1)
# print(f)


# Run3 Line 32 to 35

# def executor(func):
#     func('Interstellar1')

# executor(print)

'''
So, Here we understand that we can put function in function as an argument and we can return function,
with function.
'''

#Run4 Line 46 to 53

# Now let's move on to our main topic which is decorator

def dec(func1):  #Here we creating one function named it dec and inside that we are taking func1 of function
                 # as argument
    
    def now_execute():  # Inside dec function we are creating one more function named now_execute
        print('Executing Now')
        func1()
        print('Executed')
    return now_execute


'''
Now what we did in those 44 to 51 line let's understand it  Humne ek dec1 naam ka function banaya
es func1 ko agar hum koi bhi function denge to  usse pehle Line 48 ka print statement Executing Now
print ho jayega  aur uske baad line 50 ka print statement print('Executed') ho jayega. Aur Abhi hum print
kar rhe hai par kuch bhi ho sakta hai . Aap sum de sakte ho calculations kar sakte ho anything you want 
to do you can access it.  Lekin hum isse pehle aur iske badd koi kaam kar rhe ho , to hum isse remotely 
connect kar sakte ho kisi server ko, aur bhi kuch kar sakte , ye aap pe depend kar ta hai. Now, what if 
we made another function so let's see it.
'''



@dec     #Runline88 First ,then use this @dec function , because both are same
def world():
    print('This world is so big and beautiful')

# world()    #Run This Statemnt First Then Execute Next Statment

'''
Now , Here what we did we create a simple world function and inside we give the print statement
, then we call it and it print the statement that you write in in line 70 print statement.

Now, What happen if we change world . And After changing the world we use dec function  means

--> world = dec(world) <--

Now, the world is dec of world not only world function. The world is now what dec return, and what
dec return it return now_execute. and after this if we call world function, it can print
 Executing now, This world is so big and beautiful , Executed.

'''

# world = dec(world)     # First run this line88, then use @ notation . Because both methods are same
world()

# Now, This Whole Process Known As Decorators. If you still don't understand it read again or
#  go to code with harry youtube channel and search python tutorial decorators. I am learning 
# whole from his youtube channel


'''
If you don't want to line 88 world= dec(world) , There is shortcut trick available in python known as @
notation, You have to write @ and function name which you have to pass to another function . ex
@dec. @dec you have to put before declaring new function . and our new function is in line 69 def world()
so you have to @dec in line 68.
'''


'''
Now, after whole creating this decorators , you might think what is the use of it, It's use is , suppose
you have created one function,  and now the function that you just created you want create 10 more function
and you want to use first function in those 10 function so, here is the method which is decorator.
                                    OR

Decorators ka use kya hai, agar muje 1 he kaam 10 function ke saath karna to mai uska ek decorator 
bana lunga yaani ek blueprint bana lunga aur mai usse kuch bhi naam se call karke use karunga. usse kya
hoga hume kaafi aasani hogi.
'''