# f=open('universe.txt')
# content=f.read()
# print(content)  #Run1
# f.close()


# Now we put mode on this files

# f=open('universe.txt','r')  #We open this file in read mode
# content=f.read()
# print(content) #Run2
# f.close()


# f=open('universe.txt','rb')  #We open this file in read+binary mode
# content=f.read()
# print(content) #Run3
# f.close()


# f=open('universe.txt','rt') #We open this file in read+text mode  and by the way rt is a default mode
# content=f.read(3)
# print(content) #Run4
# # f.close()


# content=f.read(3)
# print(content) #Run5
# f.close()



# f=open('universe.txt','rt') #We open this file in read+text mode  and by the way rt is a default mode
#
# for line in f:
#     print(line,end='')  #Run6
# f.close()



# f=open('universe.txt','rt') #We open this file in read+text mode  and by the way rt is a default mode
#
# print(f.readline()) #Run7
# print(f.readline()) #Run8
# print(f.readline()) #Run9
# f.close()


f=open('universe.txt','rt') #We open this file in read+text mode  and by the way rt is a default mode
print(f.readlines())#Run10
f.close()

