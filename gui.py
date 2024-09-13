import PySimpleGUI as sg
import book
import backlog
import datetime
import math

def test():
    layout = [[sg.Text("Welcome to Reading Tracker"), [sg.Button("View Books")]]]

    window = sg.Window("Book Tracker", layout)

    while True:
        event, values = window.read()
        if event == "View Books" or event == sg.WIN_CLOSED:
            break

    window.close()

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
            editBooks(bl.backlog)

        if event == "Status":
            status(bl.backlog)

        if event == "View Books":
            displayBooks(bl.backlog)

    window.close()



def displayBooks(bl):
    layout = []
    for book in bl:
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
    for book in bl:
        totalLen += (int(book.length) - int(book.currentPage))
    pagesPerDay = math.ceil(totalLen / daysLeft)
    currentBooks = []
    for book in bl:
        if book.current == True:
            currentBooks.append(book)
    viewStatusLayout = [[sg.Text(f"To complete all of the books in your backlog by the end of the year you need to read {pagesPerDay} pages per day.")]]
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
    for bk in bl:
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
            for bk in bl:
                if bk.title == selectedBook[0]:
                    editBook(bk)
                    break
            continue

    window.close()

def editBook(book):
    editBookLayout = [[sg.Text("Title:"), sg.In(book.title)], 
                      [sg.Text("Length:"), sg.In(book.length)], 
                      [sg.Checkbox("Current book", default=book.current)],
                      [sg.Text("Current page:"), sg.In(book.currentPage)], 
                      [sg.Button("Save")]]
    window = sg.Window(title = f"Edit {book.title}", layout=editBookLayout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Save":
            print(values)

    window.close()