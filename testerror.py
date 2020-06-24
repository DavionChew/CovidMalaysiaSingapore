import time, os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

exePath = './driver/chromedriver.exe'
logPath = os.path.join(os.getcwd(),'logs','chromedriver.log')
serviceArgs = ["--log-level=INFO", "--readable-timestamp", "--append-log"]

# service = Service(executable_path=exePath, log_path=logPath, service_args=serviceArgs)
service = Service(log_path=logPath, service_args=serviceArgs)
service.start()
print(service.service_url)
print(service.process.pid)

# driver = webdriver.Remote(service.service_url)
# Update to remove infobars and save password popups

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
prefs = {"profile.password_manager_enabled": False, "credentials_enable_service": False}
options.add_experimental_option("prefs", prefs)
caps = options.to_capabilities()

driver = webdriver.Remote(service.service_url, desired_capabilities=caps)

# driver = webdriver.Remote('http://localhost:63404')
driver.get('http://www.google.com/')
driver.maximize_window()
time.sleep(3) # Let the user actually see something!
driver.get("https://github.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.close()
driver.quit()
service.stop()