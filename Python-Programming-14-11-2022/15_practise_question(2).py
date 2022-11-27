a=int(input('Enter Number : '))

b=int(input('Enter Number : '))

print('Press 1 For Addition')
print('Press 2 For Subtraction')
print('Press 3 For Multiplication')
print('Press 4 For Division')

user = int(input('Enter your choice from above : '))

if user==1:
    if a == 56 and b == 7:
        print('The addition of a and b is = 77')
    else:
      c=a+b
      print('The value of a + b is = ',c)


elif user==2:
    c=a-b
    print('The value of a - b is = ', c)

elif user==3:
    if a==45 and b==3:
        print('The multiplication of a *b is = 555')
    else:
      c=a*b
      print('The multiplication of a * b is = ', c)

else:
    if a==56 and b==4:
        print('The division of a * b is = 4')
    else:
      c=a*b
      print('The division of a / b is = ', c)




