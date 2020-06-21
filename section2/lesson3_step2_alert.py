from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='ti-ohuel.com'; alert('Пиздиться будешь, OK или OK?')")
    time.sleep(2)
    # alert - окошко только с "ОК". К примеру, согласие на куки
    alert = browser.switch_to.alert
    # confirm - окошко с "ОК" и "отмена". Разрешение на уведомления, как пример
    """
    confirm = browser.switch_to.alert
    confirm.accept()
    confirm.dismiss()
    """
    # prompt - окошко с вводом чего-либо. Например, когда хоходишь в роутер, надо писать admin admin.
    """
    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()
    """
    alert.accept()
    alert_text = alert.text

finally:
    time.sleep(5)
    browser.quit()

