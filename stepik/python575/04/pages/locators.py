from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BTN = (By.XPATH, '//div[contains(@class, "basket")]//a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(BasePageLocators):
    ...


class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    REGISTER_EMAIL = (By.XPATH, '//input[@id="id_registration-email"]')
    REGISTER_PASSWORD = (By.XPATH, '//input[@id="id_registration-password1"]')
    REGISTER_PASSWORD_CONFIRMATION = (By.XPATH, '//input[@id="id_registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators(BasePageLocators):
    ADD_TO_BASKET_BTN = (By.XPATH, '//button[contains(@class, "add-to-basket")]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "main")]//h1')
    PRODUCT_PRICE = (By.XPATH, '//p[contains(@class, "price")]')
    SUCCESS_ADD_MSG = (By.XPATH, '(//div[@id="messages"]//div[@class="alertinner "])[1]')
    BASKET_PRICE_MSG = (By.XPATH, '(//div[@id="messages"]//div[@class="alertinner "])[3]')


class BasketPageLocators(BasePageLocators):
    EMPTY_BASKET_MSG = (By.XPATH, '//div[@id="content_inner"]//p')
    BASKET_ITEMS = (By.XPATH, '//form[@id="basket_formset"]')
