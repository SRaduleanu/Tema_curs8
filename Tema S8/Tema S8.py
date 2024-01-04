from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

#initializare Chrome

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

#maximizare fereastra
chrome.maximize_window()

# Test 1
chrome.get('https://www.elefant.ro/')

# Acceptare Cookies

WebDriverWait(chrome,10).until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))).click()
sleep(2)

# Test 2
chrome.find_element(By.CSS_SELECTOR, "input[placeholder *= 'codul de produs']").send_keys("samsung s23",Keys.ENTER)
sleep(5)
rezultate_cautare = chrome.find_elements(By.CLASS_NAME, "product-title")
print(f'Numarul de rezultate returnate este: {len(rezultate_cautare)}')