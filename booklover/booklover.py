#Task 1

import pandas as pd
class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].tolist():
            print(f"{book_name} is already in the book list.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].tolist() 
    
    def num_book_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]
