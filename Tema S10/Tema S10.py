from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

#initializare Chrome

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)


#maximizare fereastra
chrome.maximize_window()

# Test 1 - Intrati pe site-ul https://www.elefant.ro/
chrome.get('https://www.elefant.ro/')

# Acceptare Cookies

WebDriverWait(chrome,10).until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))).click()
sleep(2)

# Test 2 - Cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
#          cel putin 10 rezultate.   ([class="product-title"])
chrome.find_element(By.CSS_SELECTOR, "input[placeholder *= 'codul de produs']").send_keys("samsung s23",Keys.ENTER)
sleep(3)
rezultate_cautare = chrome.find_elements(By.CSS_SELECTOR, ".product-title")
print(f'Numarul de rezultate returnate este: {len(rezultate_cautare)}')

# Test 3 - Extrageti din lista produsul cu prețul cel mai mic [class="current-price "]
#         (puteti sa va folositi de find_elements)
chrome.find_element(By.ID, 'SortingAttribute').click()
sleep(1)
chrome.find_element(By.CSS_SELECTOR, 'option[value="pret-asc"]').click()
sleep(1)
produs = chrome.find_element(By.CSS_SELECTOR,'.js-product-tile-b4ece745-798d-451c-83e3-aaeba1270b9d > div:nth-child(2) > a:nth-child(3) > h2:nth-child(1)').text
print(f'Produsul cu pretul cel mai mic din lista este: {produs}')

# - Test 4: Extrageti titlul paginii si verificati ca este corect (hint: folositi metoda title)

# se verif ca titlul este ok
chrome.get('https://www.elefant.ro/')
titlu_corect = 'elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!'
cautare_titlu  = chrome.title
try:
    assert cautare_titlu == titlu_corect
    print('Titlul paginii este corect.')
except:
    print('Titlul paginii este incorect.')
    print(f'Titlul corect al paginii >>> {cautare_titlu}')

# - Test 5:  Intrati pe site si dati click pe butonul conectare.
#            Identificati elementele de tip user si parola si inserati valori incorecte
#            (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid).
#            Ce tip de testare se aplica aici?
#                - Dati click pe butonul "conectare" si verificati urmatoarele:
#                        1. Faptul ca nu s-a facut logarea in cont
#                        2. Faptul ca se returneaza eroarea corecta


chrome.get('https://www.elefant.ro/')
# dam clic pe butonul "Conectare" de pe pagina
chrome.find_element(By.CSS_SELECTOR,'.login-prompt').click()
sleep(1)
chrome.find_element(By.XPATH, '/html/body/header/div[1]/nav/div[1]/div[4]/div[1]/ul/li/div[2]/a[1]').click()
sleep(1)
chrome.find_element(By.NAME, "ShopLoginForm_Login").send_keys('nickname@email.com')
sleep(1)
chrome.find_element(By.NAME, 'ShopLoginForm_Password').send_keys('password')
sleep(1)
chrome.find_element(By.XPATH, '//*[@name="LoginUserForm"]/div[4]/div[1]').click()

eroare_login_corecta = 'Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou.'
eroare_primita = chrome.find_element(By.XPATH, '/html/body/div[3]/div/div[9]/div[1]/div/div[1]/div/div').text
try:
    assert eroare_login_corecta == eroare_primita
    print('Eroarea returnata este corecta!')
except:
    print('Eroarea returnata nu este cea corecta!')
    print(f'Eroarea corecta este: "{eroare_login_corecta}"')

# - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
#                     si verificati faptul ca butonul "conectare" este dezactivat (hint: folositi metoda isEnabled)

#Stergerea campului email si introducerea unei valori invalide
username = chrome.find_element(By.NAME, "ShopLoginForm_Login")
username.send_keys(Keys.CONTROL, 'a')
sleep(1)
username.send_keys(Keys.BACKSPACE)
sleep(1)
username.send_keys('nickname')
sleep(1)

#Verificarea butonului 'Conectare'
buton_conectare = chrome.find_element(By.XPATH, '//*[@name="LoginUserForm"]/div[4]/div[1]')
if buton_conectare.is_enabled() == True:
    print('Butonul "Conectare" este dezactivat')
else:
    print('Butonul "Conectare" nu este dezactivat')