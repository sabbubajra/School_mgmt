print('1.Enter the records.')
print('2.Read the records.')
choice=int(input("Enter the choice:"))
cont=True
if(choice==1):
    while cont:
        name=input('Enter the name:')
        address=input('Enter the address:')
        phone=input('Enter the phone no:')
        course=input('Enter the course:')
        file=open('enter.txt','a')
        file.write('Name of the student:{}\n'.format(name))
        file.write('{} lives in {}\n'.format(name,address))
        file.write('Phone no is {}\n'.format(phone))
        file.write('{} is studying {}\n'.format(name,course))
        file.close()
        repeat=input('Do you want to continue(Y/N):')
        cont=(repeat=='y')
else:
    file=open('enter.txt','r')
    print(file.read())
    file.close()




