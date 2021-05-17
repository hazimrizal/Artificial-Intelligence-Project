# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
import fibonacci as fibonacci
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'
img = cv2.imread('TESTSHENDONG (2).png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))

##Detecting characters
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    #print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w, hImg-h), (0,0,255,), 3)

cv2.imshow('Result', img)
cv2.waitKey(0)

