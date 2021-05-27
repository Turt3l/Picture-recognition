import cv2
import pytesseract
import PySimpleGUI as sg
sg.theme("Black")
layout = [  [sg.Text('Enter the name of the picture(Must be in the containing folder)')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Picture recognition', layout)
event, values = window.read()
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread(values[0])
text = pytesseract.image_to_string(img)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == event == "Ok":
        text.replace("", " ")
        print(text)
        break
window.close()
