# [Run 1 From line 2 to 12
# import time
# def some_work(n):
#     time.sleep(n)
#     return n

# if __name__=='__main__':
#     print('Calling Some Work')
#     some_work(3)
#     print('Done!, Calling Again')
#     some_work(3)
#     print('Called Again')  #]



'''
Now, aap dekh sakte ho jab hum main function mai aate hai to hum pehle kuch 
print karwa te hai then hum function ko call karte hai. Function 3 seconds lega 
run hone mai because of time.sleep . Fir Hum wapis se wo hi some_work function 
ko call lagayenge uske badd ye bhi 3 seconds lega run hone mai. But kya ho 
agar aap chaho ki jab maine ek baar function ko call kar diya aur ye 1 time 
wala function n seconds laga rha hai koi statement print hone mai , kya ho 
agar aap second time isse print karwana chaha ho aur aap ye bhi chahte ko jab
aap second time print karwao tab ye bina n seconds ke turant(quickly) print ho 
jaye. So hum use karenge lru cache ka. 
 
'''
# [Run 2  From line 29 to 45
# import time
# from functools import lru_cache

# @lru_cache(maxsize=3)
# def some_work(n):
#     time.sleep(3)  
#     return n
# if __name__=='__main__':
#     print('Calling some work')
#     some_work(3)  
#     some_work(1)  # Current maxsize is 1
#     some_work(6)  # Current maxsize is 2
#     some_work(9)  # Current maxsize is 3
#     print('Done!! Calling Again')
#     input()  # When you enter any digit then it's gonna print Called Again . Otherwise not.
#     some_work(3)  # Current maxsize is 4
#     print('Called Again') #]


'''
So, let's understand humne kya kiya line 27 se . Humne kya kiya functools se 
lru_cache ko import kiya . Aur lru_cache ko import karne ke baad maine bold ki
meri pichli 3 calls ko save kar ke rakhna. Save kar ke isliye rakhna kyunki mai
nhi chahta ki mai isko baar baar chala ke apna time waste karu. Kise chale ke
ye some_work ko bar bar chalake. Abhi to humne time.sleep dal diya aapko dikhane
ke liye , lekkin yha pe time.sleep nhi hoga , yha pe humne time.sleep ko ek aise
chezz man lijye ki jo cheezz itna time leti hai means jo ki 3 seconds leti hai. 
to 3 second leni wali cheezz time.sleep hai. To hum yha pe 3 seconds ka delay 
dal de rhe hai . 

Abb lru_cache ka matlab kya hai ki aap ko sirf ek baar ki delayed second wait karna
padega uski maximum size ke hisab se. Means aap ko agar second time function ko 
call  karna hai to aap ko fir se n seconds wait nhi karna padega. It will run
quickly. Now aap logo ko ne dekha line 40 mai print statement se pehle
humne 3 line aur add kar di hai to wo abb kya karegi n seconds run karegi
fir line 41 3 seconds ke baad run karegi . Kyu karegi kyunki maximum size apne
3 diya and you input more than that's why. But if you enter max size 20 it
will hold you only one time then it print quickly, why because now max size 
is more than 3 . '''



'''
One little question for us. And the question is You have to ask the user how many
value do you want to cache , then you have to create one function . After creating
the function you have to give lru cache in input , and see what gonna happen.
'''

import time
from functools import lru_cache

m=int(input('How many Value Do You Want To Cache'))
@lru_cache(maxsize=m)
def some_work(n):
    time.sleep(3)
print('Calling Some Work')
some_work(5)
some_work(2)
some_work(4)
some_work(6)
print('Done!! Calling Again')
some_work(3)
print('Called Again')





