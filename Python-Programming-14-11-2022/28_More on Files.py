# f=open('universe1.txt')
# print(f.tell())             #This f.tell function tell me that in which character line i am
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()


f=open('universe1.txt')
# print(f.seek(1))
print(f.readline())
print(f.readline())
print(f.seek(34))              # This f.seek function takes me on line   whatever character you input to through end line
print(f.readline())
f.close()