"""
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
"""


import math
import time
from selenium import webdriver


LINK = 'http://suninjuly.github.io/alert_accept.html'


driver = webdriver.Chrome()

try:
    driver.get(LINK)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.switch_to.alert.accept()
    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    driver.find_element_by_xpath('//*[@id="answer"]').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(10)

finally:
    driver.quit()
