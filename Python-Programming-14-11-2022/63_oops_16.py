# In this pyfile we will learn about what is abstract base class

'''
Let's get start, to kabhi kabhi kya hota hai , mai ek aise class banana chahta hu joki ek base-class 
ki tarak work kare. example humne ye Class Rectange banaya. 

Dont' run this code this is an example only
class Rectange:
    type='Rectangle'
    sides=4
    def __init__(self):
        self.length=2
        self.breadth=2
    def rectange_area(self):
        return f'{self.length}*{self.breadth}'

lekin ab mai ye class Rectangle banane ke baad ek square naam ki bhi class banau, aur jab square naam ki 
class banaunga tab mai usme rectange_area print karunga , usme mai kya karunga return karunga 
self.length ka square. To ab kyu na hum ek shape naam ki ek base class bana du . Jo ki kuch rules and 
regualations rakhegi. shape naam ki class ek aise rules impose karegi , sabse pehla rule ki sabke pass
ek rectange_area function hona chayie, koi bhi aise class bana na paye jisme rectange_area function 
na ho , rectangle_area ek aisa function hai jo ki sabko bana na hai , ye message aapne sabko de diya hai.
To iss tarah ke message ko implement karne ke liye hume kya karna padta hai , hum istemal kar te hai
abc meta class ka . Now what is abc meta class . Humare python mai ek module hota hai
 from abc import ABCMeta, abstractmethod. Ab ye abstractmethod ek decorator hota hai . To fir hum
 ek class bana denge Shape naam . Fir class Shape ke inside jake hum likhenge ki sabko rectangle_area
 naam ka function implement karna hai . Aur ye ek abstract method hai. Abstract methdd matlab , ki
 sabko ye chize define karni padegi. Ab ye class Shape banane ke baad  hume ye Rectangle ko class
 Shape se inherit karna padega. Ab agar aap Class Rectangle ke def rectangle_area ko comment kar dete 
 ho fir ek object bana ke run kar te ho program to aapko console ek error throw karega ki aap 
 rectange_area ko define karo, aap ne rectange_area ko define nhi kiya hai.
'''
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def rectangle_area(self):
        return 0

class Rectangle(Shape):
    type='Rectangle'
    sides=4
    def __init__(self):
        self.length=2
        self.breadth=2


    def rectangle_area(self):
        return self.length*self.breadth


rect1=Rectangle()

print(rect1.rectangle_area())