# 1. The Playsound Module
# 2. The Datetime Module
# 3. Basics of Python: Conditional Statements, Iterative Statements & Slicing a string 
# 4. Implementation of Your Very Own Alarm Clock


#Run1 Line 9 to 12

# import datetime

# t= datetime.datetime.now()
# print(t)

#The date contains year, month, day, hour, minute, second, and microsecond.




#Run2

#importing the required modules
from datetime import datetime
from pygame import mixer
import time


#Next, we need to ask the user for the time he wants to set the alarm.


alarm_time = input('Enter the time of alarm to be set :HH:MM:SS AM/PM\n ')

'''
At this stage, we have obtained a point of time in the format of HH:MM: SS AM/PM.
To compare this format of time with the system time in our computer,
we need to extract the hours, minutes, seconds, and period from the above string.
We achieve this using string slicing.

String slicing helps you obtain a part of a word/sentence.


Note: If you don't know what is slicing watch file no 7_string_slicing.py in python_vs_code or 
      python-programming-14-11-2022
'''




 #obtaining the hour
alarm_hour=alarm_time[0:2]

 #obtaining the minute
alarm_minute=alarm_time[3:5]

 #obtaining the second
alarm_second=alarm_time[6:8]

 #obtaining the period
alarm_period=alarm_time[9:11]


print('Alarm Set')

'''
All we have to do now is compare and find when the current time matches the alarm time set by the user.
 To check every instant of time, we will make use of the While loop.
'''
while True:
      now = datetime.now()                   # current date and time    
      current_hour = now.strftime('%I')      # %I for Hour 00-12
      current_minute = now.strftime('%M')    # %M for Minute 00-59
      current_second = now.strftime('%S')    # %S for Second 00-59
      current_period = now.strftime('%p')    # %p for AM/PM

      if (alarm_period==current_period and alarm_hour==current_hour and alarm_minute==current_minute and
alarm_second==current_second):
        print('Wake Up')

       #Instantiate mixer
        mixer.init()


      #Load audio file
        mixer.music.load('eyes.mp3')

        print('Music Started Playing...')

      #Set preferred volume
        mixer.music.set_volume(0.2)

      #Play the music
        mixer.music.play()

#Infintie loop

        while True:
          print('*'*60)
          print("Press 'p' for pause the music\n")
          print("Press 'r' for resume the music\n")
          print("Press 'e' for exit the program")

          #take the user input
          userinput = input(' ')

          if userinput == 'p':
        
            #pause the music
            mixer.music.pause()
            print('Music is paused...')

          elif userinput == 'r':

            #resume the music
            mixer.music.unpause()
            print('Music is resumed...')


   
          elif userinput == 'e':

           #stop  the musicplayback
            mixer.music.stop()
            print('Music is stopped...')
            break
        

 