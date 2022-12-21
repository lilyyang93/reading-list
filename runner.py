import requests 
from dotenv import load_dotenv 
import os 

load_dotenv()
books_api_key = os.environ.get('apikey')

reading_list = []
selection = input("\n *** Welcome to Google Books! ***\n\nSelect a number:\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")

while selection != '3':
    match selection:
        case '1':
            keyword = input("\nEnter your keyword:\n\n>>>")
            max = 5 

            books_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={keyword}&projection=lite&maxResults={max}&key={books_api_key}")
            books_data = books_response.json()
            try: 
                response = books_data.get("items")
                for i in range(max):
                    title = response[i]["volumeInfo"]["title"]
                    authors = response[i]["volumeInfo"]["authors"] 
                    publisher = response[i]["volumeInfo"].get("publisher", "None")

                    print("\n")
                    print(f"Book {i+1}")
                    print("Title:",title)
                    print("Author(s):",authors)
                    print("Publisher:",publisher)
                    
                selection = input("\nSelect a book number to add it to your reading list. Select 0 to return home.\n\n>>>")

            except:
                print("\nUnable to retrieve books. Please try a different keyword.")
                selection = input("\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")

            if int(selection) >= 1 and int(selection) <= 5:
                my_book = int(selection)
                reading_list.append(response["items"][my_book-1]["volumeInfo"]["title"])

                print("\nYour reading list was updated.")

                selection = input("Select 0 to return home.\n\n>>>")
                
        case '2': 
            if len(reading_list) == 0:
                print("\nYou have not added any books to your reading list.\n")

                selection = input("Select 0 to return home\n\n>>>")
            else:
                print("\nYour reading list: ",reading_list)

                selection = input("\nSelect 0 to return home\n\n>>>")
        
        case _:
            print("Please enter a valid option.\n")
    selection = input("\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")
