from tkinter import filedialog

import pandas as pd
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
import pdfplumber
a=[]

def trin3():
    m = []
    #File = filedialog.askopenfilename()
    pdf = pdfplumber.open('1.pdf')
    n = len(pdf.pages)
    for page in range(n):
        f = pdf.pages[page].extract_tables()
        f2 =f
        for i in range(len(list(f2))):
            for j in range(len(f2[i])):
                c = (list(filter(None, f2[i][j])))
                #print(len(c),c)

                if len(c) == 7  :
                    #print(c)
                    a3 =(c[4].splitlines())
                    for i in a3:
                        print(i[::-1])
                        #print()
                    #m.append(a)
    df1 = pd.DataFrame(m)
    #df1.to_excel("E:/Desktop all/Desktop 09-2020/تقرير عمل/مناقصات ابومحمود/Mawani.xlsx")


trin3()

def arabic_text():

    data = pd.read_excel('Mawani.xlsx')
    data1 = data.to_numpy()
    for i in data1:
        #print(i[0])
        data3 = ((i[0]))
        dat4 = (data3[::-1])
        data5 = (str(dat4).splitlines())
        data6 = (str(data5[::-1]).replace("'", "").replace(',', '').replace('"', '').replace("[", "").replace("]", ''))
        reshaped_text = arabic_reshaper.reshape(str(data6))
        f1 = get_display(reshaped_text)
        print(data6)
        # print()
        # a.append(data6)

        text1 = (data3.splitlines())
        text2 = (text1[::-1])
        for i in text1:
            a0 = (i[::-1])

            a.append(a0)
            #print(str(a).replace("'","").replace(',','').replace('"',''))
    data7 = pd.DataFrame(a)
    # data7.to_excel('NewList2.xlsx')
    # data7.to_csv('NewList2.txt')

    """
   
    """
#arabic_text()


def arabic_text():
    data = pd.read_excel('Mawani.xlsx')
    data1 = data.to_numpy()
    for i in data1:
        # print(i[0])
        data3 = ((i[0]))
        dat4 = (data3[::-1])
        data5 = (str(dat4).splitlines())
        data6 = (str(data5[::-1]).replace("'", "").replace(',', '').replace('"', '').replace("[", "").replace("]", ''))
        reshaped_text = arabic_reshaper.reshape(str(data6))
        f1 = get_display(reshaped_text)
        print(data6)
        # print()
        # a.append(data6)

        text1 = (data3.splitlines())
        text2 = (text1[::-1])
        for i in text1:
            a0 = (i[::-1])

            a.append(a0)
            # print(str(a).replace("'","").replace(',','').replace('"',''))
    data7 = pd.DataFrame(a)
    # data7.to_excel('NewList2.xlsx')
    # data7.to_csv('NewList2.txt')

    """

    """


#arabic_text()

text = """"مﺎﻈﻧ حﻼﺻا
جﺮﺒﻟ ﺾﻳرﺄﺗ
ﻞﻤﺸﻳ تﻻﺎﺼﺗﻻا
ﻦﻣ داﻮﻤﻟا ﺔﻓﺎﻛ
مدﺮﻟا ةدﺎﻋإو ﺮﻔﺤﻟا
ﺾﻳرﺄﺘﻟا نﺎﺒﻀﻗو
ﻞﺑﺎﻴﻛو ﺔﻴﺳﺎﺤﻨﻟا
ﺐﺴﺣ ﺾﻳرﺄﺘﻟا
تﺎﻔﺻاﻮﻤﻟا
ﺔﻴﺳﺎﻴﻘﻟا"
"""

text1 = (text.splitlines())
text2 = (text1[::-1])
for i in text1:
    a0 = (i[::-1])
    #print(a0)
    reshaped_text = arabic_reshaper.reshape(a0)
    f1 = get_display(reshaped_text)

    #a.append(f1)
# print(str(a).replace("'","").replace(',','').replace('"',''))
#data7 = pd.DataFrame(a)
#data7.to_csv('NewList44.txt',encoding='utf8')
from textblob import TextBlob
