import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
#//*[@id="collapse-11AAAAAADOoTpkiJ0lL"]/div/div[2]/div/div[2]/span
#//*[@id="collapse-11AAAAAADPUPY7tAHMh"]/div/div[2]/div/div[2]/span
#//*[@id="accordion"]/div[1]
Path = 'C:\Program Files (x86)\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(Path)
#driver.implicitly_wait(30)
#https://chercher.tech/practice/practice-pop-ups-selenium-webdriver

def etmad14():
     driver.get('https://tenders.etimad.sa/Tender/AllTendersForVisitor')
     time.sleep(5)
     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul/li[4]/a').click()
     time.sleep(5)
     for i in range(5):
          aa = driver.find_elements_by_xpath('//*[@id="cardsresult"]/div[1]/div')
          for i in aa:
               time.sleep(2)
               # a10 = ((i.find_element_by_xpath('parent::div/div').text))
               a10 = (i.text)
               try:

                    if len(str(a10).splitlines()) == 13:
                         a11 = (str(a10).splitlines())
                         print(a11)
                         time.sleep(5)
               except:
                    print("0")

          driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
          time.sleep(5)
          driver.find_element_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul/li[6]/button').click()
etmad14()
def etmad13():
     driver.get('https://tenders.etimad.sa/Tender/AllTendersForVisitor')
     time.sleep(5)
     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul/li[4]/a').click()
     time.sleep(5)
     for i in range(5):
          driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
          time.sleep(5)
          driver.find_element_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul/li[6]/button').click()
#etmad13()
def etmad12():
     driver.get('https://tenders.etimad.sa/Tender/AllTendersForVisitor')
     time.sleep(5)
     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
     time.sleep(5)
     aa= driver.find_elements_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul')
     for i in aa:
          driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
          time.sleep(5)
          i.find_element_by_xpath('li/button').click()
#etmad12()
def etmad11():
     driver.get('https://tenders.etimad.sa/Tender/AllTendersForVisitor')
     time.sleep(5)
     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul/li[5]/button').click()

#etmad11()
def etmad10():
     driver.get('https://tenders.etimad.sa/Tender/AllTendersForVisitor')
     time.sleep(5)
     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
     action = ActionChains(driver)
     time.sleep(5)
     menu = driver.find_element_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul/li[5]/button')
     time.sleep(5)
     action.move_to_element(menu).click().perform()
     time.sleep(10)

#etmad10()
def etmad():
     driver.get('https://tenders.etimad.sa/Tender/AllTendersForVisitor')
     #//*/div/parent::div[@id="accordion"]/div
     #//*[@id="accordion"]/div/parent::div/div/div/div
     time.sleep(5)
     #a = driver.find_element_by_xpath("//div[@id='heading-11AAAAAADUQDvz1tOGEm']")
     aa  = driver.find_elements_by_xpath('//*[@id="cardsresult"]/div[1]/div')
     for i in aa:
          time.sleep(2)
          #a10 = ((i.find_element_by_xpath('parent::div/div').text))
          a10 = (i.text)
          try:

               if len(str(a10).splitlines()) == 13:
                    a11 = (str(a10).splitlines())
                    print(a11)
                    time.sleep(5)
          except:
               print("0")
          time.sleep(5)
          driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
          time.sleep(5)
          driver.find_element_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul/li[5]/button').click()

          #time.sleep(5)
          #driver.find_element_by_xpath('//*[@id="cardsresult"]/div[2]/div/nav/ul/li[5]/button').click()

               #print([a11[2], a11[5], a11[7]])
               #print(a11[2])

