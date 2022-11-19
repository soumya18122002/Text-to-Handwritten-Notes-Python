import pywhatkit as pwt
from PIL import Image
t2h = input("Enter any text to convert it into the handwritten format\n")
pwt.text_to_handwriting(t2h,"C:\\Users\\dawns\\OneDrive\\Documents\\Python Projects\\09 Text To Handwritten Notes\\handwritten.png",[255,0,255])
filename = "C:\\Users\\dawns\\OneDrive\\Documents\\Python Projects\\09 Text To Handwritten Notes\\handwritten.png"
img = Image.open(filename)
img.show()
