import pandas as pd
from csv import writer

def Main():
    #Try to open the csv and create it if it doesn't exist
    try:
        open("Books.csv", "a")
    except: 
        open("Books.csv", "x")
    #TODO: convert csv into a data type which is more easily searchable
    #TODO: Prompt user. What are the options? What do they want to do. 
    #Remove books after they are selected or when completed or not at all? 
    #Flag current book and remove it when a new book is chosen


def AddBook():
    #Prompt user for book information
    print("Please enter the following information about the book")
    print("Title:")
    title = input()
    print("Author")
    author=input()
    print("Book series?(y/n)")
    series=input()
    #TODO: Check for input errors
    


if __name__ == "__main__":
    Main()
