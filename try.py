from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pdfplumber
import pandas as pd
Path = 'C:\Program Files (x86)\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(Path)

data = []
def train5():
    driver.get("https://www.htmlelements.com/demos/table/overview/")
    action = ActionChains(driver)
    #driver.switch_to.frame("frame_reference")
    driver.switch_to.frame(0)
    #driver.switchTo().frame(0);
    time.sleep(5)
    click = driver.find_element_by_xpath('//*[@id="tableTableContainer"]/tbody/tr[1]/td[3]')
    action.double_click(click)
    #driver.find_element_by_xpath('//*[@id="tableTableContainer"]/tbody/tr[1]/td[3]').click()
    #driver.find_element_by_xpath('//*[@id="tableTableContainer"]/tbody/tr[1]/td[3]').click()
    (driver.find_element_by_xpath('//*[@id="tableTableContainer"]/tbody/tr[1]/td[3]/input').send_keys("ahmed"))
    #time.sleep(10)
train5()

def train1():
    driver.get("https://cosmocode.io/automation-practice-webtable/")
    #table = driver.find_elements_by_xpath('//*[@id="countries"]/tbody/tr[2]')
    table = driver.find_elements_by_xpath('//*[@id="countries"]/tbody/tr[1]/td[1]/strong')
    #print(len(table))
    #print(table.text)
    for i in range(len(table)):
        #print(i.find_element_by_xpath('//*[@id="countries"]/tbody/tr[2]/td[2]/strong').text)
        print((table[i].text))
        #print(table[1].text)
        data.append(table[i].text)
    #print(data)
    #df = pd.DataFrame(data)
    #df.to_excel("boq1.xlsx")
#train1()


def train2():
    driver.get("https://cosmocode.io/automation-practice-webtable/")
    row = len(driver.find_elements_by_xpath('//*[@id="countries"]/tbody/tr'))
    col = len(driver.find_elements_by_xpath('//*[@id="countries"]/tbody/tr[2]/td'))

    for i in range(2,row+1):
        for r in range(1,col+1):
            value = driver.find_element_by_xpath('//*[@id="countries"]/tbody/tr['+str(i)+']/td['+str(r)+']')
            #print(value.text,end=" ")
            data.append(value.text)
    #print(row)
    #print(col)
    df = pd.DataFrame(data)
    df.to_excel("boq2.xlsx")

#train2()

def train3():
    driver.get("https://cosmocode.io/automation-practice-webtable/")

    table = driver.find_elements_by_xpath('//*[@id="countries"]/tbody/tr/td')
    for i in range(len(table)):
        if i>1:
            try:
                Country =(table[i].find_element_by_xpath('//*[@id="countries"]/tbody/tr['+str(i)+']/td[2]').text)
                Capital =(table[i].find_element_by_xpath('//*[@id="countries"]/tbody/tr['+str(i)+']/td[3]').text)
                Currency =(table[i].find_element_by_xpath('//*[@id="countries"]/tbody/tr['+str(i)+']/td[4]').text)
                Primary_Language =(table[i].find_element_by_xpath('//*[@id="countries"]/tbody/tr['+str(i)+']/td[2]').text)
                web_tabel=([Country,Capital,Currency,Primary_Language])
                data.append(web_tabel)
            except:
                break
    df = pd.DataFrame(data)
    df.to_excel("boq3.xlsx")


#train3()

def train4():
    driver.get("https://tablepress.org/demo/")
    page = driver.find_elements_by_xpath('')
    table = driver.find_elements_by_xpath('//*[@id="tablepress-demo"]/tbody/tr/td')
    for i in range(len(table)):
        if i>1:
            try:
                Country =(table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr['+str(i)+']/td[2]').text)
                Capital =(table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr['+str(i)+']/td[3]').text)
                Currency =(table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr['+str(i)+']/td[4]').text)
                Primary_Language =(table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr['+str(i)+']/td[2]').text)
                web_tabel=([Country,Capital,Currency,Primary_Language])
                data.append(web_tabel)
            except:
                break
    df = pd.DataFrame(data)
    df.to_excel("boq4.xlsx")
#train4()

def train5():
    driver.get("https://tablepress.org/demo/")
    for i in range(20):
        table = driver.find_elements_by_xpath('//*[@id="tablepress-demo"]/tbody/tr/td')
        for i in range(len(table)):
            if i > 1:
                try:
                    First_Name = (table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr[' + str(i) + ']/td[1]').text)
                    Last_Name	 = (table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr[' + str(i) + ']/td[2]').text)
                    ZIP = (table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr[' + str(i) + ']/td[3]').text)
                    Birthday = (table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr[' + str(i) + ']/td[4]').text)
                    Points = (table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr[' + str(i) + ']/td[5]').text)
                    Average = (table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr[' + str(i) + ']/td[6]').text)
                    Amount = (table[i].find_element_by_xpath('//*[@id="tablepress-demo"]/tbody/tr[' + str(i) + ']/td[7]').text)
                    web_tabel = ([First_Name, Last_Name, ZIP, Birthday,Points,Average,Amount])
                    data.append(web_tabel)
                except:
                    break

        driver.find_element_by_xpath('//*[@id="tablepress-demo_next"]').click()
    df = pd.DataFrame(data)
    df.to_excel("boq6.xlsx")


#train5()

def train6():
    driver.get("https://tablepress.org/demo/")
    for i in range(10):
        driver.find_element_by_xpath('//*[@id="tablepress-demo_next"]').click()

#train6()

