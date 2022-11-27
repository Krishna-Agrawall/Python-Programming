# 0 1 1 2 3 5 8 13

# 0+0= 0+1=1     1+1=2     2+1=3    3+2=5    5+3=8   8+5=13

#Fibonacci series is nothing but sum of previous 2 number

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1

    else:
        return fib(n-1)+fib(n-2)
number=int(input('Enter the number : '))
print(fib(number))