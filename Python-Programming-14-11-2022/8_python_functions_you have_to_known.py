str='kevin is a brilliant student'

print(str)         #Run1
print(len(str))    #Run1   means run both line


# print(str.isalnum())
'''Run2  It give the false because there are spaces included and spaces is not part of alphanumeric . But if you
   remove the spaces it will print true like, str='Kevinisabrilliantstudent'. print(str). The output will gonna true
'''


# print(str.isalpha()) #Run3 It will again give you the false because the spaces included remove spaces if you want true

print(str.endswith('student')) #Run4
print(str.endswith('astudent'))  #Run5


# print(str.count('l'))    #Run6 It will count the word that how many words are there in whole sentence

# print('The word you want to search is on index number : ', str.find('d'))   #Run7

# print(str.capitalize())  #Run8 It will capitalize the 0 word of index

# print(str.upper())   #Run9
# print(str.lower())   #Run10

print(str.replace('brilliant', 'dumb'))  #Run11

