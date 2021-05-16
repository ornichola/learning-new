"""
Ваша программа должна выполнить следующие шаги:

Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
"""

import math
import time
from selenium import webdriver


LINK = 'http://suninjuly.github.io/math.html'


driver = webdriver.Chrome()

try:
    driver.get(LINK)
    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    driver.find_element_by_xpath('//*[@id="answer"]').send_keys(str(math.log(abs(12*math.sin(int(x))))))
    driver.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    driver.find_element_by_xpath('//*[@id="robotsRule"]').click()
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(10)

finally:
    driver.quit()
