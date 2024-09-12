import PySimpleGUI as sg

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
    