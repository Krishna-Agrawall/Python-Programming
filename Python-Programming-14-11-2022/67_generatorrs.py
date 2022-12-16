'''
1) Iterable - __iter__() or __getitem__()
2) Iterator - __next__()
3) Iteration


Now first let's talk about what is iterable ? 
 -> Iterable ek aisa python object hota hai jisme yaa to
  __iter__() ye wala method or __getitem__() ye method define 
  hota hai. Ye kya karta hai agar hum kisi run karenge kisi
  object ke uppar ye method tab wo hume iterator pradan(give)
  karega.

Now  Ye Iterator Kya Hota Hai?
 -> Iterator ek aisa object hota hai jisme __next__() define
    hota hai. Jisme ye Iterable wala function define hota
    hai.

Now Ye Iteration Kya Hota Hai?
 -> Iterate karne ki prakriya ko hum iteration kehthe hai.

Let's Understand this all thing in deep.

Agar mai chahta hu ki mai kisi bhi python object ko traverse 
karu jaise ki list ho sakti hai wo, ya to string ho sakti hai
manlo toddy. Aur t o d d y karke ek for loop mai usse access
karne ki kosis karu  . To mai usse kar paunga ya nhi kar paunga
ye batayega agar ye object iterable hai ya nhi . Ye baat batai
gi ki mai iterate kar sakta hu ya nhi. Agar mai usko iterate
kar sakta hu to wo ek iterable hai , aur agar nhi kar sakta to
wo iterable nhi hai. 

Aur Agar wo iterable hai to wo iterate kaise karega, wo kya 
karega __iter__() ye function run karke ek iterator generate 
karega. Aur Jab mai wo iterator pe jab mai __next__() __next__()
chalata rhunga , to wo muje us object ka agla item pradan
(provide) karega.


Now Ye Generators Kya Hota Hai?
 -> Generators ek tarah ke iterators hote hai . Means   
    Iterator - __next__() ye wala. Wo ek aise tarike ke 
    iterators hote hai jinko hum sirf ek baar travere kar
    sakte hai..


'''

def gen(n):
    for i in range(n):
        yield i  # return i

g=gen(5)
# print(g.__next__()) #Run1
# print(g.__next__()) #Run2
# print(g.__next__()) #Run3
# print(g.__next__()) #Run4
# print(g.__next__()) #Run5
# print(g.__next__())  # This will give you stop iteration error #Run6

# for i in g:
#     print(i)


t ='toddy'  #Weel this string is iterable but at the same time int is not. 
# i=iter(t)
# print(i.__next__()) #Run7
# print(i.__next__()) #Run8
# print(i.__next__()) #Run9
# print(i.__next__()) #Run10
# print(i.__next__()) #Run11

# y=23
# k=iter(y)
# print(k.__next__()) #Run 12 
# This line 73 to 75 will give you TypeError: 'int' object is not iterable


# for i in t:
#     print(i) #Run13

# def fib(n):
#     if n==1:
#         yield 0
#     elif n==2:
#         yield 14

#     else:
#         yield fib(n-1)+fib(n-2)

# f=fib(8)
# print(f) #Run14

# def fact(n):
#     if n==0:
#         yield 0
#     elif n==1:
#         yield 1
#     else:
#         yield n*fact(n-1)
# fa=fact(5)
# print(fa) #Run15

'''
Ab Apne Socha Hoga ki line 51 mai humne ek yield keyword
define kiya hai To Ye hota kya hai? 
 -> Mai return karu ya print karu ya mai yield karu
   ye 3 alag-alag baate hai. Agar mai return karu , to iska
   matlab ye hoga ki ye function ki return value hai aur return
   statement ko dekh ke function laut jayega wapas, yaani ki 
   uske aage usko kuch nhi karna hai, means ki return ke baad
   aap kuch bhi likh do kuch bhi run nhi hone wala hai. Abb

 -> Abb print kya hota hai? print statement kya karta hai ,
    ye console mai print karta hai, aur function mera chalta
    rehega .
 
 -> Abb ye yield kya karega ? Ye yield on the fly value ko 
    generates karega values ko , yaani ki wo ek generator hai.
    for example humne ek g namka variable banaya usme gen
    define kar diya aur uske andar koi bhi random value
    de di fir next line mai humne wo g ko print karwa diya. 
    Aur console mai hume generator object ke baare mai bata
    dega ye function nhi hai. Aur agar aap yield i ki jagah
    return i print karwayenge to ye hume 0 print kar ke de dega.
    Kyunki ye return kar rha hai 0 . for i in range(n) aaya 
    to jaise hi 0 aaya to iske value isne muje 0 return kardi.

'''
