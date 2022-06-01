from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from account import *
from datetime import datetime

options= webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('./chromedriver.exe', options=options)
#driver= webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get('https://sillacc.co.kr/member/login?returnURL=/reservation/golf')

#Log-in (success)
driver.find_element(by=By.ID, value='usrId').send_keys(ACCOUNT_ID)
driver.find_element(by=By.ID, value='usrPwd').send_keys(ACCOUNT_PW)
driver.find_element(by=By.ID, value='fnLogin').click()
time.sleep(1)
driver.switch_to.alert.accept()

#Refresh at 10AM (success)
while True:
    if datetime.now().minute == 28:
        driver.refresh()
        break
    else:
        pass

#wait until element comes out (success)
try:
    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'B20220609')))
except:
    print("fail")

#date choice  (input?) (success)
""" date form : this month 'A20220525' / next month 'B20220609' """
driver.find_element(by=By.ID, value='B20220609').click()





#searching empty spots (8~11am)
""" 07:10 //*[@id="tabCourseALL"]/div/div/table/tbody/tr[11] """


#agreement check (xPath 체크 필요)
elem = driver.find_element_by_xpath('//*[@id="html"]')
if elem.is_selected() == False:
    elem.click()
else:
    pass

#final decision (수정 필요)
driver.find_element_by_xpath('//*[@id="golfTimeDiv2"]/div[3]/div/div[1]/button')