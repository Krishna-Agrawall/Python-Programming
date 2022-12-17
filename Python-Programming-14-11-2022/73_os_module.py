# OS Stands For Operating System
''' 
Your Computer is made with combination of hardware and your operating system is
tell hardware that when will this thing do , if there is mouse input what you want
to do, what to show to monitor. This all thing operating system handle. Operating
System is the head and it has to show which resources it has to manage.

'''

import os
# print(dir(os))
# print(os.getcwd())  # get current working directory

# os.chdir('') # This synatax is for if you want to change your os direcotry

# f=open('universe.txt')
# print(f.read())

# print(os.listdir()) # This syntax will give me the list of files which is situated on this folder

'''
Now if you need to make folder , from this os module you can made it, by mkdir.
make directory.
'''
# os.mkdir('whoops')

'''
Now, if you make directories in folder you can use os.makedirs('')
'''
# os.makedirs('This/that')

# os.rename('universe.txt','universal.txt')

# print(os.environ.get('Path'))

# print(os.path.join('C:/','/universal.txt'))

print(os.path.exists('C://'))
print(os.path.isdir('C://universal.txt'))

