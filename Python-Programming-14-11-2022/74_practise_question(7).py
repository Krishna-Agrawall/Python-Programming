'''
1.Oh soldeier preetify my folder

Abb iska kya matlab hua , Problem statement hai ki aap logo ke pass ek folder hai.
uss foler ka path app ko diya hua hai.

2. path, dictionary file,format

Too path diya hua hai folder ka. Aap ko uss folder ka path lena hai as input. 
ek function banana hai. Wo function kya karega wo folder ka path lega as input
or string input lega. Or string input lene ke baad wo uski saari files ko dekhega.
aur ek lega dictionary file. Dictionary files ka matlab hai ki usme words rhenge
jo ki aap ko jinke saath khilwad nhi karna hai. Aur ek aur cheez rhegi input mai,
ek file format

def soldier('C://', '/universal.txt','.jpg')

Abb wo ye teno ko input lekar ,jitne bhi folder hai ko unko sabse pehle capitalize 
karega
'''

import os

def removeFiles(filen):
    DNotDis = open(filen)
    l = (DNotDis.read())
    var = (l.split('\n'))
    DNotDis.close()
    return var

def army(pathn, filen, ext):
    filen=filen
    pathn=pathn
    os.chdir(pathn)
    count = 0
    var = removeFiles(filen)
    for f in os.listdir():
         f_name, f_ext = os.path.splitext(f)
         if f_ext == f'.{ext}':
             newName = f'{str(count)}{f_ext}'
             count += 1
             os.rename(f,newName)
             pass
         if f_name not in var:
             tn = f_name.title()
             new_name = f'{tn}{f_ext}'
         else:
             new_name = f'{f_name}{f_ext}'
         os.rename(f,new_name)

if __name__ == '__main__':
    pathn=input('Enter Path Name:')
    filen=input('Enter File Name Which Contain Name Of Files Not TO Alter: ')
    ext=input('Enter Extension/Formate: ')
    army(pathn,filen,ext)


    # I copied it .