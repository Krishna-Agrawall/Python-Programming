'''
Healthy Programmer
9 AM - 5 PM Office Hours
Water - water.mp3 (3.5 litrs) - Drank - log - Every 28 min
Eyes - eyes.mp3 - every 30min - EyDone - log - Every 35 min - log
Physical activity - physical.mp3 every - 45 min - ExDone - log

'''

from pygame import mixer 
from datetime import datetime
from time import time

def music_on_loop(file,stopper):
    '''This music on loop function play the music continuously until user input done,
        Now Let"s come to file , file is my file that i will play the music, Stopper is that when
        i want to stop the music .'''

    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:

        '''
        Why we use while loop here , we use while loop here because if you play the music and then 
        exit the program , then it does'nt get the time to play. You have to give the time to play, that's 
        why use while loop  
        '''

        print('Type Drank If You Drink The Water')
        input_user_name=input(' ')
        if input_user_name==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open('mylogs.txt','a')as f:     # we open in append mode because of overwrite
        f.write(f'\n{msg},{datetime.now()}\n')

if __name__=='__main__':
    

    init_water=time()

    '''Now this init_water=time , it will return the number, then after every 1 second 1 second, jo
    time hai utne hi zyada seconds return karega, to agar mai difference launga time - init water ka
    to kya hoga muje pata chal jayega ki kitne seconds hue hai. '''
    init_eyes=time()
    init_exercise=time()
    watersecs=28*60
    eyessecs=35*60
    exsecs=45*60

    while True:
        if time() - init_water>watersecs:
            print('Sir! It"s Your Water Drinking Time. Type Drank To Stop The Alarm')
            music_on_loop('water.mp3','drank')
            init_water=time()
            log_now('Drank Water At : ')

        if time() - init_eyes>eyessecs:
            print('Sir! It"s Your Time To Doing Eye Exercise. Type eyesd To Stop The Alarm')
            music_on_loop('eyes.mp3','eyesd')
            init_eyes=time()
            log_now('Eye Exercise At : ')

        if time() - init_exercise>exsecs:
            print('Sir! It"s Your Time To Doing Physical Activity. Type exd To Stop The Alarm')
            music_on_loop('exercise.mp3','exd')
            init_exercise=time()
            log_now('Physical Exercise At : ')