from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    
    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check.click()
    
    input_robot = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    input_robot.click()
    
    x_sunduk = browser.find_element(By.CSS_SELECTOR, 'img')
    x = x_sunduk.get_attribute('valuex')
    y = str(math.log(abs(12*math.sin(int(x)))))
    
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()

