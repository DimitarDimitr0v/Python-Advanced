class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0


class Library:
    def __init__(self):
        self.books = []
    
    def find_book(self, title):

        book = [x for x in self.books if x.title == title][0]

        if book:
            return book
 