'''f=open("hello.txt",'r')
print(f.read())
with open("hello.txt",'w')as f:#to close the opened file
    f.write("This is pycharm\n")
    f.write("file handling in pycharm\n")
    f.write("use of write in file handling\n")

f=open("hello.txt",'a')
f.write("use of append to append the text")
'''
#f=open("byebye.txt",'x')
#f.close()
with open("byebye.txt",'w')as f:
    f.write("welcome to the programming\n")
    f.write("Programming in pycharm\n")
    f=open("byebye.txt",'r')
print(f.read())
print(f.seek(10))#
print(f.read(10))#from intial position to 10 character read
print(f.tell())
print(f.seek(0))
print(f.read(5))
#print(f.readline(5=-1))
print(f.readable())
print(f.writable())
print(f.seekable())
print(f.isatty())


#1.enter the record
#2.read the record
#choice 1=open the file in write mode and enter the record of the students
#choice 2=open the file in read mode and read the record of the students(at first if open in read mode then print
#"No record found"
#include(save(y/n):if y=add more records else n=exit