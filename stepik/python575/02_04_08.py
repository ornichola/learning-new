"""
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
"""

import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


LINK = 'http://suninjuly.github.io/explicit_wait2.html'

driver = webdriver.Chrome()
try:   
    driver.get(LINK)

    price = WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), '$100')
        )
    driver.find_element_by_xpath('//*[@id="book"]').click()

    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    driver.find_element_by_xpath('//*[@id="answer"]').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(10)

finally:
    driver.quit()
