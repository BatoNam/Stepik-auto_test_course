import pytest
from selenium import webdriver
import math
import time


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

#, 236896, 236897,236898, 236899, 236903, 236904, 236905
@pytest.mark.parametrize('lesson_id', [236896, 236897,236898, 236899, 236903, 236904, 236905])
class TestAnswer:
    @pytest.mark.xfail(reason="Answer must be 'Correct!'")
    def test_feedback_should_be_correct(self, browser, lesson_id):
        link = f"https://stepik.org/lesson/{str(lesson_id)}/step/1"
        browser.get(link)
        browser.implicitly_wait(15)
        browser.find_element_by_css_selector(".textarea").send_keys(str(math.log(int(time.time()))))
        browser.find_element_by_css_selector(".submit-submission").click()
        correct_text = browser.find_element_by_css_selector(".smart-hints__hint").text
        print(correct_text)
        assert "Correct!" == correct_text, correct_text
        
# Bottom text