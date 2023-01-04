#functionality related to API calls belong in this class

import requests
from classes.book import Book 

class API:
    def get_books(keyword, max):
        books_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={keyword}&projection=lite&maxResults={max}")
        books_data = books_response.json()
        response = books_data.get("items")

        try:
            items_retrieved = len(response)
        except:
            items_retrieved = 0

        if items_retrieved == 0:
            print("\nUnable to retrieve books. Please try a different keyword.")

        elif items_retrieved <= max:
            Book.get_retrieved_books(response, items_retrieved)