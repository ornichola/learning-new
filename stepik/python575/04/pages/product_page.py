from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    @property
    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    @property
    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_be_added_to_basket(self, product_name=None, product_price=None):
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_MSG).text
        total_price_msg = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MSG).text
        assert success_msg, 'No product adding success message'
        assert total_price_msg, 'No total price in basket message'
        if product_name:
            assert success_msg == f'{product_name} has been added to your basket.', 'Wrong success message'
        if product_price:
            assert f'Your basket total is now {product_price}' in total_price_msg, 'Wrong price in basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_MSG), 'Success message is presented'

    def should_fade_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_MSG), 'Success message is still present'
