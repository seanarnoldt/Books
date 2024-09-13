import unittest
import book
import backlog

class testBookClass(unittest.TestCase):
    testBook = book.Book("test book", 100, True, 50)
    def testGet(self):
        self.assertEqual(["test book", 100, True, 50], self.testBook.get())
    
    def testSetName(self):
        self.testBook.setTitle("New Title")
        self.assertEqual("New Title", self.testBook.get()[0])

    def testSetLength(self):
        self.testBook.setLength(200)
        self.assertEqual(200, self.testBook.get()[1])

    def testSetCurrent(self):
        self.testBook.setCurrent(False)
        self.assertEqual(False, self.testBook.get()[2])

    def testSetCurrentPage(self):
        self.testBook.setCurrentPage(100)
        self.assertEqual(100, self.testBook.get()[3])

class testBacklogClass(unittest.TestCase):
    testBook = book.Book("test book", 100, True, 50)
    backlog = backlog.Backlog()
    
    def testAddBook(self):
        self.backlog.addBook(self.testBook)
        self.assertEqual(self.testBook, self.backlog.backlog[0])

    def testRemoveBook(self):
        self.backlog.removeBook(self.testBook)
        self.assertEqual(0, len(self.backlog.backlog))
        
if __name__ == "__main__":
    unittest.main()