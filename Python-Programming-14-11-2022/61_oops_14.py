# In this pyfile we will learn about what is diamond shape problem in inheritance

class A:
    def met(self):
        print('This is the Method From Class A')

class B(A):
    def met(self):
       print('This is the Method From Class B')

class C(A):
    pass

class D(B,C):
    pass



a=A()
b=B()
c=C()
d=D()

d.met()
