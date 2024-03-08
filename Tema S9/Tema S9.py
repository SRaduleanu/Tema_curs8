from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

#initializare Chrome

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)


#maximizare fereastra
chrome.maximize_window()

chrome.get('https://www.elefant.ro/')

# Acceptare Cookies

WebDriverWait(chrome,10).until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))).click()
sleep(2)

# - Test 1: Cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])

chrome.find_element(By.CSS_SELECTOR, "input[placeholder *= 'codul de produs']").send_keys("samsung s23",Keys.ENTER)
sleep(3)
rezultate_cautare = chrome.find_elements(By.CSS_SELECTOR, ".product-title")
assert len(rezultate_cautare) >= 10, "Cautarea nu a avut mai mult de 10 rezultate"
sleep(1)

# - Test 2: Cautati un produs, faceti filtrare dupa categorie (orice categorie doriti) si apoi faceti filtrare dupa pret,
#            dupa care verificati faptul ca toate produsele returnate au pretul in intervalul de filtrare

a = ActionChains(chrome)
a.move_to_element(chrome.find_element(By.CLASS_NAME, 'category-button')).perform()
a.move_to_element(chrome.find_element(By.XPATH, '//*[@class="navbar-nav main-navigation-list"]/li[6]/a')).perform()
sleep(2)
chrome.find_element(By.XPATH, '//*[@class="navbar-nav main-navigation-list"]/li[6]/ul/li[2]/ul/li[3]/a').click()

sleep(3)
chrome.find_element(By.XPATH, '//*[@class="col-md-3"]/div[1]/div[4]/ul[2]/li[3]/a/span').click()
sleep(5)
rezultate_filtrare = chrome.find_element(By.CSS_SELECTOR, 'div[class = "hidden-sm element-count text-nowrap"]').text
print(f'Filtrarea a returnat {rezultate_filtrare}')

# - Test 3: Cautati un produs care nu exista si verifica faptul ca mesajul returnat este: "NU A FOST GĂSIT NICI UN REZULTAT "

chrome.find_element(By.CSS_SELECTOR, "input[placeholder *= 'codul de produs']").send_keys("dddddd",Keys.ENTER)
sleep(3)
rezultat_cautare_inexistent = chrome.find_element(By.CSS_SELECTOR, 'h1[class = "h2"]').text
text_rezultat = 'NU A FOST GĂSIT NICI UN REZULTAT :'
try:
    assert rezultat_cautare_inexistent == text_rezultat
    print('Mesajul returnat este cel corect!')
except:
    print('Mesajul returnat nu este cel corect!')
    print(f'Mesajul corect este: "{text_rezultat}"')
sleep(1)
# - Test 4: Cautati un produs, sortati lista de rezultate in ordine crescatoare dupa pret si verificati faptul ca
#           produsele au fost intr-adevar sortate

chrome.find_element(By.CSS_SELECTOR, "input[placeholder *= 'codul de produs']").send_keys("cimpanzeu",Keys.ENTER)
sleep(1)
chrome.find_element(By.ID, 'SortingAttribute').click()
sleep(1)
chrome.find_element(By.CSS_SELECTOR, 'option[value="pret-asc"]').click()
sleep(1)
try:
    assert chrome.current_url.__contains__('SortingAttribute=pret-asc')
    print('Sortarea dupa pret crescator a fost efectuata cu succes!')
except:
    print('Sortarea dupa pret crescator nu a fost realizata cu succes!')

# - Test 5: Cautati un produs, sorteaza lista de rezultate in ordine descrescatoare dupa pret si verifica faptul ca
#           produsele au fost intr-adevar sortate

chrome.find_element(By.CSS_SELECTOR, "input[placeholder *= 'codul de produs']").send_keys("ochelari",Keys.ENTER)
sleep(1)
chrome.find_element(By.ID, 'SortingAttribute').click()
sleep(1)
chrome.find_element(By.CSS_SELECTOR, 'option[value="pret-desc"]').click()
sleep(1)
try:
    assert chrome.current_url.__contains__('SortingAttribute=pret-desc')
    print('Sortarea dupa pret descrescator a fost efectuata cu succes!')
except:
    print('Sortarea dupa pret descrescator nu a fost realizata cu succes!')

# - Test 6: Intrati pe elefant.ro, dati click pe linkul Contact, si verificati faptul ca nu puteti sa dati submit
#           la formular daca nu sunt completate campurile obligatorii (verificati ca ramaneti pe aceeasi pagina)
#           (hint: folositi metoda current_url)

chrome.find_element(By.CSS_SELECTOR, 'a[title = "Contact"]').click()
chrome.find_element(By.CSS_SELECTOR, 'div[class = "o-btn o-btn-send"]').click()
url_contact = 'https://www.elefant.ro/helpdesk/contact-us'
try:
    assert url_contact == chrome.current_url
    print('Formularul nu a fost trimis cu succes!')
except:
    print('Formularul a fost trimis cu succes!')