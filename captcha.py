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
    "6LfEq1gUAAAAACEE4w7Zek8GEmBooXMMWDpBjI6r",
    "https://secure.similarweb.com/account/login?returnUrl=https%3a%2f%2fpro.similarweb.com%2f"
)

code = result['code']

print(code)


#para iterar hacer un while

ele = browser.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')
browser.execute_script("arguments[0].style.display = 'block';",ele)
browser.execute_script("arguments[0].removeAttribute('style')",ele)



element = browser.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')
browser.execute_script(f"arguments[0].innerText = '{code}'", element)


'''
ele = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div/div/div/div[1]/iframe')
browser.execute_script("arguments[0].submit();",ele)
'''

time.sleep(10)




search.send_keys("nicolas.lizama@kaufmann.cl")
search_2.send_keys("nicolas.lizama")

time.sleep(7)

browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/button').click()



#xpath del verificar //*[@id="recaptcha-verify-button"]

time.sleep(30)


#https://www.youtube.com/watch?v=0tYFZp_EVbQ
#?invisible=false