#1 method
# f=open('universe1.txt')
# print(f.readlines())
# f.close()


#2 method
with open('universe1.txt') as f:
    character=f.readlines()
    print(character)

#Both methods are correct