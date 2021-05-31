from data import EMPTY_BASKET_MSG_BY_LANG
from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        empty_basket_msg = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG).text
        assert EMPTY_BASKET_MSG_BY_LANG.get(self.browser.language, 'Your basket is empty.') in empty_basket_msg, \
            'Wrong empty basket message'
