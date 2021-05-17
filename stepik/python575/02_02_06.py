"""
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""

import math
import time
from selenium import webdriver


LINK = 'https://suninjuly.github.io/execute_script.html'


driver = webdriver.Chrome()

try:
    driver.get(LINK)
    x = driver.find_element_by_xpath('//*[@id="input_value"]').text
    driver.find_element_by_xpath('//*[@id="answer"]').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    submit_btn = driver.find_element_by_xpath('//button[@type="submit"]')
    driver.execute_script('return arguments[0].scrollIntoView(true);', submit_btn)
    driver.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    driver.find_element_by_xpath('//*[@id="robotsRule"]').click()
    submit_btn.click()

    time.sleep(10)

finally:
    driver.quit()
