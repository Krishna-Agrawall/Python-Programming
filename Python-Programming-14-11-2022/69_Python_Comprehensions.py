# l=[]
# for i in range(100):
#     if i%3==0:
#         l.append(i)
# print(l)

'''
Now To Complete this set of code you have write about 5 lines , But What if
i say that you can writer this set of in just 1 line. Yes, you can with the 
help of compreshensions. Let we show you an example
'''

# l=[i for i in range(100) if i % 3 == 0] # This method is known as list comprehensions
# print(l)


'''
You can access comprehension with dictionary also. From line 20 to 23
'''
# dict={i: f'item {i}'  for i in range(5)}
# # print(dict) #Run1
# dict1={key:value for value,key in dict.items()}
# print(dict1,'\n',dict) #Run2


# You can access compreshension with set also. From line 28 to 30

# seet={dresses for dresses in['dress1','dress2','dress3','dress1','dress1','dress2']}
# print(seet) #Run3
# print(type(seet)) #Run4


# You can access comprehension with generators also. From line 35 to 

evens=(e for e in range(100) if e%2==0)
print(type(evens)) #Run5
 
for i in evens:
    print(i) #Run6
