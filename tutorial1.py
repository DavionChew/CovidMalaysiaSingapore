from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "E:\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Malaysia")

findConfirmCaseMalaysia = driver.find_element_by_xpath("//tr[11]/td")
confirmCaseMalaysia = findConfirmCaseMalaysia.text 
confirmCaseMalaysia = confirmCaseMalaysia.split('[')
print("Confirmed Case in Malaysia: " + confirmCaseMalaysia[0])

driver.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Singapore")
findConfirmCaseSg = driver.find_element_by_xpath("//tr[9]/td")
confirmCaseSg = findConfirmCaseSg.text 
confirmCaseSg = confirmCaseSg.split('[')
print("Confirmed Case in Singapore: " + confirmCaseSg[0])

driver.quit()