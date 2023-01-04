import requests 
from api import get_books
from reading_list import get_reading_list

selection = input("\n *** Welcome to Google Books! ***\n\nSelect a number:\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")

while selection != '3':
    match selection:
        case '1':
            keyword = input("\nEnter your keyword:\n\n>>>")
            max = 5 

            get_books(keyword, max)
                
        case '2': 
            get_reading_list()
        
        case _:
            print("Please enter a valid option.\n")
    selection = input("\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")
