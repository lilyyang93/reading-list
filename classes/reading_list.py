reading_list = []

class ReadingList:
    def add_to_reading_list(response, items_retrieved):
        selection_2 = input("\nSelect a book number to add it to your reading list. Press 0 to return home.\n\n>>>")
        try: 
            if int(selection_2) >= 1 and int(selection_2) <= items_retrieved:
                my_book = int(selection_2)
                reading_list.append(response[my_book-1]["volumeInfo"]["title"])
                print("\nYour reading list was updated.")

            elif int(selection_2) == 0:
                print("\nReturning home.")
        except:
            print("\nPlease enter a valid option")

    def get_reading_list():
        if (len(reading_list) == 0):
            print("\nYou have not added any books to your reading list.\n")

        else: 
            print("\nYour reading list: ",reading_list)