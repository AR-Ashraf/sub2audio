import pytesseract
from PIL import Image


directory = "c:\\Users\\AR\\Desktop\\Capture.png"
image = Image.open(directory)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image,lang = 'eng')
print(text)
