from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pdfplumber
Path = 'C:\Program Files (x86)\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(Path)
driver.implicitly_wait(10)

a = ['الاتصالات وتقنية المعلومات','الأمن والسلامة']
a1 = ['//*[@id="basicInfo"]/div/div[3]/div/div/div/ul/li[10]','//*[@id="basicInfo"]/div/div[3]/div/div/div/ul/li[15]']

for i in a1:
    try:
        driver.get('https://tenders.etimad.sa/Tender/AllTendersForVisitor')
        #driver.find_element_by_xpath('//*[@id="itemsPerPage"]/option[2]').click()
        #driver.find_element_by_xpath('//*[@id="itemsPerPage"]/option[2]').click()
        driver.find_element_by_tag_name("button#searchBtnColaps").click()
        driver.find_element_by_xpath('//*[@id="basicInfo"]/div/div[3]/div/div/button').click()
        driver.find_element_by_xpath(i).click()
        driver.find_element_by_tag_name('button#searchBtn').click()
        tender = driver.find_element_by_xpath('//*[@id="cardsresult"]/div[1]').text
        #print(bid)
        a2 = (tender.splitlines())
        #print(a2)
        import numpy as np
        arr = np.array(a2)
        newarr = np.array_split(arr, 12)
        for i in range(len(newarr)):
            print((newarr[i][2],newarr[i][6]))
    except:
        print("no data")

