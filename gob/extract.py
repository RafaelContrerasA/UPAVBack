from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Users\Usuario\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open("image.png")

resultado = pytesseract.image_to_string(img, lang='es')

print(resultado)



#descarga una imagen y en image.open remplazala
# Paquetes PIP necesarios:
# pytesseract: pip install pytesseract
# Pillow: pip install Pillow
# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe