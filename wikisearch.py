from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "E:\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
def GetLatestMalaysiaData_func():
    driver.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Malaysia")

    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//tr[12]/td"))
        )
        confirmCaseMalaysia = element.text
        confirmCaseMalaysia = confirmCaseMalaysia.split('[')
        confirmCaseMalaysia = confirmCaseMalaysia[0].replace(',','')
        print("Confirmed Case in Malaysia: " + confirmCaseMalaysia)
    finally:
        pass

    return confirmCaseMalaysia

def GetLatestSingaporeData_func():
    driver.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Singapore")
    try:
        element2 = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//tr[9]/td"))
        )
        confirmCaseSg = element2.text
        confirmCaseSg = confirmCaseSg.split('[')
        confirmCaseSg = confirmCaseSg[0].replace(',','')
        print("Confirmed Case in Singapore: " + confirmCaseSg)
    finally:
        driver.quit()

    return confirmCaseSg
