from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    """
    Ноут и инет долгий, не успевал нажать на кнопку... пришлось делать цикл, пока не успеет
    """
    while len(browser.window_handles) == 1:
        redirect = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
        redirect.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = str(math.log(abs(12*math.sin(x))))
    
    browser.find_element(By.ID, 'answer').send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(6)
    browser.quit()

