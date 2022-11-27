print('\t\tWELCOME TO GRAHAM HEALTH MANAGEMENT\t\t')
print('Press 1 For Alex')
print('Press 2 For Jos')
print('Press 3 For Martinez')

choice=int(input('Enter Your Choice From Above : '))
if choice==1:

   def alex():


       print('Hello Mr.Alex What do you want to choose an exercise or a diet')
       print('Press 1 For Exercise or Press 2 For Diet')
       ed=int(input('Enter Your Choice : '))
       if ed==1:
          f = open('alex_exercise.txt','r+')

   #For Exercise

          c=f.write('\nAlex, can you tell me what exercise did you did in gym today?\n')
          print(f.read(c))

          ask = f.write(input(''))
          print(f.read(ask))

          print('Can You Please Again Type It What Exercise You Did?')
          ask1=input('')
          print(ask1)


          e=f.write('\nWell Alex You Enter All The details Successfully\n')
          print(f.read(e))

          print('Well Alex You Enter All The Details Successfully')



# For Food


       elif ed == 2:
            f1=open('alex_food.txt','r+')

            # print('Alex, can you tell me what  type of exercise did you did in gym today?')
            eat = f1.write('\nAlex, can you Please tell me what food did you did eat today?\n')
            print(f1.read(eat))

            ask2 = f1.write(input(''))
            print(f1.read(ask2))

            print('Alex, can you please tell me again what food did you eat today?')
            ask3 = input('')
            print(ask3)

            e = f1.write('\nWell Alex You Enter All The details Successfully\n')
            print(f1.read(e))

            print('Well Alex You Enter All The Details Successfully')

       # return ed

   alex()


elif choice==2:
    def jos():
        print('\n\n\tHello Jos What Do You Want To Choose Exercise or Diet :\t\n\n')
        print('Press 1 For Exercise or Press 2 For Diet')
        choose1=int(input('Enter Your Choice From Above : '))

        if choose1==1:
            f3=open('jos_exercise.txt','r+')

    #For Exercise

            # print('So, Hey Jos Can You Please Tell What Type Of Exercise You Have Did Today : ')

            je=f3.write('\nSo, Hey Jos Can You Please Tell What Type Of Exercise You Have Done Today : \n')
            print(f3.read(je))

            je1=f3.write(input(''))
            print(f3.read(je1))

            print('Can You Please Type Again What Type Of Exercise You Have Did Today : ')

            je2=input('')
            print(je2)

            je3=f3.write('\nOk! You Have Completed All Type Of Method Successfully . Thank You\n')
            print(f3.read(je3))

            print('Ok! You Have Completed All Type Of Method Successfully . Thank You')




        elif choose1==2:
            f4 = open('jos_food.txt','r+')

    # For Food

            # print('So, Hey Jos Can You Please Tell Me  What Type Of Food You Have Eaten Today : ')

            jf = f4.write('\nSo, Hey Jos Can You Please Tell Me What Type Of Food You Have Eaten Today : \n')
            print(f4.read(jf))

            jf1 = f4.write(input(''))
            print(f4.read(jf1))

            print('Can You Please Type Again What Type Of Food You Have Eaten Today :  ')

            jf2 =input('')
            print(jf2)

            jf3 = f4.write('\nOk! You Have Completed All Type Of Method Successfully . Thank You\n')
            print(f4.read(jf3))

            print('Ok! You Have Completed All Type Of Method Successfully . Thank You')

    jos()



elif choice==3:
    def Martinez():
        print('*'*50)
        print('\n\n\tHello Martinez What Do You Want To Choose Exercise or Diet :\t\n\n')
        print('*' * 50)
        print('\tPress 1 For Exercise or Press 2 For Diet\t')
        print('-'*50)
        choose=int(input('\tEnter Your Choice From Above : \t'))

        if choose==1:
            f5=open('martinez_exercise.txt','r+')

    #For Exercise

            # print('So, Hey Martinez Can You Please Tell What Type Of Exercise You Have Done Today : \n')

            me=f5.write('\nSo, Hey Martinez Can You Please Tell What Type Of Exercise You Have Did Today : \n')
            print(f5.read(me))

            me1=f5.write(input(''))
            print(f5.read(me1))

            print('Can You Please Type Again What Type Of Exercise You Have Did Today : ')

            me2=input('')
            print(me2)

            me3=f5.write('\nOk! You Have Completed All Type Of Method Successfully . Thank You\n')
            print(f5.read(me3))

            print('Ok! You Have Completed All Type Of Method Successfully . Thank You')




        elif choose==2:
            f6 = open('martinez_food.txt', 'r+')

    # For Food

            # print('So, Hey Martinez Can You Please Tell Me  What Type Of Food You Have Eaten Today : ')

            mf = f6.write('\nSo, Hey Martinez Can You Please Tell Me What Type Of Food You Have Eaten Today : \n')
            print(f6.read(mf))

            mf1 = f6.write(input(''))
            print(f6.read(mf1))

            print('Can You Please Type Again What Type Of Food You Have Eaten Today :  ')

            mf2 = input('')
            print(mf2)

            mf3 = f6.write('\nOk! You Have Completed All Type Of Method Successfully . Thank You\n')
            print(f6.read(mf3))

            print('Ok! You Have Completed All Type Of Method Successfully . Thank You')

    Martinez()










