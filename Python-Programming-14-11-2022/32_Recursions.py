'''What is the Meaning Of Recusions?
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result.

 or

Recursions ka matlab hota hai functions ke andar functions ko use karn.
'''


# n! This is factorial sign in mathematics if you know.

# n! = n*n-1 * n-2 * n-3.....1
#n! = n*(n-1)!

def factorial_iterative(n):
    ''':param n: Integer
       :return: n * n-1 * n-2 * n-3 ....1
       ex: 5 , 5* 5-1=4  * 5-2=3 * 5-3=2 * 5-4=1
       '''
    fact=1
    for i in range(n):
        fact=fact * (i+1)
    return fact
number=int(input('Enter The Number : '))


factorial_iterative(number)




#For Recursive
def factorial_recursive(n):
    ''':param n: Integer
           :return: n * n-1 * n-2 * n-3 ....1
           ex: 5 , 5* 5-1=4  * 5-2=3 * 5-3=2 * 5-4=1
           '''

    if n==1 or n==0:
        return 1

    else:
        return n*factorial_recursive(n-1)
number=int(input('Enter number : '))

print('Factorial using recursive method',factorial_recursive(number))
print('Factorial using iterative method',factorial_iterative(number))


