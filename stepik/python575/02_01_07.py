"""
Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""

import math
import time
from selenium import webdriver


LINK = 'http://suninjuly.github.io/get_attribute.html'


driver = webdriver.Chrome()

try:
    driver.get(LINK)
    x = driver.find_element_by_xpath('//*[@id="treasure"]').get_attribute('valuex')
    driver.find_element_by_xpath('//*[@id="answer"]').send_keys(str(math.log(abs(12*math.sin(int(x))))))
    driver.find_element_by_xpath('//*[@id="robotCheckbox"]').click()
    driver.find_element_by_xpath('//*[@id="robotsRule"]').click()
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(10)

finally:
    driver.quit()
