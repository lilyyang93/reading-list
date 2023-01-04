import requests 

reading_list = []
selection = input("\n *** Welcome to Google Books! ***\n\nSelect a number:\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")

while selection != '3':
    match selection:
        case '1':
            keyword = input("\nEnter your keyword:\n\n>>>")
            max = 5 

            books_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={keyword}&projection=lite&maxResults={max}")
            books_data = books_response.json()

            response = books_data.get("items")
            try:
                items_retrieved = len(response)
            except:
                items_retrieved = 0

            if items_retrieved == max:
                for i in range(max):
                    title = response[i]["volumeInfo"]["title"]
                    authors = response[i]["volumeInfo"]["authors"] 
                    publisher = response[i]["volumeInfo"].get("publisher", "None")

                    print("\n")
                    print(f"Book {i+1}")
                    print("Title:",title)
                    print("Author(s):",authors)
                    print("Publisher:",publisher)
                    
                selection_2 = input("\nSelect a book number to add it to your reading list. Press 0 to return home.\n\n>>>")
                try: 
                    if int(selection_2) >= 1 and int(selection_2) <= 5:
                        my_book = int(selection_2)
                        reading_list.append(response[my_book-1]["volumeInfo"]["title"])
                        print("\nYour reading list was updated.")

                    elif int(selection_2) == 0:
                        print("\nReturning home.")
                except:
                    print("\nPlease enter a valid option")

            elif items_retrieved == 0:
                print("\nUnable to retrieve books. Please try a different keyword.")

            elif items_retrieved < max:
                print(f"\nRetrieved {items_retrieved} book(s) using the keyword '{keyword}'.")
                for i in range(items_retrieved):
                    title = response[i]["volumeInfo"]["title"]
                    authors = response[i]["volumeInfo"]["authors"] 
                    publisher = response[i]["volumeInfo"].get("publisher", "None")

                    print("\n")
                    print(f"Book {i+1}")
                    print("Title:",title)
                    print("Author(s):",authors)
                    print("Publisher:",publisher)
                    
                selection_2 = input("\nSelect a book number to add it to your reading list. Press 0 to return home.\n\n>>>")
                try:
                    if int(selection_2) <= items_retrieved and int(selection_2) != 0:
                        my_book = int(selection_2)
                        reading_list.append(response[my_book-1]["volumeInfo"]["title"])
                        print("\nYour reading list was updated.")

                    elif int(selection_2) == 0:
                        print("\nReturning home.")

                except: 
                    print("\nPlease enter a valid option.")
                
        case '2': 
            if len(reading_list) == 0:
                print("\nYou have not added any books to your reading list.\n")

                selection = input("Press any key to return home.\n\n>>>")
            else:
                print("\nYour reading list: ",reading_list)

                selection = input("\nPress any key to return home.\n\n>>>")
        
        case _:
            print("Please enter a valid option.\n")
    selection = input("\n(1) Search for books using a keyword\n(2) View your reading list\n(3) Exit\n\n>>>")
