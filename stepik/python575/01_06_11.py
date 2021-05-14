from selenium import webdriver
import time


LINK_TO_REG_FORM_V1 = 'http://suninjuly.github.io/registration1.html'
LINK_TO_REG_FORM_V2 = 'http://suninjuly.github.io/registration2.html'
REG_DATA = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john.doe@example.com',
}

browser = webdriver.Chrome()

try:
    browser.get(LINK_TO_REG_FORM_V1)

    # Ваш код, который заполняет обязательные поля
    required_elements = [
        browser.find_element_by_xpath('//*[.="First name*"]/following-sibling::input'),
        browser.find_element_by_xpath('//*[.="Last name*"]/following-sibling::input'),
        browser.find_element_by_xpath('//*[.="Email*"]/following-sibling::input')
    ]
    for element, value in zip(required_elements, REG_DATA.values()):
        element.send_keys(value)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == browser.find_element_by_tag_name("h1").text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
