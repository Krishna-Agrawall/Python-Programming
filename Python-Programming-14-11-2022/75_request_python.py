# request is a module
''' 
Now what is request module? -> Kabhi bhi hum internet pe work karte hai, too hum
http request send karna chahte hai. Agar hum programattically apne python program
ke andar karna chahte hai, too hum log chahaenge ki hum log bhi issi tarah ki request
apne program ke andar bhej paye. Now requst bhi bahaut tarah ki hoti hai . Too
hum get or post ke baare mai sikhenge.

Now what is get request? -> Abb dekho manlo ki muje get request leni hai, too get 
request ka mainly meaning hota hai wo ye hota hai ki mai kisi bhi url ke andar 
enter karu aur uska content liyau. For example r=r.get("give any url"). iske baad 
agar mai isse print karu r.text too iske andar ka content pura muje aisa ka aisa
muje yha pe text mai mil jayega
'''

import requests

r=requests.get('https://site.financialmodelingprep.com/developer')
print(r.text)
print(r.status_code)


'''
Abb hum second request padhenge jo ki hai post request. post request hoti hai 
wo ek special tarah ki request hoti hai jiska ek api end point hota hai aur usee
ke sath-sath aapko data bhejna padta hai. Too jo end-point hota hai humara wo 
url hota hai humara. too yha par manlo muje post request bhejni hai too 
mai likh sakta hu url='www.earthian.com'  usee ke saath-saath url ke sath mai
likhunga data . data mai kya hoga jo mera data hoga wo ek dictionary hogi.
Aur wo dictinary mai kya likhunga , uss dictionary mai dalunga 'p1':4 p1 hai mera 4
,'p2':8.. Iske baad mai kya karunga data ke baad mai likh sakta hu r2=requests.post
aur uske baad hum apna variables de dedenge url and data. Aur hum isse kuch iss tarah
likhenge url=url and data=data . kyunki jo url and data hai jo post function wo le
rha hai . Aur aisa kar ke hume ek response milega. Aur wo response ko lene ke liye
hum kya karenge waise hi lelunga response ko jaise humne get request ki help se
liya tha . Too humne r.text likha tha abb manlo ki mai status code jaan na chahta
hu too mai likhunga print(r.status_code)
'''

# url= 'www.earthia.com'
# data={
#     'p1':4,
#     'p2':8
# }
# r2=requests.post(url=url,data=data)