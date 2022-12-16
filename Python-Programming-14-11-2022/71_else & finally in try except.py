# Run 1 Line 2 to 7
# try:
#     f=open('Ed.txt')
# except Exception as e:
#     print(e)

# print("Important Stuff")

# You know that if you don't put try exception then it does not gonna print important stuff statemetn


# Run 1 Line 2 to 7
f1=open('universe.txt')
try:
    f=open('universe1.txt')
except Exception as e:
    print(e)
else:
    print('This will run only if except is not running')
finally:
    print('Run this anyway')
    # f.close()    
    f1.close()
print("Important Stuff")