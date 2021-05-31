import math

from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


BASE_URL = 'http://selenium1py.pythonanywhere.com'


class BasePage:
    def __init__(self, browser, url=None, timeout=0):
        self.browser = browser
        self.url = url if url else BASE_URL
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'User icon is not presented, probably unauthorised user'

    def go_to_basket(self):
        basket_btn = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BTN)
        basket_btn.click()
