"""
Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
"""

import os
import time
from selenium import webdriver


LINK = 'http://suninjuly.github.io/file_input.html'
FILE_NAME = 'file.txt'


driver = webdriver.Chrome()

try:
    driver.get(LINK)
    driver.find_element_by_xpath('//input[@name="firstname"]').send_keys('John')
    driver.find_element_by_xpath('//input[@name="lastname"]').send_keys('Doe')
    driver.find_element_by_xpath('//input[@name="email"]').send_keys('john.doe@example.com')
    if not os.path.isfile(FILE_NAME):
        f = open('file.txt', 'w')
        f.close()
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), FILE_NAME)
    driver.find_element_by_xpath('//*[@id="file"]').send_keys(file_path)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    time.sleep(10)

finally:
    driver.quit()
