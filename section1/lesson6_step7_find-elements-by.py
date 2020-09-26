from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/huge_form.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys('Hacc')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:
    time.sleep(3)
    browser.quit()