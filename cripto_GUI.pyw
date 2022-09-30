import copy
import PySimpleGUI as sg
import cryptocode

sg.ChangeLookAndFeel("DarkGrey14")

layout = [
    [sg.Text('Decrypted', pad=0)],
    [sg.Multiline(size=(50, 7), key='IODecrypted'), sg.Button('Encrypt', size=(10, 2),border_width=10, pad=45)],
    [sg.Text('Encrypted')],
    [sg.Multiline(size=(50, 7), key='IOEncrypted'), sg.Button('Decrypt', size=(10, 2),border_width=10, pad=45)],
]
passLayout = [
    [sg.Text('Password', size =(15, 1)), sg.InputText(key='pass')],
    [sg.Button('OK', auto_size_button=True), sg.Button('Cancel', auto_size_button=True)]
]

window = sg.Window(
    'Cripto',
    layout,
    resizable=True,
    finalize=True,
    size=(640, 360), 
    return_keyboard_events=True,
    margins=(0,0),
)
window.bind('<Configure>', "Configure")

def main():
    event, values = window.read()

    if event == 'Encrypt':
        temp = copy.deepcopy(passLayout)
        passWindow = sg.Window(
            'Pass',
            temp,
        )
        event, passValues = passWindow.read()
        if event == 'Cancel':
            passWindow.close()
        if event == 'OK':
            print(passValues.get('pass'))
            print(values.get('IODecrypted'))
            window['IOEncrypted'].update(value = cryptocode.encrypt(values.get('IODecrypted'), passValues.get('pass')))
            passWindow.close()
    if event == 'Decrypt':
        temp = copy.deepcopy(passLayout)
        passWindow = sg.Window(
            'Pass',
            temp,
        )
        event, passValues = passWindow.read()
        if event == 'Cancel':
            passWindow.close()
        if event == 'OK':
            print(passValues.get('pass'))
            print(values.get('IOEncrypted'))
            window['IODecrypted'].update(value = cryptocode.decrypt(values.get('IOEncrypted'), passValues.get('pass')))
            passWindow.close()

    if not (event == sg.WINDOW_CLOSED):
        main()

if __name__ == '__main__':
    main()