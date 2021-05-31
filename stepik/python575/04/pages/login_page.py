from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)
        self.url += '/accounts/login/'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        _current_url = self.browser.current_url
        assert 'accounts/login' in _current_url, 'Not login page opened'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not present'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
