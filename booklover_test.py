#Task 2

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        bl = BookLover("DingDing", "dingding@example.com", "Fantasy")
        bl.add_book("Harry Potter", 5)
        self.assertTrue("Harry Potter" in bl.book_list["book_name"].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bl = BookLover("Max", "maxly@example.com", "Fantasy")
        bl.add_book("Alice in the Wonderland", 5)
        bl.add_book("Alice in the Wonderland", 4)  
        self.assertEqual(len(bl.book_list[bl.book_list["book_name"] == "Alice in the Wonderland"]), 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bl = BookLover("DongDong", "dongdong@example.com", "Mystery")
        bl.add_book("Sherlock Holmes", 5)
        self.assertTrue(bl.has_read("Sherlock Holmes"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bl = BookLover("Creamie", "creamie@example.com", "Fantasy")
        self.assertFalse(bl.has_read("Ella Enchanted"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bl = BookLover("Eva", "eva@example.com", "Romance")
        bl.add_book("Flipped", 5)
        bl.add_book("Emma", 4)
        bl.add_book("Unbreak My Heart", 3)
        self.assertEqual(bl.num_book_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        bl = BookLover("Rachel", "rachel_c@example.com", "History")
        bl.add_book("Before We Were Yours", 5)
        bl.add_book("Island of the Blue Dolphins", 4)
        bl.add_book("The Silk Roads", 2)
        favs = bl.fav_books()
        self.assertTrue(all(favs["book_rating"] > 3))
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)