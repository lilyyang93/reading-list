import requests 
from dotenv import load_dotenv 
import os 

load_dotenv()
books_api_key = os.environ.get('apikey')

selection = input("\n *** Welcome to Google Books! ***\n\nSelect a number [1-5]:\n(1) Search for books using a keyword\n\n>>>")

while selection == '1':
    match selection:
        case '1':
            keyword = input("\nEnter your keyword:\n>>>")
            books_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={keyword}&projection=lite&maxResults=5&key={books_api_key}")
            
            response = books_response.json()
            for i in range(4):
                response_title = response["items"][i]["volumeInfo"]["title"]
                response_authors = response["items"][i]["volumeInfo"]["authors"] 
                response_publisher = response["items"][i]["volumeInfo"]["publisher"]

                print("\n")
                print(f"Book {i+1}")
                print("Title: ",response_title)
                print("Author(s): ",response_authors)
                print("Publisher: ",response_publisher)
            
