# Incepeti sa luati din testele pe care le-ati facut la cele trei sesiuni de selectori (Selectori_P1,
# Selectori_P2,Selectori_P3) si implementati-le in metode de test folosind framework-ul unit test.
# Rulati testele si observati rezultatele.


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.support import expected_conditions as EC


class LOGARE(unittest.TestCase):
   USERNAME = (By.ID, 'user-name')
   PASSWORD = (By.ID, 'password')
   LOGIN_BUTTON = (By.ID, 'login-button')
   ALERT_MESSAGE = (By.CSS_SELECTOR, 'h3[data-test="error"]')
   LOGIN_HEADER = (By.CSS_SELECTOR, 'div[class="login_logo"]')
   LOGIN_VERIFY = (By.CSS_SELECTOR, 'span[class="title"]')


   def setUp(self) -> None:
       s = Service(ChromeDriverManager().install())
       self.chrome = webdriver.Chrome(service=s)
       self.chrome.maximize_window()
       self.chrome.get('https://www.saucedemo.com')


   def tearDown(self) -> None:
       self.chrome.quit()


   @unittest.skip
   def test_check_url(self):
       actual = self.chrome.current_url
       expected = 'https://www.saucedemo.com'
       self.assertEqual(actual, expected, 'The page is not correct')
       sleep(2)


   def test_incorrect_login(self):
       username = self.chrome.find_element(*self.USERNAME)
       username.send_keys("Serban")
       self.assertTrue(username.is_displayed(), "The username was displayed")
       sleep(2)
       password = self.chrome.find_element(*self.PASSWORD)
       password.send_keys("nimic")
       self.assertTrue(password.is_displayed(), "The password was displayed")
       sleep(2)


       login_button = self.chrome.find_element(*self.LOGIN_BUTTON)
       self.assertTrue(login_button.is_displayed(), "The button is displayed")
       login_button.click()
       sleep(2)
       alert_message = self.chrome.find_element(*self.ALERT_MESSAGE)
       self.assertTrue(alert_message.is_displayed(), "The alert is displayed")
       sleep(2)


   def test_correct_login(self):
       username = self.chrome.find_element(*self.USERNAME)
       username.send_keys("standard_user")
       self.assertTrue(username.is_displayed(), "The username was displayed")
       sleep(2)
       password = self.chrome.find_element(*self.PASSWORD)
       password.send_keys("secret_sauce")
       self.assertTrue(password.is_displayed(), "The password was displayed")
       sleep(2)


       login_button = self.chrome.find_element(*self.LOGIN_BUTTON)
       self.assertTrue(login_button.is_displayed(), "The button is displayed")
       login_button.click()
       sleep(2)


   def test_failed_header(self):
       header = self.chrome.find_element(*self.LOGIN_HEADER).text
       expected_header = "Swag Laboratories"
       self.assertEqual(header, expected_header, "The header did not match.")
       sleep(2)


   def test_correct_header(self):
       header = self.chrome.find_element(*self.LOGIN_HEADER).text
       expected_header = "Swag Labs"
       self.assertEqual(header, expected_header, "The header matched.")
       sleep(2)
