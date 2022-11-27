# Run1

# def fun(n):
#     print(n,'Hello From Earth')  #Well this normal  function as you know
# fun('What"s up')



# Run 2

# g='This is global variable'    #This is a global variable and you can use this variable in any function
# def fun(n):
#     print(n,'Hello From Earth')
#     g='This is a local variable'      # This is local var you can use this onln on this function not outside the function.
#     m='This is another Local variable'
#
#     print(g)
#     print(m)
#
# fun('What"s up')
# print(g)    # This is will print3
#
# print(g) #Now,if you gonna think let's check the output by print(g) the variable is global or not -
#         # - but let me tell you , whatever time you type print(g) , it gonna print global variable -
#         # - not local variable , cause you are printing outside the function
#
# print(m)   #This is gonna send error you if you try this , for reason read 3 lines above in comment



# Run 3

'''
Now, if you want to change the value of global variable in function you cannot do. Let me show you
'''

# g=5  #Global variable
#
# def earthian(a):
#     print(a,'I am an Earthian')
#
#     g=4  # Local variable
#     h=2  # Local variable
#
#     ''' First let comment g=4 which is local variable , after commenting g=4 we are try to change the value of
#         g=5 which is global variable.let's do it '''
#
#     # g=g+5       #Changing the value of global variablee
#     # print(g,h)    #Run1
#
#     ''' When you run this program you can see that you cannot run g, because here in function  g is only
#         the read variable . But you can change the value of local variable let me show you first commet out line no 42.'''
#
#     g=g+4    #Changing the value of local variablee
#     print(g,h)  #Run2
#     '''As you see after running the program the value of local variable was changed.But at the same time you run the
#       program after changing the value of global variable it will give you the error. So, don't we never change the value
#       of global variable in function . The Answer is Yes, You Change the value of global variable by assigning global
#       keyword. Let Me show in next part of code .'''
#
# earthian('Dude')





#Run4
#
# g=8
# def pandora(b):
#     print(b,'Welcome To The Pandora')
#
#     global g
#
#     g=g+20  # Changing the value of global variable
#     print(g)
#
#
# pandora('Hello Sir,')




#Run 4

def krishna():
    g=34 # Local variable
    def aero():
        global g
        g=21
    print('Before Calling aero : ',g)
    aero()
    print('After Calling aero : ',g)

krishna()
print(g)


'''Now , if you are expecting that declare global keyword in aero function the value of g will be change, so 
   let me clear your doubt , the value of g would not be change, why not change because when declaring global keyword
    the global keword work is to find the real value of g outside the function, means let me give an example you see in 
    Run2,Run3,Run4 I was declaring global variable outside the function or before declaring any function, ok . now 
    the come back to the topic our global keyword can't find any global variable outside the function. So if you gonna
    think that i declare the g=4 in krishna()fuction then i declare global g , then now why the value don't change , so
    the reason was same as i say in above of the lines.It can't change the value of g, if it don't find outside declaring
    global variable. But as you can see After declaring the krishna function if i use print(g) the value of g would be
    change , why it change  because when you declare the global keyword then the global keyword go outside the function
    and it made a new global variable g=21. 
    So i hope you understand well if don't then visit youtube and search 
    code with harry  - Scope, Global Variables and Global Keyword | Python Tutorials For Absolute Beginners In Hindi #33.
    
    '''