import PySimpleGUI as sg
import mousePosition as mp
import dataFile
import mainAction

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

layout = [
            [sg.Button('Primeiro Click (Caixa de Texto)')],
            [sg.Text('O que deve ser digitado')],
            [sg.InputText()],
            [[sg.Text('Quantas vezes por minuto')],[sg.InputText()]],
            [sg.Button('Segundo  Click (Botão enviar)')],
            [sg.Button('PLAY')]
             ]

# Create the Window

window = sg.Window('Bot-MaNIerI', layout)
def view():
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'Primeiro Click (Caixa de Texto)':
            print("primeiro botao")
            mp.clic_position()
            cordenadasDialogo = dataFile.CordenadasMouse.cordenada_x , dataFile.CordenadasMouse.cordenada_y
        elif event == 'Segundo  Click (Botão enviar)':
            print("segundo botao")
            mp.clic_position()
            cordenadasEnvia = dataFile.CordenadasMouse.cordenada_x, dataFile.CordenadasMouse.cordenada_y
        elif event == 'PLAY':
            mainAction.play(cordenadasDialogo,cordenadasEnvia,values[0],values[1])
        elif event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        event, values = window.read()
    window.close()