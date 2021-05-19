"""
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""

import math
import time
from selenium import webdriver


LINK = 'http://suninjuly.github.io/redirect_accept.html'


driver = webdriver.Chrome()

try:
    driver.get(LINK)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.switch_to.window(driver.window_handles[1])
    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    driver.find_element_by_xpath('//*[@id="answer"]').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(10)

finally:
    driver.quit()
