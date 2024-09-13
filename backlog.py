import book

class Backlog:
    backlog = []

    def __init__(self):
        self.backlog = []

    def addBook(self, book):
        self.backlog.append(book)

    def removeBook(self, book):
        self.backlog.pop(book)