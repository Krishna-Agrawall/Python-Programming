# In this pyfile we will learn about Selector and Property Decorators.

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email= f"{fname}.{lname} @gmail.com"

    def employee_detail(self):
        return f'First name is: {self.fname} And Last name is: {self.lname}'

    @property   # This property decorator work is to print the string object from the int object number.
    def email(self):
        if self.fname==None or self.lname==None:
            return 'Email is not set. Please set using setter'


        return f"{self.fname}.{self.lname} @gmail.com"

    @email.setter
    def email(self,string):
        names=string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname=names.split('.')[1]
    
    @email.deleter
    def email(self):
        self.fname=None
        self.fname=None

      
kriti=Employee('Kirtika','Voyce')
Preet=Employee('Preet','Roy')

print(kriti.employee_detail())
print(kriti.email) # If you don't want to run this as function  use @property decorator.
# But after using @property decorator then you use () function it will give you the error.

kriti.fname='Neil'
print(kriti.email)

kriti.email='This.That@gmail.com'
print(kriti.email)

del kriti.email
print(kriti.email)

'''
Now, if you want to input the email and after taking the input , then it changes the fname and lname.
So, you have to create one function which changes automatically if fname and lname changes. To do this
we make setter. First we use @ decorator and then we write the attribute which you want to take the input
 , and our current attribute is email . @email.setter. Abb is decorator ko .setter likh ne ke baad, mai 
 ek banaunga  function wo hi email naam se. Aur fir jab bhi email ko set kar ta hu, yaani ki jab mai
 chahta hu ki email set kare, wo mai ye function ke andar likh dunga. But jab aap ye function nhi 
 banate hai aur ek naya email declare kar dete hai for ex - kriti.email='This.That@gmail.com'
 . Abb manlo @email.setter+function banaya hi nhi hai aur jab aap isse run karoge to ye aap ko eroor
 dega ki can't set attribute. Abb is attrubute ko set karne ke liye hum setter bana te hai. Abb hum
 wapis se apne topic pe aate hai @email.setter pe. Hum ek setter bana rhe hai joki ye attribute ko set
 kar dega. jaise hi mai def email(self) mai ek argument dunga aur wo string bol deta hu.
 def email(self,string): 
    names= string.split('@')[0]

Abb ye split function kya karta hai tukde kar deta hai , manlo ki maine ye string di :
Kirtika.Voyce@gmail.com  . aur maine isme .split run kar diya isme to ye isko ek list bana dega.
pehli [0]list ka argument ho jayega Kirtika.Voyce ye  aur 1st index pe ho gmail.com. Hume gmail.com
se matlab nhi hai hume matlab iske 0th index se hai. abb ye names mai humara Kirtika.Voyce aa gaya
hai.

Abb hum kya likhenge 
self.fname=names.split('.')[0]
aur names.split 1 mai humara lname aa jayega
self.lame=names.split('.')[1]


'''