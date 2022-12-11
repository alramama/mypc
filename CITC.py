from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pdfplumber
Path = 'C:\Program Files (x86)\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(Path)
import glob
b = glob.glob('*.pdf')
for i in b:
    def CITC():
        driver.get("https://ers.citc.gov.sa/arabic/workspace/pages/citclogin.aspx")
        time.sleep(1.5)
        driver.find_element_by_xpath("//input[@id='ctl00_ctl41_g_3e06a129_a9dc_4696_8c4a_dfc385c02bcd_ctl00_LoginView1_Login1_UserName']").send_keys("alatraaa@naizak.com")
        time.sleep(1.5)
        driver.find_element_by_xpath("//input[@id='ctl00_ctl41_g_3e06a129_a9dc_4696_8c4a_dfc385c02bcd_ctl00_LoginView1_Login1_Password']").send_keys("Hu@naizak535")
        time.sleep(15)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_3e06a129_a9dc_4696_8c4a_dfc385c02bcd_ctl00_LoginView1_Login1_LoginButton"]').click()
        time.sleep(2)
        driver.get("https://ers.citc.gov.sa/Arabic/Service/Pages/CustomsReleasingSubmit.aspx")
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_Wizard1"]/div[2]/ul/li[3]/button').click()
        # Add invoice
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_btnNewInvoice"]').click()
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_txtInvoice"]').send_keys("G1S004278594")
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_FileUpload1"]').send_keys(os.getcwd()+'/'+i)
        time.sleep(1.5)
        driver.find_element_by_xpath(' //*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_btnAdd"]').click()
        time.sleep(1.5)
        #Add airwaybill
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_btnNewAriwayBill"]').click()
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_txtAirway"]').send_keys('59048211864-AWB')
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_FileUpload2"]').send_keys(os.getcwd()+'/'+i)
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_btnadd2"]').click()
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_txt_PurposeOfImportingTheShipment"]').send_keys("لشبكة عملاء  ")
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_Wizard1"]/div[2]/ul/li[3]/button').click()
        time.sleep(1.5)
        # Add product
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_btn_NewShipmentItem"]').click()
        time.sleep(1.5)
        driver.switch_to.frame('myframe')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_txt_ItemDesc"]').send_keys("جهاز جدار ناري")
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_txt_Quantity"]').send_keys('5')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_txt_amount"]').send_keys('250')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_ddl_CustomTariffCode"]/option[13]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_ddl_ShipmentItemType"]/option[2]').click()
        #driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_btnValidateSparePart"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_txt_DeviceIndustrialModel"]').send_keys('GX 200')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_txt_Manufacturer"]').send_keys("SOPHOS")
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_btnValidate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_txt_CommercialModelAr"]').send_keys('GX 200')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_txt_DeviceDescrAr"]').send_keys('جهاز جدار ناري')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_CustomsReleasingItemsAttachment_btn_Upload"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_CustomsReleasingItemsAttachment_fileUploader"]').send_keys(os.getcwd()+"/"+i)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_CustomsReleasingItemsAttachment_btn_Save"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_f0b7bf53_febe_4cc2_bc87_a33e6d83b458_ctl00_DM_btnSave"]').click()
        #driver.switch_to.default_content()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl41_g_5a2a8880_0d93_4709_a228_3119e1bccd5d_ctl00_DM_Wizard1"]/div[2]/ul/li[3]/button/span').click()
    CITC()