"""               if a11[2] == "تامين وتجهيز مشاركة وزارة الداخلية في الأيام العالمية":
                    print(a11)
               else:
                    print("not")
"""
#etmad()
#div/div/div/div/div/div/div/h3/a
def train4():
     driver.get("https://tenders.etimad.sa/Tender/AllTendersForVisitor")
     aa  = driver.find_elements_by_xpath('//*[@id="cardsresult"]/div[1]/div')
     for i in aa:
          time.sleep(2)
          a10 = (i.find_element_by_xpath('//*[@id="cardsresult"]/div[1]/div/div/div/div/div/div/div/div/div/h3/a').text)
          if a10 == "تامين وتجهيز مشاركة وزارة الداخلية في الأيام العالمية ":
               print(100)
     """
     for product in productes:
          producte_name = product.find_element_by_xpath("div/div/div/div/div/h3/a").text
          #product.find_element_by_xpath("div/button").click()
          #print(producte_name)
          if producte_name == "تامين وتجهيز مشاركة وزارة الداخلية في الأيام العالمية":
               #product.find_element_by_xpath("div/button").click()
               print("Ok")
"""
#train4()

def train4():
     driver.get("https://rahulshettyacademy.com/angularpractice/")
     driver.find_element_by_css_selector("a[href*='shop']").click()
     productes = driver.find_elements_by_xpath("//div[@class='card h-100']")
     for product in productes:
          producte_name = product.find_element_by_xpath("div/h4/a").text
          product.find_element_by_xpath("div/button").click()
          #print(producte_name)
          if producte_name == "iphone X":
               product.find_element_by_xpath("div/button").click()

#train4()

def train3():
     driver.get("https://rahulshettyacademy.com/angularpractice/")
     #driver.find_element_by_name("name").send_keys("مرتضى الرمضان")
     #print(driver.find_element_by_name("name").get_attribute("value"))
     #print(driver.execute_script('return document.getElementsByName("name")[0].value'))
     shopButton = driver.find_element_by_css_selector("a[href*='shop']")
     driver.execute_script("arguments[0].click();",shopButton)
     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

#train3()

def train2():
     driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
     action = ActionChains(driver)
     action.context_click(driver.find_element_by_id("double-click")).perform()
     action.double_click(driver.find_element_by_id("double-click")).perform()
     alrt = driver.switch_to.alert
     assert "You double clicked me!!!, You got to be kidding me" == alrt.text
     alrt.accept()
     driver.close()
#train2()
def train1():
     driver.get("https://rahulshettyacademy.com/AutomationPractice/")
     action = ActionChains(driver)
     time.sleep(5)
     menu = driver.find_element_by_id('mousehover')
     time.sleep(5)
     action.move_to_element(menu).perform()
     time.sleep(5)
     indexmnue = driver.find_element_by_xpath('/html/body/div[4]/div/fieldset/div/div/a[2]')
     time.sleep(5)
     action.move_to_element(indexmnue).click().perform()
#train1()
def train():
     driver.get('https://the-internet.herokuapp.com/windows')
     driver.find_element_by_link_text('Click Here').click()
     tab_window = driver.window_handles[1]
     driver.switch_to.window(tab_window)
     print(driver.find_element_by_tag_name('h3').text)
     driver.close()
     driver.switch_to.window(driver.window_handles[0])
#train()

def Tahkom0():
     driver.get('https://www.tahakom.com/tenders')
     #//*/div/parent::div[@id="accordion"]/div
     #//*[@id="accordion"]/div/parent::div/div/div/div
     time.sleep(5)
     #a = driver.find_element_by_xpath("//div[@id='heading-11AAAAAADUQDvz1tOGEm']")
     aa  = driver.find_elements_by_xpath('//*[@id="accordion"]/div')
     for i in aa:
          time.sleep(2)
          #a10 = ((i.find_element_by_xpath('parent::div/div').text))
          (i.click())
          time.sleep(2)
          print(str(i.text).splitlines())
          print("____________________________________________________")

          #print(len(i))

#Tahkom0()

def Tahkom():
     driver.get('https://www.tahakom.com/tenders')
     #//*/div/parent::div[@id="accordion"]/div
     #//*[@id="accordion"]/div/parent::div/div/div/div
     time.sleep(5)
     #a = driver.find_element_by_xpath("//div[@id='heading-11AAAAAADUQDvz1tOGEm']")
     aa  = driver.find_elements_by_xpath('//*[@id="accordion"]/div')
     for i in aa:
          time.sleep(2)
          #a10 = ((i.find_element_by_xpath('parent::div/div').text))
          print(i.text)
          #print(a10)

          #print(len(i))

