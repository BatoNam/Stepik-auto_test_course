from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    x = int(browser.find_element(By.ID, "input_value").text)
    y = str(math.log(abs(12*math.sin(x))))
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(5)
    browser.quit()

