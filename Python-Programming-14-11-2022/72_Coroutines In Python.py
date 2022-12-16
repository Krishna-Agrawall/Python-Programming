'''
Manlo, Mai ek fuction banau searcher(). Jo ki kya karega ek book mai search karega
ki koi text hai ya nhi hai. Aur aap khi se book ya koi file read kar rhe hai ho aur
wo meri file time le rhi hai manlo mai import time lele rha hu + aur 
time.sleep(4) laga deta hu. Hum koi badi book yha pe nhi lene wale hai aur koi book
texts file bhi nhi dalne wale hai aur fir text file se usse read kare. Isse accha
hum time.sleep use kar lete hai. Isse kya hoga 4 second ka delay aa jayega. Aap
bus aisa samaj lo ja humne time.sleep likha hua hai, wha par hum koi bahaut badi 
book ko read kar rhe ya koi machine learning model read kar rhe hai, ya koi aise
file read kar rhe ho jo ki bahaut zyada time consume karti ho

Abb hum kya karenge ki mai chahta hu ki iske time.sleep ke bad mai koi bhi cheej
searcher function ko du to ye muje bata de ye cheez book mai hai ya nhi hai. To 
manlo mai jo book read kar rha hu wo kuch is tarah dikh ti hai 
book='Hello I Am An Earthian And My Name Is Krishna Agrawal'. Now Abb aap kuch 
aisa samaj li jiye ye string jo hai ye 10000 or 15000 or 20000 badi string hai
aur aap log isse read kar rhe hai jo ki time lagne wala hai 4 second kyunki aap
log isse kisi file se read kar rhe hai. Too yha par jo hai hum ko time lagne wala
hai , Abb hum chahte hai ki agar ek baar import time se time.sleep tak run kare
too ye itna run ho jaye aur uske agli baad run kare too time.sleep ki next line se
run ho jaye function. 

Too yha tak pauch ne ke liye hum coroutines ka use karte hai. Abb ye jo searcher
function banaya hai ye humne ek coroutine banaya hai. Now, Abb Python Ko Pata kaise
chalega ki ye coroutine hai ye ek normal function nhi hai. So hum ek while True:
lenge .Abb mai bolunga text = (yield) . Abb kya hota tha yield keyword mai hum
generator use kar dede the to hum kehte thee ki ye value ko on the fly generate 
kar do . Hum kehte thee yield i . yield i ka matlab hota tha ki value ko on the fly
generate kardo. Lekin jab mai text = (yield) likh rha hu too iska matlab ye hai ki
mai iss def searcher() function ko ek coroutines ki tarah use karne wala hu , aur
uske baad jo bhi cheez searcher function ko send karunga wo ye text=(yield)  pe aa
jayegi. To direct searcher function mai chalu karunga agli baar ,isko send karunga
to ye import time +book+time.sleep yha tak too ye start karke car ko khada kar dega.
uske baad ye direct while wali condition mai aa jayega aur fir while to text tak
chalta rhega infinitely. 

Abb mai likhunga if text in book: tab kya karega ye print('Your text is in the book')
else: mai ye print karega print('Your text is not in the bood'). 

Abb yha par baat aat hai ki hum iss coroutine ko chalaye kaise. Now one thing
you need to know or understand that ki ye sab function nhi hai ye ek coroutine hai.

Now abb  hum while loop se bhar nikal te hai , aur nikal ne ke baad hum likh te hai
search = searcher() . So humne ye coroutine ka ek instance bana liya hai . Abb
yha par mai kya karne wala hu search karne wala hu koi values. Abb kaise mai wo 
karunga , wo karne ke liye mai kya karunga sabse pehle start karunga . Aur isko
start kar ne ke liye muje next method chalana padega . next(search). 

Abb yha par kya hai agar mai likhu search.send("Krishna"). Agar mai isko run karunga
too ye 4 seconds ka delay le ga aur fir ye print kar dega your text is in the book.
Lekin agar mai search.send("Krishna") ke baad ek input lu aur usme kuch bhi likh du
man lu ki input('Press Any Key') aur ye likh ne ke baad mai ye search ko fir se 
input ke baad send kar deta hu . Abb mai jaise he isse run kar deta hu too sabse 
pehle too ye delay aa rha hai yha par . Jab ye pehli baar run karega time.sleep(4)
ka delay aayega. Then ye keh rha hai press any key . Aur jaise he humne key press
ki too ye turant run ho jayega. Too pehli baar bus ye import time to time.sleep 
work karega. Aur agli baar jab ye chalega to while se chalta he chala jayega, Aur
uske baad wali call hogi function ki ye jo hai meri line 70 se function chalu ho gi
means while se. 


'''

def searcher():
     import time
     #Some 4 Seconds Time Consuming  Task
     book='Hello I Am An Earthian And My Name Is Krishna Agrawal'
     time.sleep(4)

     while True:
        text=(yield) # This yield for creating coroutine
        if text in book:
            print('Your text is in the book')
        else:
            print('Your text is Not in the book')

search=searcher()
print('Search Started')
next(search)
print('Next Method Run')
search.send("Krishna") # type: ignore
search.close()
# input('Press Any Key : ')
# search.send("Krishna Agrawal") # type: ignore
# input('Press Any Key : ')
# search.send("Nice") # type: ignore
# input('Press Any Key : ')
# search.send("James") # type: ignore
    
'''
Now,ek baar aur coroutines ko summarize kar lete hai ki ye hum kab use karte hai,
coroutine hum tab istemal karte hai jab humara jo function hai usme kuch aise
cheezee hai jo ki usse initialize hone mai bahaut zyada time leti hai. Aur ek baar
wo initialize ho jata hai uske baad wo kaam karta hai . Jaise ki humara searcher
tha . Sabse pehle ye book ko read karta hai import time se time.sleep tak. 
Humney delay laga diya hai . Delay ko aap kuch aisa samaj lo ki book ko read karne
mai laga hua time, yaa fir book ko download karne mai laga hua time too ye sab cheeze
lagi yha uske baad while True ke baad ye chalta gaya .  
'''
