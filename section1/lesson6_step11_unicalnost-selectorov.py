from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
    input1.send_keys("Ivan")
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second')
    input1.send_keys("Ivanov")
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third')
    input1.send_keys("II@mail.ru")
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
    time.sleep(2)
    
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(10)
    browser.quit()

