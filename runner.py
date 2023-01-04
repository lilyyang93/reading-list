from classes.api import API
from classes.reading_list import ReadingList

selection = input("\n *** Welcome to Google Books! ***\n\nSelect a number:\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")

while selection != '3':
    match selection:
        case '1':
            keyword = input("\nEnter your keyword:\n\n>>>")
            max = 5 

            API.get_books(keyword, max)
                
        case '2': 
            ReadingList.get_reading_list()
        
        case _:
            print("Please enter a valid option.\n")
    selection = input("\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")
