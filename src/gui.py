# hello_psg.py

import PySimpleGUI as sg
import piglatintranslator as pls

layout = [
    [sg.Text("Enter your text:")],
    [sg.In(size=(50, 3), enable_events=False, key="-INPUT-"), sg.Button("GO")],
    [sg.Text("See your translation HERE", key = "-RESULT-")]]

# Create the window
window = sg.Window("English-to-Pig-Latin Translator", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "GO":
        result = pls.run(values["-INPUT-"])
        window["-RESULT-"].update(result)

    if event == sg.WIN_CLOSED:
        break

window.close()