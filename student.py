from book import Book
class Student:


    def __init__(self,name,address):
        self.name=name
        self.address=address
    def getname(self):
        return self.name
    def getaddress(self):
        return self.address
a=int(input("Enter the no of students:"))
studentlist=[]
for i in range(1,a+1):
    name=input("enter the name:")
    addr=input("enter the address:")
    stud=Student(name,addr)
    studentlist.append(stud)

studentmap=map(lambda stud:stud.getname()+" "+stud.getaddress(),studentlist)
print(list(studentmap))

myBook=Book(2,'Adultery','Paulo Coelho')
print(myBook.getauthor())

