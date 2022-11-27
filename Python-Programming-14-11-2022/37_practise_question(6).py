#Building snake water gun game

import random
computer = ['snake', 'water', 'gun']
chance=10
no_of_chance=0
computer_point=0
human_point=0




print('Press s for snake')
print('Press w for water')
print('Press g for gun')



while no_of_chance<chance:

    user=input('Enter Your Choice From Above:')
    v=random.choice(computer)

    if user==v:
        print('Tie 0 points to each')

    elif user== 's' and v=='water':
       human_point += 1
       print('Congratulations ! sir you won the game , Your snake wins against Water')
       print('You won 1 point')
       print(f'\n\nYou Won The Game {human_point} time and Computer Won the Game {computer_point}\n\n ')


    elif user=='g' and v=='water':
        computer_point += 1
        print('You have lost the game , Your gun lost against Water')
        print('Computer wins 1 point')
        print(f'\n\nComputer Won The Game {computer_point} time and You Won The Game {human_point} time\n\n')

    elif user== 'w' and v=='gun':
       human_point += 1
       print('Congratulations ! sir you won the game , Your water wins against gun')
       print('You won 1 point')
       print(f'\n\nYou Won The Game {human_point} time and Computer Won the Game {computer_point}\n\n')


    elif user=='s' and v=='gun':
        computer_point+=1
        print('You have lost the game , Your snake lost against Gun')
        print('Computer won 1 point')
        print(f'\n\nComputer Won The Game {computer_point} time and You Won The Game {human_point} time \n\n')


    elif user=='g' and v=='snake':
        human_point+=1
        print('You have won the game , Your gun won against snake')
        print('You won 1 point')
        print(f'\n\nYou Won The Game {human_point} time and Computer Won the Game {computer_point}\n\n')

    elif user=='w' and v=='snake':
        computer_point+=1
        print('You have lost the game , Your snake lost against Gun')
        print('Computer won 1 point')
        print(f'\n\nComputer Won The Game {computer_point} time and You Won The Game {human_point} time\n\n')
    else:
        print('You have inputed wrong character , The character you need to input is s,w,g.')
        no_of_chance+=1
        print(f'{chance-no_of_chance} is  left are {chance}')

print('Game Over')

if computer_point==human_point:
    print('The result is Tie')

elif computer_point>human_point:
    print('computer win the game')

else:
         print('You win the game')

print(f'Your point is {human_point} and computer point is {computer_point} ')








