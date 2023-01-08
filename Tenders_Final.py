#from webdriver_manager.chrome import ChromeDriverManager
import datetime
from datetime import date

today = date.today()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pdfplumber
import pandas as pd
Path = 'C:/Program Files (x86)/webdriver/chromedriver'
driver = webdriver.Chrome(executable_path=Path)
a = []
def etmad_bid_information3():
    driver.get("https://tenders.etimad.sa/Tender/AllTendersForVisitor")
    time.sleep(5)
    driver.maximize_window()
    #driver.find_element(By.XPATH,'//*[@id="itemsPerPage"]/option[4]').click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[@id='searchBtnColaps']").click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="Search"]/div/div[1]/div/div[2]/a/i').click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(500,850)")
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="dates"]/div/div[5]/div/div/button').click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(700,1000)")
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="dates"]/div/div[5]/div/div/div/ul/li[3]/a/span[1]').click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,0)")
    work_tybe = ['//*[@id="basicInfo"]/div/div[3]/div/div/div/ul/li[10]/a/span[1]', '//*[@id="basicInfo"]/div/div[3]/div/div/div/ul/li[15]/a/span[1]']
    for type in work_tybe:
        time.sleep(15)
        driver.find_element(By.XPATH,'//*[@id="basicInfo"]/div/div[3]/div/div/button').click()
        time.sleep(10)
        driver.find_element(By.XPATH,type).click()
        time.sleep(10)
        driver.execute_script("window.scrollTo(700,1000)")
        time.sleep(10)
        driver.find_element(By.XPATH,"//button[@id='searchBtn']").click()
        time.sleep(10)
        print("ok")
        time.sleep(5)
        bid = driver.find_elements(By.XPATH,'//*[@id="cardsresult"]/div[1]/div/div')
        for i in bid:
            time.sleep(5)
            b = (i.text).splitlines()
            if len(b) == 13:
                a.append(b)
                #for i in bid:
            #print(i.text)
        bid_list = pd.DataFrame(a)
        bid_list.to_excel(str(today) + '.xlsx')
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(10)
etmad_bid_information3()
