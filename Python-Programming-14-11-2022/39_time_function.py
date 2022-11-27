import time

#Run1

# initialize=time.time()
#
# a=0
# while(a<45):
#
#    a+=1
#    print(f'The value of a is {a} ')
# print('This while loop ran in ',time.time() - initialize,' seconds')
#
# initialize2=time.time()
# for a in range(46):
#     print(f'The value of b is {a}')
# print('This for loop ran in ', time.time() - initialize2,' seconds')

localtime=time.asctime(time.localtime(time.time()))
print(localtime)

# Sat Nov 19 12:06:30 2022