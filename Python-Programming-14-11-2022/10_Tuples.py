'''
credit-w3school
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set,
and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''

#Mutable - can change , ex-lists
#Immutable - cannot change , ex=tuples

Number = [12, 34, 56]  # This is list

# print(Number) #Run1
Number[1] = 13
# print(Number)#Run2



'''Now you can see , putting list, i can change the number if i want to. But things are gonna change in tupple we cannot 
   change the number .'''

Number1 = (12, 34, 56) # This is Tupple
# print(Number1)#Run3        First,run this line no27,28 then run line no 30,31

# Number1[2] = 35
# print(Number1) #Run4


''' As we can see when we run the tupple program  it will give the TypeError which is :
    'tuple' object does not support item assignment'''




# swapping

a=5
b=2

# temp = a
# a = b
# b = temp
# print(a, b) #Run5

# Well,as i write in line 45 to 47 this is old method to do swapping there is new method in python to do swapping lets see

a, b = b, a                # This is new method to do swapping in python
print(a,b)   #Run6
