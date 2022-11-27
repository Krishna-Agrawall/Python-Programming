'''
credit:w3school.com
The while Loop:
With the while loop we can execute a set of statements as long as a condition is true.
'''

#First Run this program uncomment it
# i=1
# while i<45:
#     i += 1
#
#     print(i)  #Run1


# Introduction of break and continue statement

# i=0
# while(True):
#     if i<5:
#         i+=1
#         continue
#
#     if i==45:
#         break
#     i+=1
#     print(i)


# Quiz
'''
Now, you have to made a program in which user input the number until he enter 100. when he enter above>100
you have to stop and print you have enter above the 100.
'''




while(True):
    i=int(input('Enter number : '))
    if i>99:
        print('You type 100 ,program can display upto 99')
        break


    print('You Enter : ',i)




