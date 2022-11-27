i=10
n=18
while(True):
    if  i <=0:

        print('Game over')
        break
    i=i-1
    a=int(input('Guess number = '))
    if n == a:
        print('Congratulations you won the game')
        print('You won the game in' , i , 'chance')
        break

    else:
        if a>0 and a<10:
          print('You are close to the number try again\n')
          print('Your chance left is ', i)

        elif a>10 and a<15:
          print('You are far  close to the number try again\n')
          print('Your chance left is ', i)

        elif a>14 and a<18:
          print('You are really close to the number try again\n')
          print('Your chance left is ', i)
        elif a>18 and a<21:
            print('Your are really close to the number try again\n')
            print('Your chance left is ',i)
        elif a>20 and a<30:
          print('You are close to the number try again\n')
          print('Your chance left is ', i)

        elif a>30 :
          print('You are not close to the number try again\n')
          print('Your chance left is ', i)














