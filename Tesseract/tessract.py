from PIL import Image
import pytesseract
from tkinter import filedialog
import arabic_reshaper
import pdfplumber
from bidi.algorithm import get_display
import cv2
import re
import glob
import numpy as np

#file = filedialog.askopenfilename()
pytesseract.tesseract_cmd = r"C:\Tesseract"
b = glob.glob('*.jpg')
for img1 in glob.glob("*.jpg"):
    myfile =  Image.open(img1)
    #myfile =  Image.open("0.jpg")
    #text = pytesseract.image_to_string(myfile,lang ='eng')
    text = pytesseract.image_to_string(myfile)
    x1 = re.findall("\d+\.\d+", str(text))
    try:
        a = ["1", "2", "-3"]
        print(img1,':',  [max(float(x) for x in x1)])
        # [1, 2, -3]    #print('file name: ',img1,'',max(int(x1)))
    except:
        print(img1)