import unittest
from classes.book import Book

"""

app should handle:
-when books are retrieved, create book objects with correct information
-if no pubisher information available, object should be created with None 
-clear list of retrieved books after creating objects 
-correctly display book information

"""

class TestBook(unittest.TestCase):

    def test_book_init(self):
        #testing creation of book object using the keyword "dogs" and the first book retrieved 
        # Fkg7C9mAS2wC
        # Book 1
        # Title: Dogs
        # Author(s): ['Raymond Coppinger', 'Lorna Coppinger']
        # Publisher: University of Chicago Press
        book = Book("Fkg7C9mAS2wC", "Dogs", ['Raymond Coppinger', 'Lorna Coppinger'], "University of Chicago Press")
        self.assertEqual(book.id,"Fkg7C9mAS2wC") 
        self.assertEqual(book.title,"Dogs") 
        self.assertEqual(book.author,['Raymond Coppinger', 'Lorna Coppinger']) 
        self.assertEqual(book.publisher,"University of Chicago Press") 

if __name__ == '__main__':
    unittest.main()