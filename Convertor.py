import pyautogui
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img  = Image.open("att.png")
new_size=tuple(5*x for x in img.size)
img=img.resize(new_size,Image.LANCZOS)
output = pytesseract.image_to_string(img)
print(output)