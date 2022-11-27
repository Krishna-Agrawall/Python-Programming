print('You have to 5 rows and on this 5 row there are 1 are row star 2 row star and so on there  \n')
b=int(input('Enter 0 For Straight Or Enter 1 For Reverse : '))

n=int(input('Enter which row do you want print : '))


if n==1 and b==0:

    print('*')

elif n==2 and b==0:
   print('*')
   print('**')
elif n==3 and b==0:
    print('*')
    print('**')
    print('***')

elif n==4 and b==0:
    print('*')
    print('**')
    print('***')
    print('****')
elif n==5 and b==0:
    print('*')
    print('**')
    print('***')
    print('****')
    print('*****')

if b > 1:
        print('You can print upto 0 and 1 only')
elif n>5:
  print('You can only print upto 1 to 5 ')



if n==5 and b==1:
    print('*****')
    print('****')
    print('***')
    print('**')
    print('*')
elif n==4 and b==1:
    print('****')
    print('***')
    print('**')
    print('*')
elif n==3 and b==1:
    print('***')
    print('**')
    print('*')
elif n==2 and b==1:
    print('**')
    print('*')
elif n==1 and b==1:
    print('*')


if b > 1:
        print('You can print upto 0 and 1 only')

elif n>5:
    print('You can only print upto 1 to 5 ')


