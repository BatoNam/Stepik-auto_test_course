from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    answer = int(num1) + int(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(f"{answer}") # ищем элемент с текстом "Python"
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()

