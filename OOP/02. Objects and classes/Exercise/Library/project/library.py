from typing import List, Dict
from ss.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str, List[str]] = {}  # { author: [book1, book2...] }
        self.rented_books: Dict[str, Dict[str: int]] = {}  # { username: { book_name: days_to_return } }

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:  # the book is available
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            # I've made a mistake here by not checking if the username is already in the rented_books
            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        # the book is already rented
        return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in user.books:  # he has the book in his records
            user.books.remove(book_name)

            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"
