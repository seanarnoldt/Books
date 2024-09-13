class Book():
    title = None
    length = None
    current = False
    currentPage = 0

    def __init__(self, title, length, current=False, currentPage=0):
        self.title = title
        self.length = length
        self.current = current
        self.currentPage = currentPage
    
    def get(self):
        return([self.title, self.length, self.current, self.currentPage])
    
    def setTitle(self, title):
        self.title = title

    def setLength(self, length):
        self.length = length

    def setCurrent(self, current):
        self.current = current

    def setCurrentPage(self, currentPage):
        self.currentPage = currentPage