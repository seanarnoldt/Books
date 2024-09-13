import pandas as pd
import sys
import os
import json
import datetime
import math
import gui 

def addBook(books):
    #Prompt user for book information
    book = {}
    print("Please enter the following information about the book")
    print("Title:")
    title = input()
    print("Length: ")
    length = input()
    book["Title"] = title
    book["Length"] = length
    book["Current"] = False
    book["Page"] = 0
    return books

def status(books):
    totalLen = 0
    daysLeft = 0
    current_date = datetime.datetime.now()
    end_of_year = datetime.datetime(current_date.year, 12, 31)
    daysLeft = (end_of_year - current_date).days + 2
    for book in books:
        totalLen += (int(book["Length"]) - int(book["Page"]))
    pagesPerDay = math.ceil(totalLen / daysLeft)
    print(f"To complete all of the books in your backlog by the end of the year you need to read {pagesPerDay} pages per day.")
    for book in books:
        if book["Current"] == True:
            remaining = int(book["Length"]) - int(book["Page"])
            days = math.floor(remaining/pagesPerDay)
            delta = datetime.timedelta(days=days-1)
            targetDate = (current_date + delta)
            title = book["Title"]
            formattedDate = targetDate.strftime("%A, %B %d")
            print(f"Target completion date of {title} is {formattedDate}.")
    return books

def edit(books):
    invalid = True
    while invalid:
        print("Which book would you like to edit?")
        for book in books:
            print(book["Title"])
        editing = input()
        book_edit = None
        for book in books:
            if book["Title"] == editing:
                book_edit = book
                invalid = False
        if book_edit is None:
            print(f"Invalid book selection. Valid options: {books}")
    invalid = True
    while invalid:
        print(f"What would you like to change about {editing}? (complete, current_book, current_page, title, length)")
        choice = input()
        invalid = False
        match choice:
            case "current_book":
                if book_edit["Current"] == False:
                    book_edit["Current"] = True
                else:
                    book_edit["Current"] = False
            case "current_page":
                book_edit["Page"] = input("What page are you on?")
            case "title":
                book_edit["Title"] = input("What is the title of the book?")
            case "length":
                book_edit["Length"] = input("How many pages are in the book?")
            case "complete":
                confirm = input("Are you sure you want to complete this book? It will be removed from your backlog. (y/n)")
                if confirm == "y":
                    for i in range(0, len(books)-1):
                        book = books[i]
                        if book["Title"] == book_edit["Title"]:
                            books.pop(i)
                            break
                elif confirm == "n":
                    print("Operation cancelled")
                else:
                    print("Invalid input")
            case _: 
                invalid = True
                print("Invalid selection. Valid selections: (current_book, current_page, title, length)")
    return books

if __name__ == "__main__":
    file_path = "books.txt"
    if os.path.exists(file_path):
    # Open and read the file
        with open(file_path, 'r') as file:
            try:
                books = json.load(file)
            except json.JSONDecodeError:
                print("Failed to load books from JSON")
    file.close()
        
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
    