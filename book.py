class Book:
    def __init__(self,id,name,author):
        self.id=id
        self.name=name
        self.author=author
    def getid(self):
        return self.id
    def getname(self):
        return self.name

    def getauthor(self):
        return self.author


mybook=Book(1,'Mahako ma','Madan Krishna Shrestha')
print('The id of the book is {}'.format(mybook.getid()))
print('The name of the book is {}'.format(mybook.getname()))
print('The author of the book is {}'.format(mybook.getauthor()))
