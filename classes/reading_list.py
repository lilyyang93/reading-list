#functionality related to getting or updating a user's reading list belong in this class

reading_list = []

class ReadingList:
    def add_to_reading_list(books):
        selection_2 = input("\nSelect a book number to add it to your reading list. Press 0 to return home.\n\n>>>")

        try: 
            if int(selection_2) >= 1 and int(selection_2) <= len(books):
                book_num = int(selection_2)-1
                reading_list.append(books[book_num].title)
                print("\nYour reading list was updated.")

            elif int(selection_2) == 0:
                print("\nReturning home.")
            elif int(selection_2) > len(books):
                print("\nInvalid option, please try again.")
        except:
            print("\nInvalid option, please try again.")

    def get_reading_list():
        if (len(reading_list) == 0):
            print("\nYou have not added any books to your reading list.\n")

        else: 
            print("\nYour reading list: ",reading_list)