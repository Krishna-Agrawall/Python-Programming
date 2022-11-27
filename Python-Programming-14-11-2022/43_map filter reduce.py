number=['23','12','89','45']


#Run1 line 6 to 10

# for i in range(len(number)):
#     number[i]=int(number[i])
#
# number=number[2]+1
# print(number)


#Run2  line 15 to 19

# number1=list(map(int,number))
# number2=number1[2]+1
# # print(number1)
# print(number2)
# print(map(int,number1))



#Run3 Line 27 to 33

#Creating a norma function

# def square(a):
#     return a*a
#
# num=[2,3,4,5,6,7,8,9]
#
# numbers=list(map(square,num))
# print(numbers)


#Run4 Line 40 to 45

# Now Try The Square Function With Lambda

# square=lambda a : a*a
#
# num=[1,2,3,4,5,6,7,8,9,10]
#
# num1=list(map(square,num))
# print(num1)



#Run5 Line 51 to 57

# Now There Is Another Method To Use Lambda Fuction Let's See It


# num=[1,3,5,7,9,11,13]
#
# num1=list(map(lambda a :a*a, num))
# print(num1)


#Run6 Line 63 to 73


# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func=[square,cube]
#
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)



# Now we learn about filter function

#Run7 Line 81 to 87

# l=[3,67,44,89,21,78,50]
#
# def is_greater_50(num):
#     return num>50
#
# val=list(filter(is_greater_50,l))
# print(val)



# Now we learn about reduce function

#Run8 Line 97 to 101

# Well, this is  the normal method to add the numbers

# l=[1,2,3,4]
# num=0
# for i in l:
#     num=num+i
# print(num)


#Run9 Line 110 to 114

from functools import reduce

# Well, this is the new method to add the numbers using reduce

l=[1,2,3,4]
val=reduce(lambda x,y:x+y,l)
print(val)

