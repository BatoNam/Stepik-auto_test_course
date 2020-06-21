from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    
    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    
    input_robot = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_robot)
    input_robot.click()
    
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = str(math.log(abs(12*math.sin(int(x)))))
    
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()

