from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from twocaptcha import TwoCaptcha
from solveRecaptcha import solveRecaptcha

solver = TwoCaptcha('6fb9ea7a06972a82eb9fa0c432dd033e')

browser = webdriver.Chrome()
browser.get('https://secure.similarweb.com/account/login?returnUrl=https%3a%2f%2fpro.similarweb.com%2f')

search = browser.find_element(By.XPATH, '//*[@id="input-email"]')
search_2 = browser.find_element(By.ID, "input-password")



result = solveRecaptcha(
    "6Ld9tP8SAAAAAKgr5QDjmeSkBXDIIy6aDRFdgYa8",
    "https://secure.similarweb.com/account/login?returnUrl=https%3a%2f%2fpro.similarweb.com%2f"
)

code = result['code']

print(code)

time.sleep(10)

WebDriverWait(browser, 120).until(
    EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
)



browser.execute_script("document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")





time.sleep(10)




search.send_keys("felipe.mena@andesmotor.cl")
search_2.send_keys("andesmotor")


#browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/button').click()


#xpath del verificar //*[@id="recaptcha-verify-button"]

time.sleep(40)


