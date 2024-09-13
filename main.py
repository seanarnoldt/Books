import pandas as pd
import sys
import os
import json
import datetime
import math
import gui 
import backlog
import book

def initializeBacklog(rawBacklog):
    bl = backlog.Backlog()
    for title in rawBacklog:
        newBook = book.Book(str(title["Title"]), int(title["Length"]), bool(title["Current"]), bool(title["Page"]))
        bl.addBook(newBook)
    return bl

if __name__ == "__main__":
    file_path = "books.txt"
    if os.path.exists(file_path):
    # Open and read the file
        with open(file_path, 'r') as file:
            try:
                rawbacklog = json.load(file)
            except json.JSONDecodeError:
                print("Failed to load books from JSON")
    file.close()
    userBacklog = initializeBacklog(rawBacklog=rawbacklog)

    if len(sys.argv) == 1:
        gui.menu(userBacklog)
    else:    
        if sys.argv[1] == "-a":
            another = True
            while another:
                books = addBook(books)
                print("Add another book? (y/n)")
                response = input()
                if response == 'y':
                    another = True
                elif response == 'n':
                    another = False
                else:
                    print('Invalid input expect y or n')
                    another = False
        if sys.argv[1] == "-s":
            books = status(books)
        if sys.argv[1] == "-e":
            books = edit(books)

        with open(file_path, 'w') as file:
            json.dump(books, file, indent=4)  # Write the dictionary as a JSON string
        file.close()    
        