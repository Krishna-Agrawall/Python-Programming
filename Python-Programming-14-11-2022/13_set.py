'''
credit:w3school.com

Set:
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple,
 and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.
'''

s=set()
# print(type(s))  #Run1

set_list = set([1, 2, 3, 4, 5])
# print(type(set_list))  #Run2
# print(set_list)         #Run3

s.add(1)
# print(s) #Run4

s.add(1)
# print(s)   #Run5   It does not add 1 because set only take unique values only

s.add(2)
# print(s) #Run6

s.add(3)
# print(s) #Run7


'''

Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
'''


a={'krishna','agrawal','krishna','singhal','apple',4,2,4,2,1}
# print(a)  #Run8

b={'icecream','chocolate','cherry','rasmalai','icecream','mango','chocolate'}
# print(len(b))   #Run9
# print(b)        #Run9
# print(type(b))  #Run9

b.remove('icecream')
print(b)      #Run10
