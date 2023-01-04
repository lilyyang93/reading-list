import unittest
from classes.api import API
import requests

"""

app should handle:
-API edge case: when no publisher information is provided
-API edge case: when fewer than the request # of books is returned, such as 3 instead of 5
-API edge case: when no books are returned 

"""

class TestAPI(unittest.TestCase):

    def test_get_books_1(self):
        #this keyword is able to retrieve the requested amount of books 
        keyword = "flowers"
        max = "5"
        books_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={keyword}&projection=lite&maxResults={max}")
        books_data = books_response.json()
        response = books_data.get("items")
        retrieved = len(response) 
        self.assertEqual(retrieved, 5)
    
    def test_get_books_2(self):
        #this keyword (gibberis) is unable to retrieve the requested amount of books 
        keyword = "hiejsk" 
        max = 5
        books_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={keyword}&projection=lite&maxResults={max}")
        books_data = books_response.json()
        response = books_data.get("items")
        retrieved = len(response)
        self.assertEqual(retrieved, 5)

    def test_get_books_3(self):
        #this keyword (gibberish) retrieves 0 books
        keyword = "eiglskehgakegoeigs" 
        max = 5
        books_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={keyword}&projection=lite&maxResults={max}")
        books_data = books_response.json()
        response = books_data.get("items")
        retrieved = len(response)
        self.assertEqual(retrieved, 5)

if __name__ == '__main__':
    unittest.main()
