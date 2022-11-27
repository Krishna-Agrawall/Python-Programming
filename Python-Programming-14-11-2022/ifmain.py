def func(capital):
    return f'The capital of India is {capital}'

def func1(a,b):
    return a+b+3


#Run1 line 9 to 12

# f=func('Delhi')
# print(f)
# f1=func1(6,6)
# print(f'The sum of a+b is : {f1} ')



# After running the Run1 Now Let run the Run2


print('And the name is',__name__)       # Here's in output the name comes main but if any one  import this file , the name would be your file name.
if __name__ == '__main__':
    f=func('Delhi')
    print(f)
    f1=func1(6,6)
    print(f'The sum of a+b is : {f1} ')