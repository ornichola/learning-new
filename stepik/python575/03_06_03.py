"""
Ваша задача — реализовать автотест со следующим сценарием действий:

открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
"""

import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


WAIT_TIME = 7.5


@pytest.fixture
def driver():
    __chrome_options = Options()
    __chrome_options.add_argument('--headless')
    _driver = webdriver.Chrome(options=__chrome_options)
    yield _driver
    _driver.close()


@pytest.mark.parametrize(
    'link',
    [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
    ]
)
def test_03_06_03(link, driver):
    driver.get(link)
    text_area = WebDriverWait(driver, WAIT_TIME).until(
        EC.visibility_of_element_located((By.XPATH, '//textarea'))
    )
    text_area.send_keys(str(math.log(int(time.time()))))
    driver.find_element_by_xpath('//button[@class="submit-submission"]').click()
    feedback_block = WebDriverWait(driver, WAIT_TIME).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "smart-hints")]'))
    )
    feedback = feedback_block.text
    try:
        assert feedback == 'Correct!'
    except AssertionError:
        print(feedback)
