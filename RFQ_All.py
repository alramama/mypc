from tkinter import *
from tkinter import filedialog
import pdfplumber
import pandas as pd
import arabic_reshaper
import pdfplumber
from bidi.algorithm import get_display
import ast
from datetime import date

today = date.today()

import datetime
#import pyarabic.trans
import mysql.connector
from tkinter import *
import io
import os
import glob
b = glob.glob('E:/Desktop all/Desktop 09-2020/تقرير عمل/SEC_RFQ/08.JAN.2023/*.pdf')
import datetime
from datetime import datetime

excel_sheet = []
def entryshhet():
    #a = os.listdir('C:/Users/DELL/Pictures/SEC_RFQ')
    for i in b:
        #file = filedialog.askopenfilename()
        pdf = pdfplumber.open(i)
        n = len(pdf.pages)
        a120 = []
        for page in range(n):
            f = pdf.pages[page].extract_tables()
            #print(f)
            for i in range(len(list(f))):
                for j in range(len(f[i])):
                    a44 = (list(filter(None, f[i][j])))
                    a = []
                    for x in a44:
                        a.append(x.replace("\n", " "))
                    a12 = []
                    for x1 in a:
                        a12.append(x1.replace("(cid:0)", ""))
                        #print(len(a12))
                    if len(a) == 5 or len(a44) == 1 or len(a44)==3 :
                        (a120.append(a))
                        text_to_be_reshaped = str(a12)
                        reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
                        bidi_text = get_display(reshaped_text)
                        res = ast.literal_eval(bidi_text)
                        #print((res))
                        #print(len(a),a)
                    if len(a44)==100:
                        print(a44)
            #print(len(f),f)
        #for i in range(len(a120)):
        flat_list = []
        for sublist in a120:
            for item in sublist:
                flat_list.append(item)
        import numpy as np
        def insert_RFQ():
            listA = flat_list[14:]
            biddate = flat_list[8]
            date_bid = datetime.strptime(biddate, '%m/%d/%Y').date()
            bidclose = flat_list[9]
            date_close = datetime.strptime(bidclose, '%m/%d/%Y').date()

            composite_list = [listA[x:x + 6] for x in range(0, len(listA), 6)]

            for i in range(len(composite_list)):
                a121 = (composite_list[i])
                #print((a121))
                #print(len(a121),flat_list[7],a121[0])
                #print(len(composite_list[i]),composite_list[i])
                try:
                    if len(composite_list[i])==6:
                        Bid_SOW_short= a121[5]
                        val =(flat_list[7],date_bid,date_close,flat_list[11],flat_list[12],(a121[0]),a121[5],a121[3],a121[4],Bid_SOW_short[0:20])
                        excel_sheet.append(val)
                    elif len(composite_list[i]) == 5:
                        val =(flat_list[7],flat_list[8],flat_list[9],flat_list[11],flat_list[12],a121[0],"Unable to insert Please see RFQ",a121[3],a121[4],'Unable to insert Please see RFQ')
                        excel_sheet.append(val)
                except:
                    print("cnnot read the file",flat_list[7])
        insert_RFQ()
    name = today
    df1 = pd.DataFrame(excel_sheet)
    df1.to_excel('E:/Desktop all/Desktop 09-2020/تقرير عمل/SEC_RFQ/05.JAN.2023/' + str(name) +'.xlsx')

entryshhet()


