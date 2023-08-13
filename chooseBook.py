import pandas as pd

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
    

if __name__ == "__main__":
    Main()
