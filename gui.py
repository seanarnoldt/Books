import PySimpleGUI as sg
import book
import backlog
import datetime
import math

def error(errorMsg):
    layout = [[sg.Text(text_color="red", text=errorMsg), [sg.Button("OK")]]]
    window = sg.Window(title="ERROR", layout=layout)

    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()

def menu(bl):
    layout = [[[sg.Button("View Books")], [sg.Button("Status")], [sg.Button("Add Book")], [sg.Button("Edit Backlog")], [sg.Button("Exit")]]]
    window = sg.Window(title="Book Backlog", layout=layout, element_padding=[10,10], margins=[100,100])
    
    while True: 
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Edit Backlog":
            editBooks(bl)

        if event == "Status":
            status(bl)

        if event == "View Books":
            displayBooks(bl)

        if event == "Add Book":
            addBook(bl)

    window.close()

def addBook(bl):
    layout = [[sg.Text("Title:"), sg.In()], 
                      [sg.Text("Length:"), sg.In()], 
                      [sg.Checkbox("Current book", default=False)],
                      [sg.Text("Current page:"), sg.In(0)], 
                      [sg.Button("Save")]]
    window = sg.Window(title="Add a New Book", layout=layout, element_padding=[10,10])

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Save":
            newBook = book.Book(values[0], values[1], values[2], values[3])
            bl.addBook(newBook)
            bl.saveBacklog()
            break
    window.close()

def displayBooks(bl):
    layout = []
    for book in bl.backlog:
        if book.current:
            layout.append([sg.Text(f"{book.title} {book.length} pages. Currently reading.")])
        else:
            layout.append([sg.Text(f"{book.title} {book.length} pages.")])
    layout.append([sg.Button("Edit Backlog")])
    window = sg.Window(title="Backlog", layout=layout, element_padding=[10,10])

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Edit Backlog":
            editBooks(bl)

    window.close()

def status(bl):
    totalLen = 0
    daysLeft = 0
    current_date = datetime.datetime.now()
    end_of_year = datetime.datetime(current_date.year, 12, 31)
    daysLeft = (end_of_year - current_date).days + 2
    for book in bl.backlog:
        totalLen += (int(book.length) - int(book.currentPage))
    pagesPerDay = math.ceil(totalLen / daysLeft)
    currentBooks = []
    for book in bl.backlog:
        if book.current == True:
            currentBooks.append(book)
    viewStatusLayout = [[sg.Text(f"There are {daysLeft} days left in the year. You have {totalLen} pages left to read.")]]
    viewStatusLayout.append([[sg.Text(f"To complete all of the books in your backlog by the end of the year you need to read {pagesPerDay} pages per day.")]])
    if len(currentBooks) > 0:
        for book in currentBooks:
            remaining = int(book.length) - int(book.currentPage)
            days = math.floor(remaining/pagesPerDay)
            delta = datetime.timedelta(days=days-1)
            targetDate = (current_date + delta)
            title = book.title
            formattedDate = targetDate.strftime("%A, %B %d")
            viewStatusLayout.append([sg.Text(f"Target completion date of {title} is {formattedDate}.")])
    else: 
        viewStatusLayout.append([sg.Text("You have no current book."), sg.Button("Edit Backlog")])
    window = sg.Window(title = "Status", layout = viewStatusLayout, element_padding=[10,10])

    while True: 
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Edit Backlog":
            editBooks(bl)
    window.close()

def editBooks(bl):
    titles = []
    for bk in bl.backlog:
        titles.append(bk.title)

    viewBookLayout = [[sg.Text("Select a book to edit")],
                      [sg.Listbox(titles, size=[30,10], bind_return_key=True, select_mode="LISTBOX_SELECT_MODE_SINGLE", key='-LISTBOX-')], 
                      [sg.Button("Confirm")]]

    window =  sg.Window(title = "Book Backlog", layout=viewBookLayout, element_padding=[10, 10])

    while True: 
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "Confirm":
            selectedBook = values["-LISTBOX-"]
            for bk in bl.backlog:
                if bk.title == selectedBook[0]:
                    editedVals = editBook(bl, bk)
                    if editedVals is not None:
                        bk.setAll(editedVals)
                    break
            bl.saveBacklog()
            continue
    window.close()

def editBook(bl, book):
    editBookLayout = [[sg.Text("Title:"), sg.In(book.title)], 
                      [sg.Text("Length:"), sg.In(book.length)], 
                      [sg.Checkbox("Current book", default=book.current)],
                      [sg.Text("Current page:"), sg.In(book.currentPage)], 
                      [sg.Button("Save"), sg.Button("Complete/Remove")]]
    window = sg.Window(title = f"Edit {book.title}", layout=editBookLayout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Save":
            window.close()
            return(values)
        if event == "Complete/Remove":
            bl.removeBook(book)
            break
    window.close()