#Tahkom()
def Tahkom1():
     driver.get('https://www.tahakom.com/tenders')
     #//*/div/parent::div[@id="accordion"]/div
     #//*[@id="accordion"]/div/parent::div/div/div/div
     time.sleep(5)
     #a = driver.find_element_by_xpath("//div[@id='heading-11AAAAAADUQDvz1tOGEm']")
     driver.find_elements_by_class_name('card').click()
     time.sleep(5)
#Tahkom1()

#//*[@id="accordion"]/div/div/div/parent::div/div/div/div

def chamber():
     driver.get('https://www.chamber.sa/ChamberServices/InquiryServices/Tenders/Pages/PublicTenders.aspx')
     #driver.back()
     #//*/div/parent::div[@id="accordion"]/div
     #//*[@id="accordion"]/div/parent::div/div/div/div
     time.sleep(5)
     #a = driver.find_element_by_xpath("//div[@id='heading-11AAAAAADUQDvz1tOGEm']")
     #//*[@id="cbqwpctl00_ctl42_g_4f497b2d_5f18_4eb1_97dc_4c6ac289f225"]/ul/li/div/a
     aa  = driver.find_elements_by_xpath('//*[@id="cbqwpctl00_ctl42_g_4f497b2d_5f18_4eb1_97dc_4c6ac289f225"]/ul/li/div/a')
     for i in aa:
          time.sleep(10)
          #a10 = ((i.find_element_by_xpath('parent::div/div').text))
          i.find_element_by_xpath('//*[@id="cbqwpctl00_ctl42_g_4f497b2d_5f18_4eb1_97dc_4c6ac289f225"]/ul/li/div/a').click()
          #time.sleep(30)
          #driver.find_element_by_xpath('//*[@id="ctl00_ctl42_g_4bd0dd0f_ce96_4d3f_91df_efca8f1e4c38_ctl00_lblShowAttachments"]').click()
          time.sleep(5)
          driver.back()

#chamber()

def chamber1():
     driver.get('https://www.chamber.sa/ChamberServices/InquiryServices/Tenders/Pages/PublicTenders.aspx')
     #driver.back()
     #//*/div/parent::div[@id="accordion"]/div
     #//*[@id="accordion"]/div/parent::div/div/div/div
     time.sleep(2)
     #a = driver.find_element_by_xpath("//div[@id='heading-11AAAAAADUQDvz1tOGEm']")
     #//*[@id="cbqwpctl00_ctl42_g_4f497b2d_5f18_4eb1_97dc_4c6ac289f225"]/ul/li/div/a
     driver.find_element_by_xpath('//*[@id="cbqwpctl00_ctl42_g_4f497b2d_5f18_4eb1_97dc_4c6ac289f225"]/ul/li[1]/div/a').click()
     time.sleep(2)
     driver.find_element_by_xpath('//*[@id="ctl00_ctl42_g_4bd0dd0f_ce96_4d3f_91df_efca8f1e4c38_ctl00_lblShowAttachments"]').click()
     time.sleep(3)
     tab_window = driver.window_handles[1]
     driver.switch_to.window(tab_window)
     driver.switch_to.window(driver.window_handles[1])
     #driver.find_element_by_xpath('//*[@id="icon"]/iron-icon').click()
     time.sleep(3)
     driver.back()
#chamber1()

def nwc():
     driver.get('https://www.nwc.com.sa/Arabic/OurOperations/E-vendors/Pages/Public-Tenders.aspx')
     #//*/div/parent::div[@id="accordion"]/div
     #//*[@id="accordion"]/div/parent::div/div/div/div
     time.sleep(5)
     #a = driver.find_element_by_xpath("//div[@id='heading-11AAAAAADUQDvz1tOGEm']")
     aa  = driver.find_elements_by_xpath('//*[@id="column"]/div/div/a')
     for i in aa:
          time.sleep(2)
          #a10 = ((i.find_element_by_xpath('parent::div/div').text))
          a10 = (i.text)
          print(a10)
#nwc()
