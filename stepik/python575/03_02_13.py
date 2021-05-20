"""
Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
"""

import time
import unittest
from selenium import webdriver

LINK_TO_REG_FORM_V1 = 'http://suninjuly.github.io/registration1.html'
LINK_TO_REG_FORM_V2 = 'http://suninjuly.github.io/registration2.html'
REG_DATA = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john.doe@example.com',
}

driver = webdriver.Chrome()


class TestABC(unittest.TestCase):

    def check_form(self, link_to_form):
        try:
            driver.get(link_to_form)
            required_elements = [
                driver.find_element_by_xpath('//*[.="First name*"]/following-sibling::input'),
                driver.find_element_by_xpath('//*[.="Last name*"]/following-sibling::input'),
                driver.find_element_by_xpath('//*[.="Email*"]/following-sibling::input')
            ]
            for element, value in zip(required_elements, REG_DATA.values()):
                element.send_keys(value)

            driver.find_element_by_css_selector("button.btn").click()
            time.sleep(1)
            self.assertEqual(
                'Congratulations! You have successfully registered!',
                driver.find_element_by_tag_name("h1").text
            )
        finally:
            driver.quit()

    def test_reg_form_v1(self):
        self.check_form(LINK_TO_REG_FORM_V1)

    def test_reg_form_v2(self):
        self.check_form(LINK_TO_REG_FORM_V2)


if __name__ == '__main__':
    unittest.main()
