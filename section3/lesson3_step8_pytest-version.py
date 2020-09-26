from selenium import webdriver
from selenium.webdriver.common.by import By


def fill(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second').send_keys("Ivanov")
    browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third').send_keys("II@mail.ru")
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    return browser.find_element_by_tag_name("h1").text  


class TestLink():
    def test_link1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        assert fill(link1) == "Congratulations! You have successfully registered!", "Error somewhere"

    def test_link2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        assert fill(link2) == "Congratulations! You have successfully registered!", "NoSuchElementException"


if __name__ == "__main__":
    browser.quit()
