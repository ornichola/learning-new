import hashlib
import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
    pytest.param(
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
        marks=pytest.mark.xfail(reason='stepik-575-04-03-04')
    ),
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket(product_name=page.product_name, product_price=page.product_price)


@pytest.mark.skip(reason='stepik-575-04-03-06')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='stepik-575-04-03-06')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_fade_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.open()
        email = str(time.time()) + '@fakemail.org'
        page.register_new_user(
            email=email,
            password=hashlib.md5(email.encode('utf-8')).hexdigest()
        )
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.add_to_basket()
        page.should_be_added_to_basket(product_name=page.product_name, product_price=page.product_price)
