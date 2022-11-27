'''
credit-w3school
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

List always made in [] square brackets.
'''


list = ['Air', 'Water', 'Oxygen', 'Fire', 1, 2, 3,
        4, 5]

# print(list)  #Run1

# print(list[2], [3], [6])      #Run2


list1 = [67, 34, 98, 99, 34, 28]
# list1.sort()     #Run3
# list1.reverse()  #Run4
# print(list1)     #Run5

# Now we use slicing here so let's do in next lines

# print(list1[:4])    #Run6
# print(list1[1:3])   #Run7
# print(list1[::1])   #Run8   This is also known as extended slicing
# print(list1[::2])   #Run9
# print(list1[1::2])  #Run10
# print(list1[1:5:2]) #Run11


# Now we gonna print original list to see there are any difference or not

# print(list1)     #Run12


#Now if you want to find maximum , minimum and length of your list1 here is the code in next lines

# print(max(list1))  #Run13
# print(min(list1))  #Run14
# print(len(list1))  #Run15


#                                        Append

'''Now if you had wish you want to an number in last . So in python there is a method which is known as append.
   so append will add the number you want in last. Let me give you example in next lines code
'''

# print(list1)       #Run16   First we print our list to show which numbers are there in list1

#As you can see our last number is 28 . Now if you want to add 56 in last you can add how , let me code it


list1.append(56)
# print(list1)      #Run17


#If you want to append more numbers you can.

list1.append(42)
list1.append(17)
list1.append(92)

# print(list1)   #Run18


#
list2 = []
list2.append(34)
list2.append(69)
list2.append(10)

# print(list2)  #Run19

#                                           Insert
''' Now in insert function you can add number in any of index . In append you cannot do this because append 
only add number in last but insert not . Let show an example '''

list3 = [78, 23, 45, 69, 81, 22]

list3.insert(2,44)
list3.insert(5,70)
# print(list3)  #Run20


#                                           Remove
# Now if you want to remove any number there is a function known as remove it will remove the number .

list4 = [45, 67, 89, 90, 12]
list4.remove(67)
# print(list4)   #Run21


#                                           pop
''' If you want to remove the last number of your list there is a function in python known as pop . It will delete the
last number. Let's us show an example'''

list5 = [34, 23, 67, 89, 42, 12, 56, 78, 43]
list5.pop()
# print(list5)   #Run22

