from pygame import mixer
from datetime import datetime
from time import time 

def music_on_loop(file,Stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_user_detail=input(' ')
        if input_user_detail==Stopper:
            mixer.music.stop()
            break
def newlog(msg):
    with open ('log2.txt','a') as f:
        f.write(f'{msg} {datetime.now()}') 
if __name__=='__main__':
    
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersec=10
    eyesec=27
    excercise=45

    while True:
        if time()-init_water>watersec:
            print('Time for drink water, Type "drank" to stop the alarm ')
            init_water=time()
            music_on_loop('water.mp3','drank')
            newlog('Drank water at : ')

        if time()-init_eyes>eyesec:
            print('Time for doing eyes exercise, Type "eyed" to stop the alarm ')
            init_eyes=time()
            music_on_loop('eyes.mp3','eyed')
            newlog('Done eyes exercise at : ')

        if time()-init_exercise>excercise:
            print('Time for doing physical activity , Type "exd" to stop the alarm ')
            init_exercise=time()
            music_on_loop('exercise.mp3','exd')
            newlog('Done eyes exercise at : ')