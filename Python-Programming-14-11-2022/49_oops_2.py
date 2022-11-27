class Employee:
    no_of_leaves=10

Jason=Employee()
Shreya=Employee()

Jason.name='Jason Hernandez'  # type: ignore
Jason.salary=25000  # type: ignore
Jason.type='Instructor'  # type: ignore

Shreya.name='Shreya Rai'  # type: ignore
Shreya.salary=50000  # type: ignore
Shreya.type='Student'  # type: ignore



# print(Jason.no_of_leaves)  Run1
# print(Shreya.no_of_leaves) Run2
# print(Employee.no_of_leaves) #Run3

print(Jason.__dict__)  #Run4        This dictionary shows that how that how many class variable are there
Jason.no_of_leaves=12
print(Jason.__dict__)  #Run5

# print(Employee.no_of_leaves) #Run6

print(Employee.__dict__)  #Run7