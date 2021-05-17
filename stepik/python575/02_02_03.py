"""
Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное рассчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания
"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


LINK = 'http://suninjuly.github.io/selects2.html'


driver = webdriver.Chrome()

try:
    driver.get(LINK)
    select = Select(driver.find_element_by_xpath('//select[@id="dropdown"]'))
    select.select_by_value(str(
        int(driver.find_element_by_xpath('//*[@id="num1"]').text) +
        int(driver.find_element_by_xpath('//*[@id="num2"]').text)
    ))
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(10)

finally:
    driver.quit()
