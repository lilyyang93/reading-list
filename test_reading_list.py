import unittest
from classes.reading_list import ReadingList

"""

app should handle:
-if user selects a book # to add to reading list: input should only be valid if it corresponds to a book 
-if user selects 0, return home 
-if user selects a number that is greater than the available book numbers, prompt with error message and return home
-if user selects a non number, prompt with error message and return home 
-if user chooses to view reading list that is empty, display message about no books added
-if user chooses to view reading list that is not empy, display the reading list 

"""

if __name__ == '__main__':
    unittest.main()