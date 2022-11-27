'''credit-w3school.com
Dictionary:
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

Dictionary Items:
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

key:value pairs means that key is word and value is a meaning . Let me give you an example

key                 value
Legitimate:    conforming to the law or to rules.


Now Legitimate is a key and conforming to the law or to rules is a value.

'''




d = {}
print(type(d))  #Run1

d1 = {'Ankit':'Cricket','Bobby':'Football','Chris':'Tennis' ,
      'Rohan':{'B':'Brown Bred','L':'Dal-Rice','Dinner':'Roti with bhindi'}}
# print(d1['Ankit'])  #Run2

print(d1['Rohan']['Dinner'])   #Run3 We can create dictionary in dictionary

d1['Dineshji']='Badminton'
d1['Eouyang']='Basketball'
print(d1) #Run3




# If i want to delete any name in the dictionary i or you can use del function

del d1['Eouyang']
# print(d1) #Run4

# Now we are gonna use copy function in dictionary

# d2=d1
# del d2['Dineshji']
# print(d1) #Run5

'''Now , let's see what we do exactly in line 50to53 we create a variable name d2 ok. now we put the value d1
  in d2 .  Next we del dineshji name in d2 , and if we print d1 we can see name dineshji was also deleted in d1. 
  so if you don't to delete the name you can use copy function. Again explanation so d3 is a pointer which is pointing
   to d2 and d2 is also a pointer which is pointing itself. Now d3 don't create a new dictinary  . d3 dictionary reference
   d2. so if i remove dineshji name in d2 the same name also remove from d1'''


d2=d1.copy()
del d2['Dineshji']
# print(d1) #Run6
# print(d2)  #Run7

#New Functions

# d2.get('Rohan')  #Run8

d2.update({'Meet':'Rugby'})
# print(d2)#Run9


# print(d2.keys())  #Run10
print(d2.items())  #Run11