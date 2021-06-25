import subprocess

import cv2
import pytesseract
from tkinter import *
from tkinter import filedialog
import tkinter as tk

pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'
window = Tk()
txtbox1 = tk.Text (font = ("Meiryo UI", 12),height=500, width = 500, state=NORMAL)


def openFile():
    filepath = filedialog.askopenfilename(initialdir="")
    file = open(filepath)
    print(file.name)
    ispath = file.name
    return ispath

def executeImg():
    img = cv2.imread(openFile())
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(pytesseract.image_to_string(img))
    shen = pytesseract.image_to_string(img)

    ##Detecting characters
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    for b in boxes.splitlines():
        # print(b)
        b = b.split(' ')
        # print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255,), 3)

    txtbox1.insert(END,shen)
    cv2.imshow('Result', img)


   #cv2.waitKey(0)

def copy_text():
    txt = txtbox1.get("1.0","end")
    subprocess.run(['clip.exe'], input=txt.strip().encode('utf-16'), check=True)


# Create the display screen object
window.title('Insert image here')
window.geometry('600x400')
button = Button(text="Open", command=executeImg)
button.pack()
copy_button = Button(text="Copy Text", command=copy_text)
copy_button.pack()

txtbox1.pack (expand = 1)

window.mainloop()

