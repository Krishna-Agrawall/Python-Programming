# list=['krishna','meet','anstor','kylian','ney']
# print(list)  #Run1



# for item in list:
#     print(item)  #Run2

list1 = [['krishna', 1], ['meet', 4], ['anstor', '8'], ['kylian', 12], ['ney', 16]]


# for item ,value in list1:
#      print(item,value)  #Run3

dict1 = dict(list1)
# print(dict1) #Run4

# for item,value in dict1:
#     print(item,value)  #Run4

#in line 18 and 19 when you run the program it will generate the error but if you don't want error you can use item function

# for item,value in dict1.items():
#     print(item,'and run is : ',value)  #Run5

# for item in dict1:
    # print(item)  #Run6  In this the key values print only




# Quiz

'''
You have to create a list and after creating the list we have to print only numbers which is greater then 6,
In list whatever things you can input whether it is string or int .
'''

list=[int,float,'jan',1,'feb',2,'june',6,'august',8,'sep',9,'october',10,'november',11,'december',12]

for items in list:
    if str(items).isnumeric() and items>6:
        print(items)












