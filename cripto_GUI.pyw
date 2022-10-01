import copy
import PySimpleGUI as sg
import cryptocode

sg.ChangeLookAndFeel("DarkGrey14")

lay = [
    [sg.Column([[sg.Text('Decrypted', pad=(0,0))]]),
    sg.Column([[sg.Text('', size=(40,0))]]) ,
    sg.Column([[sg.Text('Password') , sg.InputText(key='pass', password_char="*", pad=(0,0), size=(20,0))]])]
]

layout = [
    [sg.Column(lay, pad=0)],
    #[sg.Text('Decrypted', pad=(20,0)), sg.InputText(key='pass', password_char="*", pad=(150,0), size=(50,0))],
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
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Encrypt':
            window['IOEncrypted'].update(value = cryptocode.encrypt(values.get('IODecrypted'), values.get('pass')))
        if event == 'Decrypt':
            window['IODecrypted'].update(value = cryptocode.decrypt(values.get('IOEncrypted'), values.get('pass')))

    
    window.close()

if __name__ == '__main__':
    main()