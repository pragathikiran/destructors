class Library:
 def __init__(self,name):

    self.name = name
    self.books = []

def add_book(self,book_name):
  
      self.books.append(book_name)
      print(f'📖"{book_name} "added to the library!')

def show_books(self):
   if self.books:
       print(f'books available in {self.name}')
       for book in self.books:
        print(f"- {book}")
    
    else:

     print("sorry book not found")

my_library = Library("kids library")

my_library.add_book("harry potter")
my_library.add_book("famous five")
my_library.add_book("wonderful wizard of oze")
my_library.add_book("good girl guide to murder")
my_library.add_book("the day I stop drininig milk")

my_library.show_books()




