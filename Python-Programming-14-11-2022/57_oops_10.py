#In this pyfile we learn about What is  Multlever Inheritance

class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(darry.basketball)

# electronic device
# pocket gadget
# phone




#Let's create the first class
# class electronic_device:
#     airpods=1
#     def ed(self):
#         return f'Airpods are {self.airpods} time'

# #Let's creat the second class
# class pocket_gadgets(electronic_device):
#     mini_camera=1
#     artis=1
#     def pg(self):
#         return f'Mini Cameras are {self.mini_camera} and artis are {self.artis}'

# #Let's create the third class   
# class phone(pocket_gadgets):
#     # artis=1
#     def ph(self):
#         return f'Arits are {self.artis}'

# jame=electronic_device()
# chris=pocket_gadgets()
# Nasty=phone()

# print(chris.artis)