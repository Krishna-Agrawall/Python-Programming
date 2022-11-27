# f=open('universe1.txt','w')
# f.write('In milky way galaxy one system occurs which is known as solar system')  #Run1
# f.close()


# f=open('universe1.txt','a')
# f.write('\nIn solar system there are 8 planets. which is  Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune')
# f.close() #Run2


# if you want to print how many characters you typed in a particular simply you have to crete the variable
# and print it let me show you with an example

f=open('universe1.txt','a')
character=f.write('\nIn solar system there are 8 planets. which is  Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune')
print(character)       #Run3
f.close()



#Now if i open file in write mode (w) it all deletes what you write in file .


# f=open('universe.txt','w')
# character=f.write('In solar system there is one habitable planet known as earth')
# print(character)   #Run4
# f.close()




'''Now What Happen If I Say You Can Read And Write In Same File. So, If You Want To Do This There Is One 
   One Mode Whice is 'r+' Mens You Can Read Also And Write Also In Existing File. Let Me Show You An Example'''


f=open('universe1.txt','r+')
print(f.read())               #Run5
f.write('\nEarth is a planet in solar system which is habitable. nd in this planet many type of species exist')
print(f.read())               #Run6
f.close()