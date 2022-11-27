class Student:
    pass

rihan=Student()
neha=Student()


# Now Creating Instance Variable Of Rihan And Neha. Instance Variables Means You Can Add Variables in Rihan And Neha

rihan.name='Rihan'  # type: ignore
rihan.std='Fifth'  # type: ignore
rihan.section='A'  # type: ignore
rihan.subjects=['sanskrit','science','maths']  # type: ignore

neha.name='Neha'  # type: ignore
neha.std='Seventh'  # type: ignore
neha.section='C'  # type: ignore
neha.subjects=['sanskrit','science','maths','social science','english','hindi']  # type: ignore

print(rihan.name)  # type: ignore
print(rihan.std)  # type: ignore
print(rihan.section)  # type: ignore
print(rihan.subjects)  # type: ignore

print(neha.name)  # type: ignore
print(neha.std)  # type: ignore
print(neha.section)  # type: ignore
print(neha.subjects)  # type: ignore

print(rihan,'\n',neha)  #Run1