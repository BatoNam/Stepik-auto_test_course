from selenium import webdriver
from selenium.webdriver.common.by import By
import time



link = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.implicitly_wait(5)
    '''
    time.sleep(3)
    метод не очень, т.к. на разных машинах сайт может загружаться по разному
    инет тоже влияет. так что лучше использовать просмотр элемента каждые 0.5 сек в течение x секунд.
    '''
    
    # Верификация
    browser.find_element(By.CSS_SELECTOR, "#verify").click()
    
    # Подтверждение работы кнопки
    verify = browser.find_element(By.ID, "verify_message").text
    
    assert "Verification was successful!" in verify
    
finally:
    time.sleep(4)
    browser.quit()

