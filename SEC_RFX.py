from tkinter import *
from tkinter import filedialog
import pdfplumber
import pandas as pd
import arabic_reshaper
import pdfplumber
from bidi.algorithm import get_display
import ast
import pyarabic.trans
import mysql.connector
from tkinter import *
import io
import os
root = Tk()
root.geometry("500x500")
label = Label( root,relief=RAISED, text = " ETMAD TABLE " ,font= 100 )
label.pack()
ENT = Entry(root)
#file = filedialog.askopenfilename()
label = Label( root, text = "No of table Column" )
label.pack()

No_Colmun = Entry(root)

def entryshhet():

    file = filedialog.askopenfilename()

    pdf = pdfplumber.open(file)
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

                if len(a)== 5 or len(a44)==1 or len(a44)==3 :
                    (a120.append(a))
                if len(a44)==100:
                    print(a44)
        #print(len(f),f)
    #for i in range(len(a120)):
    flat_list = []
    for sublist in a120:
        for item in sublist:
            flat_list.append(item)
    #print(flat_list)
    import numpy as np
    def insert_RFQ():
        listA = flat_list[14:]
        composite_list = [listA[x:x + 6] for x in range(0, len(listA), 6)]
        for i in range(len(composite_list)):
            a121 = (composite_list[i])
            #print(len(composite_list[i]),composite_list[i])
            if len(composite_list[i])==6:
                #print(flat_list[7],flat_list[8],flat_list[9],flat_list[11],flat_list[12],a121[0],a121[1],a121[2],a121[3],a121[4],a121[5])

                def insert():
                    #db = mysql.connector.connect(user='root', host='localhost', database='naizak')
                    db = mysql.connector.connect(host="127.0.0.1", user="root", password="12345678",database="naizak1")

                    cursor = db.cursor()
                    sql ='INSERT INTO films_rfq (Bidno ,Bid_Date ,Bid_Close ,Buyer ,Buyer_Tel,Line_no,Bid_SOW,Unit,Qty) values (%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s)'
                    val =(flat_list[7],flat_list[8],flat_list[9],flat_list[11],flat_list[12],a121[0],a121[5],a121[3],a121[4])
                    cursor.execute(sql, val)
                    db.commit()
                    print(cursor.rowcount,flat_list[7],a121[0], 'record(s) inserted')
                    cursor.close()
                    db.close()
                insert()
            elif len(composite_list[i])==5:
                #print(flat_list[7],flat_list[8],flat_list[9],flat_list[11],flat_list[12],a121[0], a121[1], a121[2], a121[3], a121[4])
                def insert():
                    db = mysql.connector.connect(host="127.0.0.1", user="root", password="12345678",database="naizak1")
                    cursor = db.cursor()
                    sql ='INSERT INTO films_rfq (Bidno ,Bid_Date ,Bid_Close ,Buyer ,Buyer_Tel,Line_no,Bid_SOW,Unit,Qty) values (%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s)'
                    val =(flat_list[7],flat_list[8],flat_list[9],flat_list[11],flat_list[12],a121[0],"Unable to insert Please see RFQ",a121[3],a121[4])
                    cursor.execute(sql, val)
                    db.commit()
                    print(cursor.rowcount,flat_list[7],a121[0], 'record(s) inserted')
                    cursor.close()
                    db.close()
                insert()

    insert_RFQ()



btn = Button(root,text = "INSERT",command = entryshhet)
No_Colmun.pack()
btn.pack()
root.mainloop()


