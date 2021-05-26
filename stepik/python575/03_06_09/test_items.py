import time


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
TO_BASKET_BTN_LOCATOR = '//button[contains(@class, "add-to-basket")]'


def test_to_basket_btn_on_item_page(driver):
    driver.get(LINK)

    # time.sleep(30)

    to_basket_btn = driver.find_elements_by_xpath(TO_BASKET_BTN_LOCATOR)
    assert to_basket_btn, f'"Add to basket" button is not present on: {driver.current_url}'
