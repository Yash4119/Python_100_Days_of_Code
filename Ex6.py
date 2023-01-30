'''
Create a library class that have 2 variables
no_of_books
list of books
'''

class Library:
    

    def __init__(self,name):
        self.libName = name
        self.no_of_books = 0
        self.books = {}

    def addBook(self, book, author):
        self.no_of_books += 1
        self.books[author] = book
    
    def showBooks(self):
        print()
        print("Printing All Books")
        for key in self.books:            
            print("Book Name :- ",key," => Written by :- ",self.books[key])
            print()

    def countOfBooks(self):
        print(f"Number of Books in the {self.libName} library are :- {self.no_of_books}")


lib1 = Library("Lonavla Sahakari Library")
lib1.addBook("Sawant","Chava")
lib1.addBook("HanumanJi","Ramayan1stEdition")
lib1.addBook("Ved Vyas","Ramayan2ndtEdition")

lib2 = Library("DYPIT Pimpri Library")
lib2.addBook("Yash Ambekar","How to trade Profitably")
lib2.addBook("Teja Bhai","Apti and Geometry")

print(lib1.libName , " Details")
lib1.showBooks()
lib1.countOfBooks()

print(lib2.libName , " Details")
lib2.showBooks()
lib2.countOfBooks()