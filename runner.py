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
            books_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={keyword}&projection=lite&maxResults=5&key={books_api_key}")
            
            response = books_response.json()
            for i in range(5):
                response_title = response["items"][i]["volumeInfo"]["title"]
                response_authors = response["items"][i]["volumeInfo"]["authors"] 
                response_publisher = response["items"][i]["volumeInfo"]["publisher"]
                print("\n")
                print(f"Book {i+1}")
                print("Title: ",response_title)
                print("Author(s): ",response_authors)
                print("Publisher: ",response_publisher)
            selection = input("\nSelect a book number to add it to your reading list. Select 0 to return home.\n\n>>>")
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
