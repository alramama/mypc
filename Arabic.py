text = []
a0 = [['لﺎﺼﺗﻻا', 'ﺰﻛﺮﻣ', 'ﻲﺗﻮﺼﻟا', 'ﺪﻳﺮﺒﻟا', 'ﻒﺗﺎﻬﻟا', 'مﺎﻈﻧ', 'ـﻟ ةﺰﻬﺟﻷا', 'مداﻮﺧ'],['تاﻮﻨﺳ', 'ثﻼﺛ', 'ةﺪﻤﻟ ﻢﻋد', 'ةﺰﻬﺟﻷا', 'مداﻮﺧ'],['تاﻮﻨﺳ', 'ثﻼﺛ ةﺪﻤﻟ', 'ﻢﻋد ﻊﻣ', 'ﺔﻴﺳﺎﺳأ', 'ﺔﻴﻔﺗﺎﻫ', 'ﺔﺼﺧر'],['تاﻮﻨﺳ', 'ثﻼﺛ ةﺪﻤﻟ', 'ﻢﻋد ﻊﻣ', 'ﺔﻣﺪﻘﺘﻣ', 'ﺔﻴﻔﺗﺎﻫ', 'ﺔﺼﺧر']]
for j in a0:
    for i in j[::-1]:
        print(i[::-1])
        text.append(i[::-1])
    text.append(" ")
print(text)
    #for i in a1:
    	#text.append(i[::-1])
#print(' '.join(text))