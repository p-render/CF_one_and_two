# Library model: 3 Classes, and demonstration commands.

class Library(object):
    def __init__(self, name):
        self.name = name
        self.shelves = []

    def new_shelf(self):
        new_shelves = Shelf()
        self.shelves.append(new_shelves)

    def title_list(self):
        shelved = []
        for b in range(0,len(self.shelves)):
            shelved.append(self.shelves[b].list_books())
        return shelved

    def list_shelves(self):
        return len(self.shelves)

class Shelf(object):
    def __init__(self):
        self.books = {}
    
    def list_books(self):
        shelved = []
        for b in self.books.keys():
            shelved.append(self.books[b].titles())
        return shelved

class Book(object):        
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.subject_num = None

    def enshelf(self, subject_num):
        self.subject_num = subject_num
        libro.shelves[self.subject_num].books[self] = self
    
    def unshelf(self):        
        del libro.shelves[self.subject_num].books[self]
        return self

    def titles(self):
        return self.title

# The Library in action

libro = Library("Computer Book Library")

print                                               
print "Good Books on Computers"
print

# Creating Shelves
for b in range(0,5):
        libro.new_shelf()

# Creating Books
python = Book("Learn Python the Hard Way","Zed Shaw")
pandas = Book("Python for Data Analysis", "Wes Mckinney")
processing = Book("Learning Processing","Daniel Shiffman")
open_source = Book("The Cathedral and the Bazaar","Eric Raymond")
open_source_2 = Book("Producing Open Source Software", "Karl Fogel")
coders = Book("Coders at Work", "Peter Seibel")
arduino = Book("30 Arduino Projects for the Evil Genius", "Simon Monk")

#Shelving Books
python.enshelf(0)
pandas.enshelf(0)
processing.enshelf(1)
open_source.enshelf(2)
open_source_2.enshelf(2)
arduino.enshelf(3)
coders.enshelf(4)

# Testing Library functions
print "There are " + str(libro.list_shelves()) + " shelves in the library."
print
print "Inventory of books (shelves bracketed): "
print 
print libro.title_list()
print
print "Checking out 'Learn Python the Hard Way'"
python.unshelf()
print
print "Showing the change in inventory (unbracketed)..."
print

for b in libro.title_list():
    print ', '.join(str(item) for item in b)

print
print "Enjoy!"
print

        
