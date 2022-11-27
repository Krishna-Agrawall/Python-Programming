# def func(n):
#     fact=1
#     for i in range(n):
#         fact=fact*(i+1)
#     return fact
# number=int(input('Enter number : '))



# def func1(n):
#     if n==1 or n==0:
#         return 1
#     else:
#        return n*func(n-1)
# number=int(input('Enter number : '))
#
# print(func(number))
# print(func(number))



# import datetime
#
# time=datetime.datetime.now()
# print(time)
#
# import calendar
#
# cal=calendar.calendar(theyear=2005)
# print(cal)


# Snake water gun

# import random

# lst = ['s', 'w', 'g']

# chance = 10
# no_of_chance = 0
# computer_point = 0
# human_point = 0

# print(" \t \t \t \t Snake,Water,Gun Game\n \n")
# print("s for snake \nw for water \ng for gun \n")

# # making the game in while
# while no_of_chance < chance:
#     _input = input('Snake,Water,Gun:')
#     _random = random.choice(lst)

#     if _input == _random:
#         print("Tie Both 0 point to each \n ")

#     # if user enter s
#     elif _input == "s" and _random == "g":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     elif _input == "s" and _random == "w":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     # if user enter w
#     elif _input == "w" and _random == "s":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     elif _input == "w" and _random == "g":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     # if user enter g

#     elif _input == "g" and _random == "s":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")


#     elif _input == "g" and _random == "w":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     else:
#         print("you have input wrong \n")

#     no_of_chance = no_of_chance + 1
#     print(f"{chance - no_of_chance} is left out of {chance} \n")

# print("Game over")

# if computer_point == human_point:
#     print("Tie")

# elif computer_point > human_point:
#     print("Computer wins and you loose")

# else:
#     print("you win and computer loose")

# print(f"your point is {human_point} and computer point is {computer_point}")

#
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#






from pygame import mixer

# Instantiate mixer
mixer.init()

# Load audio file
mixer.music.load('eyes.mp3')
    

print("music started playing....")

# Set preferred volume
mixer.music.set_volume(0.2)

# Play the musice
mixer.music.play()

# Infinite loop
while True:
    print("------------------------------------------------------------------------------------")
    print("Press 'p' to pause the music")
    print("Press 'r' to resume the music")
    print("Press 'e' to exit the program")

    # take user input
    userInput = input(" ")

    if userInput == 'p':

        # Pause the music
        mixer.music.pause()
        print("music is paused....")
    elif userInput == 'r':

        # Resume the music
        mixer.music.unpause()
        print("music is resumed....")
    elif userInput == 'e':

        # Stop the music playback
        mixer.music.stop()
        print("music is stopped....")
        break




def getdata():
    import datetime
    return datetime.datetime.now()

