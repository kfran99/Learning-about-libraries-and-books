class Book(object):
    def __init__(self, my_id, title, author):
        self.title = title
        self.author = author
        self.id = my_id

    def print_book_attributes(self):
        print self.title +" "+ self.author +" " + str(self.id)


#new_book = Book("Gone with the Wind", "Margaret Mitchell")

#new_book.print_book_attributes()

class Library(object):
    books = {}

    def add_book(self, book):
        self.books[book.id] = book
    def show_books(self):
        for book_id in self.books.keys():
            self.books[book_id].print_book_attributes()    
    # def __init__(self, book):
    #     self.book = book

new_library = Library()

new_library.add_book(Book(1, "Gone with the Wind", "Margaret Mitchell"))

new_library.add_book(Book(2, "East of Eden", "John Steinbeck"))

new_library.show_books()


