from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("I")
    input1 = browser.find_element(By.NAME, 'lastname')
    input1.send_keys("I")
    input1 = browser.find_element(By.NAME, 'email')
    input1.send_keys("I")
   
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    upload = browser.find_element(By.ID, 'file')
    upload.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
    time.sleep(2)    
finally:
    time.sleep(10)
    browser.quit()

