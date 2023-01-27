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
browser.get('https://secure.similarweb.com/account/login?returnUrl=%2f')
#https://secure.similarweb.com/account/login?returnUrl=%2fm (con captcha)
#https://secure.similarweb.com/account/login?returnUrl=https%3a%2f%2fpro.similarweb.com%2f (sin captcha)
search = browser.find_element(By.XPATH, '//*[@id="input-email"]')
search_2 = browser.find_element(By.ID, "input-password")



result = solveRecaptcha(
    "6Ld9tP8SAAAAAKgr5QDjmeSkBXDIIy6aDRFdgYa8",
    "https://secure.similarweb.com/account/login?returnUrl=https%3a%2f%2fpro.similarweb.com%2f"
)

code = result['code']

print(code)

#time.sleep(10)

WebDriverWait(browser, 120).until(
    EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
)

findtable = browser.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')


#browser.execute_script("document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")
#findtable.send_keys(code)
'''
textarea = browser.find_element(By.ID, 'g-recaptcha-response')
textarea.click()
textarea.clear()
textarea.send_keys(str(code))
print('listo')


textarea = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'g-recaptcha-response')))
textarea.click()
textarea.clear()
textarea.send_keys(str(code))
'''

#browser.execute_script(f'document.getElementsById("g-recaptcha-response")[0].value={code}')
element = browser.find_element(By.ID, 'g-recaptcha-response')
browser.execute_script(f"arguments[0].innerText = '{code}'", element)



time.sleep(10)
