#objects/functionality related to books should belong in this class 

from classes.reading_list import ReadingList

class Book:
    retrieved_books = []
    def __init__(self, id, title, author, publisher):
        self.id = id #included id attribute for a unique identifier 
        self.title = title
        self.author = author
        self.publisher = publisher 
        # can add more attributes in the future as needed
    
    def display_retrieved_books(books):
        for b in books:
            print("\n")
            print(f"Book", books.index(b)+1)
            print("Title:" ,b.title)
            print("Author(s):" ,b.author)
            print("Publisher:" ,b.publisher)
            
        ReadingList.add_to_reading_list(Book.retrieved_books)
        Book.clear_retrieved_books()
    
    def get_retrieved_books(response, items_retrieved):
        
        for i in range(items_retrieved):
            id = response[i]["id"]
            title = response[i]["volumeInfo"]["title"]
            authors = response[i]["volumeInfo"]["authors"] 
            publisher = response[i]["volumeInfo"].get("publisher", "None")

            i = Book(id, title, authors, publisher)
            Book.retrieved_books.append(i)

        Book.display_retrieved_books(Book.retrieved_books)

    def clear_retrieved_books():
        Book.retrieved_books = []

        
    
