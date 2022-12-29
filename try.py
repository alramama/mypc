import ast
import time
import pandas as pd
import pdfplumber
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import filedialog
def trin3():
    m = []
    #open_file = filedialog.askopenfilename()
    pdf = pdfplumber.open('BOQ_Bid.pdf')
    n = len(pdf.pages)
    for page in range(n):
        f = pdf.pages[page].extract_tables()
        reshaped_text = arabic_reshaper.reshape(str(f).replace("\n",""))
        f1 = get_display(reshaped_text)
        f2 = ast.literal_eval(f1)
        for i in range(len(list(f2))):
            for j in range(len(f2[i])):
                Key_word = '(CIDX)'
                a = (list(filter(None, f2[i][j])))
                if len(a) == 3:
                    #print(a)
                    bid_word = ((str(a[0]).split()))
                    #print(bid_word)
                    for word in bid_word:
                        if word == Key_word:
                            a.insert(0,Key_word)
                            #print(a)
                            #new=Key_word[i] , a
                            m.append(a)
    if len(m)>0:
        print(True)
        data = pd.DataFrame(m)
        data.to_excel("Items of" + Key_word + ".xlsx")


trin3()
