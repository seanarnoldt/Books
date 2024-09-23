import book
import os
import json

class Backlog:
    backlog = []

    def __init__(self):
        self.backlog = []

    def addBook(self, book):
        self.backlog.append(book)

    def removeBook(self, book):
        for i in range(len(self.backlog)):
            if book.title == self.backlog[i].title:
                self.backlog.pop(i)
        self.saveBacklog()
        
    def loadBacklog(self, file_path = "books.txt"):
        rawBacklog = None
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    rawBacklog = json.load(file)
                except json.JSONDecodeError:
                    print("Failed to load books from JSON")
        else: 
            with open(file_path, 'a') as file:
                pass
        file.close()
        if rawBacklog is not None:
            for title in rawBacklog:
                newBook = book.Book(str(title["Title"]), int(title["Length"]), bool(title["Current"]), int(title["Page"]))
                self.addBook(newBook)
        return self.backlog
    
    def saveBacklog(self, file_path = "books.txt"):
        backlogSave = []
        for title in self.backlog:
            backlogSave.append({"Title":title.title, "Length":title.length, "Current":title.current, "Page":title.currentPage})
        with open(file_path, 'w') as file:
            json.dump(backlogSave, file, indent=4)  # Write the dictionary as a JSON string
        file.close()    