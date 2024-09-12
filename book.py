class book():
    title = None
    length = None
    current = False
    currentPage = 0

    def __init__(self, title, length, current=False, currentPage=0):
        self.title = title
        self.length = length
        self.current = False
        self.currentPage = currentPage
    
    def get(self):
        return([self.title, self.length, self.current, self.currentPage])
    