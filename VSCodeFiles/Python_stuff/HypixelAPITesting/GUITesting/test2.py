import PySimpleGUI as sg, random as rand

layout = [[sg.Text('yada yada',size=(30,2),key='-OUTPUT-')],[sg.Button('Exit'),sg.Button('change')]]

window = sg.Window('testing',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'change':
        window['-OUTPUT-'].update(str(rand.randint(0,22)))