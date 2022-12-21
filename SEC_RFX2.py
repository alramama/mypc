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
import glob
b = glob.glob('*.pdf')
import datetime
from datetime import datetime

def entryshhet():
    a = os.listdir('C:/Users/DELL/Pictures/SEC_RFQ')
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

                        Key_word = ['Endpoint','Network', 'Server', 'Communication', 'Radio', 'Router', 'Switch', 'Firewall', 'Optical', 'Fiber', 'Optic', 'VCS', '(Video Conferencing)', 'Video', 'Wall', 'Monitor', 'PAGA', '(Public Address General Alarm)', 'PABX', '(business telephone)', 'Command Room', 'Security', 'Security', 'CCTV', 'Camera', 'Access Control', 'IDAS', 'Intrusion detection and assessment', 'LDAS', 'Long Range Detection Assessment', 'Radar', 'Marine Barrier', 'Floating Barrier', 'Sonar', '(underwater surveillance and detection)', 'Drop Arm', 'Fence', 'Barrier', 'Siren' , 'Cyber', 'Security', 'Cyber', 'Security', 'Firewall', 'System', 'Access', 'Protection']
                        if any(substring in (a121[5]) for substring in Key_word):
                            #print("Yes",flat_list[7],a121[0])
                            def insert():
                                #db = mysql.connector.connect(user='root', host='localhost', database='naizak')
                                db = mysql.connector.connect(host="127.0.0.1", user="root", password="12345678",database="naizak1")
                                cursor = db.cursor()
                                sql ='INSERT INTO bids_rfq(Bidno,Bid_Date,Bid_Close ,Buyer ,Buyer_Tel,Line_no,Bid_SOW,Unit,Qty,Bid_SOW_short) values (%s,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s)'
                                #val =(flat_list[7],flat_list[8],flat_list[9],flat_list[11],flat_list[12],(a121[0]),a121[5],a121[3],a121[4],Bid_SOW_short[0:20])
                                val =(flat_list[7],date_bid,date_close,flat_list[11],flat_list[12],(a121[0]),a121[5],a121[3],a121[4],Bid_SOW_short[0:20])
                                #print(type(flat_list[8]))
                                cursor.execute(sql, val)
                                db.commit()
                                print(cursor.rowcount, flat_list[7], a121[0],'record(s) inserted')
                                cursor.close()
                                db.close()
                            insert()
                    elif len(composite_list[i]) == 5:
                            Key_word = ['Endpoint', 'Network', 'Server', 'Communication', 'Radio', 'Router', 'Switch','Firewall', 'Optical', 'Fiber', 'Optic', 'VCS', '(Video Conferencing System)',
                                        'Video', 'Wall', 'Monitor System', 'PAGA', '(Public Address General Alarm)','PABX', '(business telephone systems)', 'Command Room', 'Security', 'Security',
                                        'CCTV', 'Camera', 'Access Control', 'IDAS','Intrusion detection and assessment systems ', 'LDAS','Long Range Detection Assessment System', 'Radar', 'Marine Barrier','Floating Barrier', 'Sonar', '(underwater surveillance and detection)',
                                        'Drop Arm', 'Fence', 'Barrier', 'Siren', 'Cyber', 'Security', 'Cyber','Security', 'Firewall', 'System', 'Access', 'OT', 'Protection']
                            if any(substring in (a121[4]) for substring in Key_word):
                                #print("Yes", flat_list[7], a121[0])

                                def insert():
                                    db = mysql.connector.connect(host="127.0.0.1", user="root", password="12345678",database="naizak1")
                                    cursor = db.cursor()
                                    sql = 'INSERT INTO bids_rfq (Bidno ,Bid_Date ,Bid_Close ,Buyer,Buyer_Tel,Line_no,Bid_SOW,Unit,Qty,Bid_SOW_short) values (%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s)'
                                    val =(flat_list[7],flat_list[8],flat_list[9],flat_list[11],flat_list[12],a121[0],"Unable to insert Please see RFQ",a121[3],a121[4],'Unable to insert Please see RFQ')
                                    cursor.execute(sql, val)
                                    db.commit()
                                    print(cursor.rowcount, flat_list[7], a121[0], 'record(s) inserted')
                                    cursor.close()
                                    db.close()
                                insert()
                except:
                    print("cnnot read the file",flat_list[7])
        insert_RFQ()
entryshhet()


