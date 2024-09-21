import gui
import backlog
import book
if __name__ == "__main__":
    testBacklog = backlog.Backlog()
    testBacklog.loadBacklog("testBacklog.txt")
    testBook = book.Book("Test", 100)
    testBacklog.addBook(testBook)
    testBacklog.saveBacklog("testBacklog.txt")
