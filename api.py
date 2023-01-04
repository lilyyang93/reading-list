import requests
from reading_list import add_to_reading_list

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
        for i in range(items_retrieved):
            title = response[i]["volumeInfo"]["title"]
            authors = response[i]["volumeInfo"]["authors"] 
            publisher = response[i]["volumeInfo"].get("publisher", "None")

            print("\n")
            print(f"Book {i+1}")
            print("Title:",title)
            print("Author(s):",authors)
            print("Publisher:",publisher)

        add_to_reading_list(response, items_retrieved)