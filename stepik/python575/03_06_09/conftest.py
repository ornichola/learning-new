import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome', help='Launch specific browser (possible Chrome or Firefox)'
    )
    parser.addoption(
        '--headless', action='store_true', default=False, help='Launch in headless mode'
    )
    parser.addoption(
        '--language', action='store', default='en-gb', help='Choose shop language'
    )


@pytest.fixture(scope='function')
def driver(request):
    _browser = request.config.getoption('browser').lower()
    _language = request.config.getoption('language')
    _is_headless = request.config.getoption('headless')
    if _browser == 'chrome':
        __chrome_options = ChromeOptions()
        __chrome_options.add_experimental_option('prefs', {'intl.accept_languages': _language})
        __chrome_options.headless = _is_headless
        driver = webdriver.Chrome(options=__chrome_options)
    elif _browser == 'firefox':
        __firefox_options = FirefoxOptions()
        __firefox_options.set_preference('intl.accept_languages', _language)
        __firefox_options.headless = _is_headless
        driver = webdriver.Firefox(options=__firefox_options)
    else:
        raise pytest.UsageError('Browser should be Chrome (default) or Firefox')

    yield driver

    driver.quit()
